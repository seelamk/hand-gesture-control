"""
Configuration Manager for Hand Gesture Control System

This module handles loading and managing configuration settings from config.json.
It provides easy access to all system parameters and allows runtime updates.

Author: Hand Gesture Control Team
Purpose: Assistive technology for users with mobility limitations
"""

import json
import os
from typing import Dict, Any


class Config:
    """
    Configuration manager that loads settings from config.json
    
    This class provides centralized access to all configuration parameters
    including camera settings, hand tracking parameters, mouse control settings,
    and accessibility features.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize configuration manager
        
        Args:
            config_path (str): Path to the configuration JSON file
        """
        self.config_path = config_path
        self.settings = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """
        Load configuration from JSON file
        
        Returns:
            Dict[str, Any]: Configuration dictionary
            
        Raises:
            FileNotFoundError: If config file doesn't exist
            json.JSONDecodeError: If config file is invalid JSON
        """
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Config file '{self.config_path}' not found. Using defaults.")
            return self._get_default_config()
        except json.JSONDecodeError as e:
            print(f"Error parsing config file: {e}. Using defaults.")
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """
        Provide default configuration if file is missing
        
        Returns:
            Dict[str, Any]: Default configuration dictionary
        """
        return {
            "camera": {"device_id": 0, "width": 1280, "height": 720, "fps": 30},
            "hand_tracking": {"max_hands": 1, "min_detection_confidence": 0.7, "min_tracking_confidence": 0.5},
            "mouse_control": {"sensitivity": 1.5, "smoothing_factor": 0.5, "screen_width": 1920, "screen_height": 1080},
            "gestures": {"enabled": True, "debounce_time": 0.5},
            "accessibility": {"visual_feedback": True, "audio_feedback": False, "auto_pause_minutes": 15}
        }
    
    def get(self, key_path: str, default: Any = None) -> Any:
        """
        Get configuration value using dot notation
        
        Args:
            key_path (str): Path to config value (e.g., 'camera.width')
            default (Any): Default value if key not found
            
        Returns:
            Any: Configuration value
            
        Example:
            >>> config = Config()
            >>> width = config.get('camera.width')  # Returns 1280
        """
        keys = key_path.split('.')
        value = self.settings
        
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        
        return value
    
    def save(self):
        """
        Save current configuration to file
        
        This allows runtime changes to be persisted for future sessions.
        """
        try:
            with open(self.config_path, 'w') as f:
                json.dump(self.settings, f, indent=2)
            print(f"Configuration saved to {self.config_path}")
        except Exception as e:
            print(f"Error saving configuration: {e}")
    
    def update(self, key_path: str, value: Any):
        """
        Update configuration value using dot notation
        
        Args:
            key_path (str): Path to config value (e.g., 'camera.width')
            value (Any): New value to set
            
        Example:
            >>> config = Config()
            >>> config.update('mouse_control.sensitivity', 2.0)
        """
        keys = key_path.split('.')
        current = self.settings
        
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        current[keys[-1]] = value


# Global configuration instance
config = Config()

