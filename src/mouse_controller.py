"""
Mouse Controller Module

This module handles mouse cursor movement and click actions based on hand gestures.
It provides smooth cursor movement, click detection, drag-and-drop functionality,
and scrolling capabilities.

Features:
- Smooth cursor movement with configurable sensitivity
- Left and right click simulation
- Drag and drop support
- Scroll up/down functionality
- Screen boundary handling
- Movement smoothing to reduce jitter

Author: Hand Gesture Control Team
Purpose: Assistive technology for users with mobility limitations
"""

import pyautogui
import numpy as np
from typing import Tuple, Optional
import time


class MouseController:
    """
    Controls mouse cursor and click actions
    
    This class translates hand positions to mouse movements and gestures to clicks.
    It includes smoothing algorithms to prevent jittery cursor movement.
    """
    
    def __init__(self, 
                 screen_width: int = 1920,
                 screen_height: int = 1080,
                 sensitivity: float = 1.5,
                 smoothing_factor: float = 0.5):
        """
        Initialize mouse controller
        
        Args:
            screen_width (int): Screen width in pixels
            screen_height (int): Screen height in pixels
            sensitivity (float): Movement sensitivity multiplier (higher = faster)
            smoothing_factor (float): Smoothing factor (0-1, higher = smoother but slower)
        """
        # Get actual screen size
        self.screen_width, self.screen_height = pyautogui.size()
        
        # Override with config if provided
        if screen_width > 0:
            self.screen_width = screen_width
        if screen_height > 0:
            self.screen_height = screen_height
        
        self.sensitivity = sensitivity
        self.smoothing_factor = smoothing_factor
        
        # Previous cursor position for smoothing
        self.prev_x = 0
        self.prev_y = 0
        
        # Click state tracking
        self.is_clicking = False
        self.is_dragging = False
        self.last_click_time = 0
        self.click_cooldown = 0.3  # Minimum time between clicks
        
        # PyAutoGUI settings
        pyautogui.FAILSAFE = True  # Move mouse to corner to abort
        pyautogui.PAUSE = 0.01     # Small pause between actions
    
    def move_cursor(self, hand_x: float, hand_y: float, frame_width: int, frame_height: int):
        """
        Move cursor based on hand position with smoothing
        
        Args:
            hand_x (float): Hand x position in frame (normalized 0-1)
            hand_y (float): Hand y position in frame (normalized 0-1)
            frame_width (int): Width of camera frame
            frame_height (int): Height of camera frame
        """
        # Convert normalized coordinates to screen coordinates
        # Flip x-axis for mirror effect
        screen_x = int((1 - hand_x) * self.screen_width * self.sensitivity)
        screen_y = int(hand_y * self.screen_height * self.sensitivity)
        
        # Apply smoothing using exponential moving average
        if self.prev_x == 0 and self.prev_y == 0:
            # First movement, no smoothing
            self.prev_x = screen_x
            self.prev_y = screen_y
        else:
            # Smooth the movement
            screen_x = int(self.smoothing_factor * self.prev_x + (1 - self.smoothing_factor) * screen_x)
            screen_y = int(self.smoothing_factor * self.prev_y + (1 - self.smoothing_factor) * screen_y)
            
            self.prev_x = screen_x
            self.prev_y = screen_y
        
        # Clamp to screen boundaries
        screen_x = max(0, min(screen_x, self.screen_width - 1))
        screen_y = max(0, min(screen_y, self.screen_height - 1))
        
        # Move the cursor
        try:
            pyautogui.moveTo(screen_x, screen_y)
        except pyautogui.FailSafeException:
            print("Mouse moved to corner - FailSafe triggered")
    
    def left_click(self):
        """
        Perform left mouse click with cooldown
        """
        current_time = time.time()
        
        # Check cooldown to prevent multiple rapid clicks
        if current_time - self.last_click_time >= self.click_cooldown:
            pyautogui.click()
            self.last_click_time = current_time
            print("Left click")
    
    def right_click(self):
        """
        Perform right mouse click with cooldown
        """
        current_time = time.time()
        
        if current_time - self.last_click_time >= self.click_cooldown:
            pyautogui.rightClick()
            self.last_click_time = current_time
            print("Right click")
    
    def start_drag(self):
        """
        Start drag operation (mouse down)
        """
        if not self.is_dragging:
            pyautogui.mouseDown()
            self.is_dragging = True
            print("Drag started")
    
    def stop_drag(self):
        """
        Stop drag operation (mouse up)
        """
        if self.is_dragging:
            pyautogui.mouseUp()
            self.is_dragging = False
            print("Drag stopped")

    def scroll(self, direction: str, amount: int = 3):
        """
        Scroll the mouse wheel

        Args:
            direction (str): 'up' or 'down'
            amount (int): Scroll amount (number of clicks)
        """
        if direction == 'up':
            pyautogui.scroll(amount)
            print(f"Scroll up {amount}")
        elif direction == 'down':
            pyautogui.scroll(-amount)
            print(f"Scroll down {amount}")

    def double_click(self):
        """
        Perform double click
        """
        current_time = time.time()

        if current_time - self.last_click_time >= self.click_cooldown:
            pyautogui.doubleClick()
            self.last_click_time = current_time
            print("Double click")

    def get_cursor_position(self) -> Tuple[int, int]:
        """
        Get current cursor position

        Returns:
            Tuple[int, int]: (x, y) cursor coordinates
        """
        return pyautogui.position()

    def reset_smoothing(self):
        """
        Reset smoothing values (useful when hand tracking is lost)
        """
        self.prev_x = 0
        self.prev_y = 0

    def set_sensitivity(self, sensitivity: float):
        """
        Update cursor sensitivity

        Args:
            sensitivity (float): New sensitivity value
        """
        self.sensitivity = max(0.1, min(sensitivity, 5.0))  # Clamp between 0.1 and 5.0
        print(f"Sensitivity set to {self.sensitivity}")

    def set_smoothing(self, smoothing: float):
        """
        Update smoothing factor

        Args:
            smoothing (float): New smoothing factor (0-1)
        """
        self.smoothing_factor = max(0.0, min(smoothing, 1.0))  # Clamp between 0 and 1
        print(f"Smoothing set to {self.smoothing_factor}")

