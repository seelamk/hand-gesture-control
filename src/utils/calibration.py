"""
Calibration Utilities

This module provides calibration tools to customize the system for individual users.
It helps users set up optimal sensitivity, screen boundaries, and gesture thresholds
based on their specific needs and physical capabilities.

Features:
- Screen boundary calibration
- Sensitivity adjustment
- Gesture threshold tuning
- User profile management
- Accessibility presets

Author: Hand Gesture Control Team
Purpose: Assistive technology for users with mobility limitations
"""

import json
import os
from typing import Dict, Any, Optional


class Calibration:
    """
    Calibration manager for user-specific settings
    
    This class helps users calibrate the system to their needs and saves
    personalized settings for future sessions.
    """
    
    def __init__(self, profile_name: str = "default"):
        """
        Initialize calibration manager
        
        Args:
            profile_name (str): Name of the user profile
        """
        self.profile_name = profile_name
        self.profile_dir = "profiles"
        self.profile_path = os.path.join(self.profile_dir, f"{profile_name}.json")
        
        # Create profiles directory if it doesn't exist
        os.makedirs(self.profile_dir, exist_ok=True)
        
        # Load or create profile
        self.settings = self._load_profile()
    
    def _load_profile(self) -> Dict[str, Any]:
        """
        Load user profile from file
        
        Returns:
            Dict[str, Any]: Profile settings
        """
        if os.path.exists(self.profile_path):
            try:
                with open(self.profile_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading profile: {e}")
                return self._get_default_settings()
        else:
            return self._get_default_settings()
    
    def _get_default_settings(self) -> Dict[str, Any]:
        """
        Get default calibration settings
        
        Returns:
            Dict[str, Any]: Default settings
        """
        return {
            "mouse_sensitivity": 1.5,
            "smoothing_factor": 0.5,
            "gesture_debounce": 0.5,
            "click_hold_duration": 0.3,
            "screen_boundaries": {
                "left": 0,
                "right": 1920,
                "top": 0,
                "bottom": 1080
            },
            "gesture_thresholds": {
                "pinch_distance": 0.05,
                "finger_extension_threshold": 0.6
            },
            "accessibility": {
                "high_contrast": False,
                "large_cursor": False,
                "audio_feedback": False,
                "reduced_motion": False
            }
        }
    
    def save_profile(self):
        """
        Save current settings to profile file
        """
        try:
            with open(self.profile_path, 'w') as f:
                json.dump(self.settings, f, indent=2)
            print(f"Profile '{self.profile_name}' saved successfully")
        except Exception as e:
            print(f"Error saving profile: {e}")
    
    def get_setting(self, key: str, default: Any = None) -> Any:
        """
        Get a calibration setting
        
        Args:
            key (str): Setting key (supports dot notation)
            default (Any): Default value if not found
            
        Returns:
            Any: Setting value
        """
        keys = key.split('.')
        value = self.settings
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set_setting(self, key: str, value: Any):
        """
        Set a calibration setting
        
        Args:
            key (str): Setting key (supports dot notation)
            value (Any): New value
        """
        keys = key.split('.')
        current = self.settings
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
    
    def calibrate_screen_boundaries(self, left: int, right: int, top: int, bottom: int):
        """
        Calibrate screen boundaries for cursor movement
        
        Args:
            left (int): Left boundary (pixels)
            right (int): Right boundary (pixels)
            top (int): Top boundary (pixels)
            bottom (int): Bottom boundary (pixels)
        """
        self.settings["screen_boundaries"] = {
            "left": left,
            "right": right,
            "top": top,
            "bottom": bottom
        }
        print(f"Screen boundaries calibrated: {left}, {right}, {top}, {bottom}")
    
    def apply_preset(self, preset_name: str):
        """
        Apply a predefined accessibility preset
        
        Args:
            preset_name (str): Name of preset ('high_precision', 'easy_control', 'minimal_motion')
        """
        presets = {
            "high_precision": {
                "mouse_sensitivity": 1.0,
                "smoothing_factor": 0.7,
                "gesture_debounce": 0.7
            },
            "easy_control": {
                "mouse_sensitivity": 2.0,
                "smoothing_factor": 0.3,
                "gesture_debounce": 0.3
            },
            "minimal_motion": {
                "mouse_sensitivity": 1.2,
                "smoothing_factor": 0.8,
                "gesture_debounce": 0.8
            }
        }
        
        if preset_name in presets:
            self.settings.update(presets[preset_name])
            print(f"Applied preset: {preset_name}")
        else:
            print(f"Preset '{preset_name}' not found")

