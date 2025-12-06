"""
Feedback Utilities

This module provides visual and audio feedback to help users understand
what gestures are being recognized and what actions are being performed.

Features:
- Visual overlays showing current gesture
- On-screen indicators for actions
- Audio feedback for gesture changes
- Status messages and notifications
- Accessibility-friendly feedback options

Author: Hand Gesture Control Team
Purpose: Assistive technology for users with mobility limitations
"""

import cv2
import numpy as np
from typing import Tuple, Optional


class VisualFeedback:
    """
    Provides visual feedback on the camera feed
    
    This class draws overlays, status messages, and indicators to help
    users understand the system's current state.
    """
    
    def __init__(self, show_fps: bool = True, show_gesture: bool = True):
        """
        Initialize visual feedback
        
        Args:
            show_fps (bool): Whether to display FPS counter
            show_gesture (bool): Whether to display current gesture
        """
        self.show_fps = show_fps
        self.show_gesture = show_gesture
        self.fps = 0
        
        # Colors (BGR format)
        self.COLOR_GREEN = (0, 255, 0)
        self.COLOR_RED = (0, 0, 255)
        self.COLOR_BLUE = (255, 0, 0)
        self.COLOR_YELLOW = (0, 255, 255)
        self.COLOR_WHITE = (255, 255, 255)
        self.COLOR_BLACK = (0, 0, 0)
    
    def draw_text(self, frame: np.ndarray, text: str, position: Tuple[int, int],
                  color: Tuple[int, int, int] = None, font_scale: float = 0.7,
                  thickness: int = 2, background: bool = True) -> np.ndarray:
        """
        Draw text on frame with optional background
        
        Args:
            frame (np.ndarray): Frame to draw on
            text (str): Text to display
            position (Tuple[int, int]): (x, y) position
            color (Tuple[int, int, int]): Text color (BGR)
            font_scale (float): Font size scale
            thickness (int): Text thickness
            background (bool): Whether to draw background rectangle
            
        Returns:
            np.ndarray: Frame with text drawn
        """
        if color is None:
            color = self.COLOR_WHITE
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # Get text size for background
        (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)
        
        x, y = position
        
        # Draw background rectangle
        if background:
            cv2.rectangle(frame, 
                         (x - 5, y - text_height - 5),
                         (x + text_width + 5, y + baseline + 5),
                         self.COLOR_BLACK, -1)
        
        # Draw text
        cv2.putText(frame, text, (x, y), font, font_scale, color, thickness)
        
        return frame
    
    def draw_gesture_indicator(self, frame: np.ndarray, gesture_name: str,
                               position: Tuple[int, int] = (10, 30)) -> np.ndarray:
        """
        Draw current gesture name on frame
        
        Args:
            frame (np.ndarray): Frame to draw on
            gesture_name (str): Name of current gesture
            position (Tuple[int, int]): Position to draw at
            
        Returns:
            np.ndarray: Frame with gesture indicator
        """
        # Choose color based on gesture
        color_map = {
            'point': self.COLOR_GREEN,
            'pinch': self.COLOR_BLUE,
            'peace': self.COLOR_YELLOW,
            'palm': self.COLOR_RED,
            'fist': self.COLOR_WHITE,
            'thumb_up': self.COLOR_GREEN,
            'thumb_down': self.COLOR_RED,
            'none': self.COLOR_WHITE
        }
        
        color = color_map.get(gesture_name.lower(), self.COLOR_WHITE)
        text = f"Gesture: {gesture_name.upper()}"
        
        return self.draw_text(frame, text, position, color, font_scale=0.8, thickness=2)
    
    def draw_fps(self, frame: np.ndarray, fps: float,
                 position: Tuple[int, int] = None) -> np.ndarray:
        """
        Draw FPS counter on frame
        
        Args:
            frame (np.ndarray): Frame to draw on
            fps (float): Current FPS value
            position (Tuple[int, int]): Position to draw at
            
        Returns:
            np.ndarray: Frame with FPS counter
        """
        if position is None:
            # Default to top-right corner
            position = (frame.shape[1] - 150, 30)
        
        self.fps = fps
        text = f"FPS: {fps:.1f}"
        
        return self.draw_text(frame, text, position, self.COLOR_GREEN, font_scale=0.6)
    
    def draw_status_message(self, frame: np.ndarray, message: str,
                           duration: float = 2.0) -> np.ndarray:
        """
        Draw a temporary status message
        
        Args:
            frame (np.ndarray): Frame to draw on
            message (str): Status message
            duration (float): How long to show message (seconds)
            
        Returns:
            np.ndarray: Frame with status message
        """
        # Center position
        height, width = frame.shape[:2]
        position = (width // 2 - 100, height - 50)
        
        return self.draw_text(frame, message, position, self.COLOR_YELLOW, 
                            font_scale=0.8, thickness=2)
    
    def draw_cursor_indicator(self, frame: np.ndarray, position: Tuple[int, int],
                             radius: int = 10, color: Tuple[int, int, int] = None) -> np.ndarray:
        """
        Draw a circle at cursor position
        
        Args:
            frame (np.ndarray): Frame to draw on
            position (Tuple[int, int]): Cursor position
            radius (int): Circle radius
            color (Tuple[int, int, int]): Circle color
            
        Returns:
            np.ndarray: Frame with cursor indicator
        """
        if color is None:
            color = self.COLOR_GREEN
        
        cv2.circle(frame, position, radius, color, 2)
        cv2.circle(frame, position, 2, color, -1)
        
        return frame

