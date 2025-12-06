"""
Gesture Recognition Module

This module identifies specific hand gestures from hand landmarks and maps them to actions.
It uses finger states and hand positions to recognize common gestures like pointing,
pinching, peace sign, open palm, fist, and thumbs up/down.

Supported Gestures:
- POINT: Index finger extended, others folded (cursor control)
- PINCH: Thumb and index finger close together (click/select)
- PEACE: Index and middle fingers extended (right click)
- PALM: All fingers extended (pause/stop)
- FIST: All fingers folded (scroll mode)
- THUMB_UP: Only thumb extended upward (scroll up)
- THUMB_DOWN: Only thumb extended downward (scroll down)

Author: Hand Gesture Control Team
Purpose: Assistive technology for users with mobility limitations
"""

import math
import time
from typing import Optional, Tuple, List
from enum import Enum


class Gesture(Enum):
    """Enumeration of recognized gestures"""
    NONE = "none"
    POINT = "point"           # Index finger pointing
    PINCH = "pinch"           # Thumb and index close
    PEACE = "peace"           # V sign (index + middle)
    PALM = "palm"             # Open hand
    FIST = "fist"             # Closed fist
    THUMB_UP = "thumb_up"     # Thumbs up
    THUMB_DOWN = "thumb_down" # Thumbs down
    GRAB = "grab"             # Pinch and hold


class GestureRecognizer:
    """
    Recognizes hand gestures from landmark data
    
    This class analyzes hand landmarks to identify specific gestures and
    implements debouncing to prevent rapid gesture switching.
    """
    
    def __init__(self, debounce_time: float = 0.5):
        """
        Initialize gesture recognizer
        
        Args:
            debounce_time (float): Minimum time (seconds) between gesture changes
        """
        self.debounce_time = debounce_time
        self.current_gesture = Gesture.NONE
        self.last_gesture_time = 0
        self.gesture_start_time = 0
    
    def calculate_distance(self, point1: Tuple[float, float, float], 
                          point2: Tuple[float, float, float]) -> float:
        """
        Calculate Euclidean distance between two 3D points
        
        Args:
            point1: First point (x, y, z)
            point2: Second point (x, y, z)
            
        Returns:
            float: Distance between points
        """
        return math.sqrt(
            (point1[0] - point2[0]) ** 2 +
            (point1[1] - point2[1]) ** 2 +
            (point1[2] - point2[2]) ** 2
        )
    
    def recognize_gesture(self, landmarks: List[Tuple[float, float, float]], 
                         finger_states: dict) -> Gesture:
        """
        Recognize gesture from hand landmarks and finger states
        
        Args:
            landmarks: List of 21 hand landmarks (x, y, z) normalized coordinates
            finger_states: Dictionary of finger states {'thumb': bool, 'index': bool, ...}
            
        Returns:
            Gesture: Recognized gesture enum
        """
        if not landmarks or not finger_states:
            return Gesture.NONE
        
        # Count extended fingers
        extended_count = sum(finger_states.values())
        
        # Get key landmarks for gesture detection
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        
        # Calculate distance between thumb and index (for pinch detection)
        pinch_distance = self.calculate_distance(thumb_tip, index_tip)
        
        # Gesture recognition logic
        gesture = Gesture.NONE
        
        # PINCH: Thumb and index finger close together (distance < 0.05)
        if pinch_distance < 0.05:
            gesture = Gesture.PINCH
        
        # PALM: All 5 fingers extended
        elif extended_count == 5:
            gesture = Gesture.PALM
        
        # FIST: No fingers extended or only thumb
        elif extended_count == 0 or (extended_count == 1 and finger_states['thumb']):
            # Check if thumb is pointing up or down
            if finger_states['thumb']:
                # Thumb up if thumb tip y < wrist y
                if thumb_tip[1] < landmarks[0][1]:
                    gesture = Gesture.THUMB_UP
                else:
                    gesture = Gesture.THUMB_DOWN
            else:
                gesture = Gesture.FIST
        
        # POINT: Only index finger extended
        elif (finger_states['index'] and not finger_states['middle'] and 
              not finger_states['ring'] and not finger_states['pinky']):
            gesture = Gesture.POINT
        
        # PEACE: Index and middle fingers extended
        elif (finger_states['index'] and finger_states['middle'] and 
              not finger_states['ring'] and not finger_states['pinky']):
            gesture = Gesture.PEACE
        
        # Apply debouncing to prevent rapid gesture changes
        current_time = time.time()
        
        if gesture != self.current_gesture:
            # Only change gesture if enough time has passed
            if current_time - self.last_gesture_time >= self.debounce_time:
                self.current_gesture = gesture
                self.last_gesture_time = current_time
                self.gesture_start_time = current_time
        
        return self.current_gesture

    def get_gesture_duration(self) -> float:
        """
        Get how long the current gesture has been held

        Returns:
            float: Duration in seconds
        """
        return time.time() - self.gesture_start_time

    def is_gesture_held(self, duration: float) -> bool:
        """
        Check if current gesture has been held for specified duration

        Args:
            duration (float): Required hold duration in seconds

        Returns:
            bool: True if gesture held long enough
        """
        return self.get_gesture_duration() >= duration

    def get_gesture_name(self) -> str:
        """
        Get human-readable name of current gesture

        Returns:
            str: Gesture name
        """
        return self.current_gesture.value

    def reset(self):
        """
        Reset gesture state
        """
        self.current_gesture = Gesture.NONE
        self.last_gesture_time = 0
        self.gesture_start_time = 0

