"""
Hand Tracking Module using MediaPipe

This module provides real-time hand detection and landmark tracking using Google's MediaPipe.
It detects up to 21 landmarks per hand and provides normalized coordinates for each point.

Key Features:
- Real-time hand detection from webcam feed
- 21 landmark points per hand (fingertips, joints, palm, wrist)
- Normalized coordinates (0-1 range) for screen-independent processing
- Configurable detection and tracking confidence thresholds

Landmark Index Reference:
0: Wrist
1-4: Thumb (CMC, MCP, IP, Tip)
5-8: Index finger (MCP, PIP, DIP, Tip)
9-12: Middle finger (MCP, PIP, DIP, Tip)
13-16: Ring finger (MCP, PIP, DIP, Tip)
17-20: Pinky finger (MCP, PIP, DIP, Tip)

Author: Hand Gesture Control Team
Purpose: Assistive technology for users with mobility limitations
"""

import cv2
import mediapipe as mp
import numpy as np
from typing import Optional, List, Tuple, Dict


class HandTracker:
    """
    Hand tracking class using MediaPipe Hands solution
    
    This class handles webcam input, hand detection, and landmark extraction.
    It provides methods to get hand positions and draw visual feedback.
    """
    
    def __init__(self, 
                 max_hands: int = 1,
                 min_detection_confidence: float = 0.7,
                 min_tracking_confidence: float = 0.5):
        """
        Initialize the hand tracker
        
        Args:
            max_hands (int): Maximum number of hands to detect (1 or 2)
            min_detection_confidence (float): Minimum confidence for hand detection (0.0-1.0)
            min_tracking_confidence (float): Minimum confidence for hand tracking (0.0-1.0)
        """
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        # Create Hands object with specified parameters
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,  # False for video stream
            max_num_hands=max_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        
        # Store current frame and results
        self.frame = None
        self.results = None
        self.frame_height = 0
        self.frame_width = 0
    
    def process_frame(self, frame: np.ndarray) -> bool:
        """
        Process a video frame to detect hands
        
        Args:
            frame (np.ndarray): Input frame from webcam (BGR format)
            
        Returns:
            bool: True if hand(s) detected, False otherwise
        """
        self.frame = frame
        self.frame_height, self.frame_width, _ = frame.shape
        
        # Convert BGR to RGB (MediaPipe uses RGB)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame to detect hands
        self.results = self.hands.process(rgb_frame)
        
        # Return True if hands are detected
        return self.results.multi_hand_landmarks is not None
    
    def get_hand_landmarks(self, hand_index: int = 0) -> Optional[List[Tuple[float, float, float]]]:
        """
        Get normalized landmarks for a specific hand
        
        Args:
            hand_index (int): Index of the hand (0 for first hand, 1 for second)
            
        Returns:
            Optional[List[Tuple[float, float, float]]]: List of (x, y, z) coordinates (normalized 0-1)
                                                         or None if hand not detected
        """
        if not self.results or not self.results.multi_hand_landmarks:
            return None
        
        if hand_index >= len(self.results.multi_hand_landmarks):
            return None
        
        hand_landmarks = self.results.multi_hand_landmarks[hand_index]
        
        # Extract all 21 landmarks
        landmarks = []
        for landmark in hand_landmarks.landmark:
            landmarks.append((landmark.x, landmark.y, landmark.z))
        
        return landmarks
    
    def get_landmark_position(self, landmark_id: int, hand_index: int = 0) -> Optional[Tuple[int, int]]:
        """
        Get pixel coordinates of a specific landmark
        
        Args:
            landmark_id (int): ID of the landmark (0-20)
            hand_index (int): Index of the hand (0 or 1)
            
        Returns:
            Optional[Tuple[int, int]]: (x, y) pixel coordinates or None if not found
        """
        landmarks = self.get_hand_landmarks(hand_index)
        
        if not landmarks or landmark_id >= len(landmarks):
            return None
        
        # Convert normalized coordinates to pixel coordinates
        x = int(landmarks[landmark_id][0] * self.frame_width)
        y = int(landmarks[landmark_id][1] * self.frame_height)
        
        return (x, y)

    def draw_landmarks(self, frame: np.ndarray, hand_index: int = 0) -> np.ndarray:
        """
        Draw hand landmarks and connections on the frame

        Args:
            frame (np.ndarray): Frame to draw on
            hand_index (int): Index of the hand to draw

        Returns:
            np.ndarray: Frame with landmarks drawn
        """
        if not self.results or not self.results.multi_hand_landmarks:
            return frame

        if hand_index >= len(self.results.multi_hand_landmarks):
            return frame

        # Draw landmarks and connections
        self.mp_drawing.draw_landmarks(
            frame,
            self.results.multi_hand_landmarks[hand_index],
            self.mp_hands.HAND_CONNECTIONS,
            self.mp_drawing_styles.get_default_hand_landmarks_style(),
            self.mp_drawing_styles.get_default_hand_connections_style()
        )

        return frame

    def get_finger_states(self, hand_index: int = 0) -> Optional[Dict[str, bool]]:
        """
        Determine which fingers are extended (up) or folded (down)

        This is useful for gesture recognition. A finger is considered "up" if its
        tip is higher (lower y-value) than its PIP joint.

        Args:
            hand_index (int): Index of the hand

        Returns:
            Optional[Dict[str, bool]]: Dictionary with finger states
                                       {'thumb': bool, 'index': bool, 'middle': bool,
                                        'ring': bool, 'pinky': bool}
                                       or None if hand not detected
        """
        landmarks = self.get_hand_landmarks(hand_index)

        if not landmarks:
            return None

        # Landmark indices for fingertips and joints
        # Thumb: tip=4, IP=3
        # Index: tip=8, PIP=6
        # Middle: tip=12, PIP=10
        # Ring: tip=16, PIP=14
        # Pinky: tip=20, PIP=18

        finger_states = {
            'thumb': landmarks[4][0] < landmarks[3][0] if landmarks[4][0] < 0.5 else landmarks[4][0] > landmarks[3][0],  # Thumb uses x-axis
            'index': landmarks[8][1] < landmarks[6][1],   # Tip higher than PIP joint
            'middle': landmarks[12][1] < landmarks[10][1],
            'ring': landmarks[16][1] < landmarks[14][1],
            'pinky': landmarks[20][1] < landmarks[18][1]
        }

        return finger_states

    def get_hand_center(self, hand_index: int = 0) -> Optional[Tuple[int, int]]:
        """
        Get the center point of the hand (palm center)

        Args:
            hand_index (int): Index of the hand

        Returns:
            Optional[Tuple[int, int]]: (x, y) pixel coordinates of palm center
        """
        landmarks = self.get_hand_landmarks(hand_index)

        if not landmarks:
            return None

        # Calculate center using wrist (0) and middle finger MCP (9)
        center_x = int((landmarks[0][0] + landmarks[9][0]) / 2 * self.frame_width)
        center_y = int((landmarks[0][1] + landmarks[9][1]) / 2 * self.frame_height)

        return (center_x, center_y)

    def release(self):
        """
        Release MediaPipe resources

        Call this when done using the hand tracker to free up resources.
        """
        self.hands.close()

