"""
Utilities Package

This package contains utility modules for the Hand Gesture Control System.

Modules:
- smoothing: Algorithms for smoothing hand tracking data
- calibration: User calibration and profile management
- feedback: Visual and audio feedback utilities

Author: Hand Gesture Control Team
"""

from .smoothing import ExponentialMovingAverage, SimpleMovingAverage, OneEuroFilter
from .calibration import Calibration
from .feedback import VisualFeedback

__all__ = [
    'ExponentialMovingAverage',
    'SimpleMovingAverage',
    'OneEuroFilter',
    'Calibration',
    'VisualFeedback'
]

