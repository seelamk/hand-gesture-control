"""
Smoothing Utilities

This module provides various smoothing algorithms to reduce jitter and noise
in hand tracking data, resulting in smoother cursor movement and more stable
gesture recognition.

Algorithms:
- Exponential Moving Average (EMA)
- Simple Moving Average (SMA)
- Kalman Filter (simplified)
- Low-pass filter

Author: Hand Gesture Control Team
Purpose: Assistive technology for users with mobility limitations
"""

import numpy as np
from collections import deque
from typing import Tuple, Optional


class ExponentialMovingAverage:
    """
    Exponential Moving Average (EMA) smoother
    
    Gives more weight to recent values while still considering historical data.
    Good for real-time applications with low latency.
    """
    
    def __init__(self, alpha: float = 0.5):
        """
        Initialize EMA smoother
        
        Args:
            alpha (float): Smoothing factor (0-1). Higher = less smoothing, more responsive
        """
        self.alpha = alpha
        self.prev_value = None
    
    def smooth(self, value: float) -> float:
        """
        Apply EMA smoothing to a value
        
        Args:
            value (float): Current value
            
        Returns:
            float: Smoothed value
        """
        if self.prev_value is None:
            self.prev_value = value
            return value
        
        smoothed = self.alpha * value + (1 - self.alpha) * self.prev_value
        self.prev_value = smoothed
        return smoothed
    
    def smooth_point(self, x: float, y: float) -> Tuple[float, float]:
        """
        Smooth a 2D point
        
        Args:
            x (float): X coordinate
            y (float): Y coordinate
            
        Returns:
            Tuple[float, float]: Smoothed (x, y) coordinates
        """
        if self.prev_value is None:
            self.prev_value = (x, y)
            return (x, y)
        
        smoothed_x = self.alpha * x + (1 - self.alpha) * self.prev_value[0]
        smoothed_y = self.alpha * y + (1 - self.alpha) * self.prev_value[1]
        
        self.prev_value = (smoothed_x, smoothed_y)
        return (smoothed_x, smoothed_y)
    
    def reset(self):
        """Reset the smoother"""
        self.prev_value = None


class SimpleMovingAverage:
    """
    Simple Moving Average (SMA) smoother
    
    Averages the last N values. Provides good smoothing but introduces latency.
    """
    
    def __init__(self, window_size: int = 5):
        """
        Initialize SMA smoother
        
        Args:
            window_size (int): Number of values to average
        """
        self.window_size = window_size
        self.values = deque(maxlen=window_size)
    
    def smooth(self, value: float) -> float:
        """
        Apply SMA smoothing to a value
        
        Args:
            value (float): Current value
            
        Returns:
            float: Smoothed value
        """
        self.values.append(value)
        return sum(self.values) / len(self.values)
    
    def smooth_point(self, x: float, y: float) -> Tuple[float, float]:
        """
        Smooth a 2D point using separate queues for x and y
        
        Args:
            x (float): X coordinate
            y (float): Y coordinate
            
        Returns:
            Tuple[float, float]: Smoothed (x, y) coordinates
        """
        if not hasattr(self, 'x_values'):
            self.x_values = deque(maxlen=self.window_size)
            self.y_values = deque(maxlen=self.window_size)
        
        self.x_values.append(x)
        self.y_values.append(y)
        
        smoothed_x = sum(self.x_values) / len(self.x_values)
        smoothed_y = sum(self.y_values) / len(self.y_values)
        
        return (smoothed_x, smoothed_y)
    
    def reset(self):
        """Reset the smoother"""
        self.values.clear()
        if hasattr(self, 'x_values'):
            self.x_values.clear()
            self.y_values.clear()


class OneEuroFilter:
    """
    One Euro Filter - Advanced smoothing with adaptive cutoff
    
    Provides excellent smoothing while maintaining responsiveness.
    Automatically adjusts smoothing based on movement speed.
    """
    
    def __init__(self, min_cutoff: float = 1.0, beta: float = 0.007):
        """
        Initialize One Euro Filter
        
        Args:
            min_cutoff (float): Minimum cutoff frequency
            beta (float): Speed coefficient
        """
        self.min_cutoff = min_cutoff
        self.beta = beta
        self.prev_value = None
        self.prev_time = None

