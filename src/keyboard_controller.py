"""
Keyboard Controller Module

This module handles keyboard input simulation for common shortcuts and actions.
It enables users to perform keyboard operations through hand gestures, making
typing and shortcuts accessible without physical keyboard use.

Features:
- Common keyboard shortcuts (Copy, Paste, Undo, etc.)
- Text input simulation
- Special key presses (Enter, Backspace, Tab, etc.)
- Modifier key combinations (Ctrl, Alt, Shift)
- Application switching and window management

Author: Hand Gesture Control Team
Purpose: Assistive technology for users with mobility limitations
"""

import pyautogui
import time
from typing import List, Optional


class KeyboardController:
    """
    Controls keyboard input and shortcuts
    
    This class provides methods to simulate keyboard input, including
    individual keys, key combinations, and common shortcuts.
    """
    
    def __init__(self, key_press_delay: float = 0.1):
        """
        Initialize keyboard controller
        
        Args:
            key_press_delay (float): Delay between key presses in seconds
        """
        self.key_press_delay = key_press_delay
        self.last_key_time = 0
        self.key_cooldown = 0.5  # Minimum time between same key presses
    
    def press_key(self, key: str):
        """
        Press a single key
        
        Args:
            key (str): Key to press (e.g., 'a', 'enter', 'space')
        """
        current_time = time.time()
        
        if current_time - self.last_key_time >= self.key_press_delay:
            pyautogui.press(key)
            self.last_key_time = current_time
            print(f"Key pressed: {key}")
    
    def press_keys(self, keys: List[str]):
        """
        Press multiple keys in sequence
        
        Args:
            keys (List[str]): List of keys to press
        """
        for key in keys:
            pyautogui.press(key)
            time.sleep(self.key_press_delay)
        print(f"Keys pressed: {', '.join(keys)}")
    
    def hotkey(self, *keys):
        """
        Press a combination of keys simultaneously (hotkey)
        
        Args:
            *keys: Variable number of keys to press together
            
        Example:
            hotkey('ctrl', 'c')  # Copy
            hotkey('ctrl', 'shift', 's')  # Save As
        """
        current_time = time.time()
        
        if current_time - self.last_key_time >= self.key_cooldown:
            pyautogui.hotkey(*keys)
            self.last_key_time = current_time
            print(f"Hotkey pressed: {' + '.join(keys)}")
    
    # Common shortcuts
    def copy(self):
        """Copy selected text (Ctrl+C)"""
        self.hotkey('ctrl', 'c')
    
    def paste(self):
        """Paste from clipboard (Ctrl+V)"""
        self.hotkey('ctrl', 'v')
    
    def cut(self):
        """Cut selected text (Ctrl+X)"""
        self.hotkey('ctrl', 'x')
    
    def undo(self):
        """Undo last action (Ctrl+Z)"""
        self.hotkey('ctrl', 'z')
    
    def redo(self):
        """Redo last undone action (Ctrl+Y)"""
        self.hotkey('ctrl', 'y')
    
    def select_all(self):
        """Select all content (Ctrl+A)"""
        self.hotkey('ctrl', 'a')
    
    def save(self):
        """Save current document (Ctrl+S)"""
        self.hotkey('ctrl', 's')
    
    def find(self):
        """Open find dialog (Ctrl+F)"""
        self.hotkey('ctrl', 'f')
    
    def new_tab(self):
        """Open new tab in browser (Ctrl+T)"""
        self.hotkey('ctrl', 't')
    
    def close_tab(self):
        """Close current tab (Ctrl+W)"""
        self.hotkey('ctrl', 'w')
    
    def switch_window(self):
        """Switch between windows (Alt+Tab)"""
        self.hotkey('alt', 'tab')
    
    def minimize_window(self):
        """Minimize current window (Windows+Down)"""
        self.hotkey('win', 'down')
    
    def maximize_window(self):
        """Maximize current window (Windows+Up)"""
        self.hotkey('win', 'up')
    
    def type_text(self, text: str, interval: float = 0.05):
        """
        Type text character by character
        
        Args:
            text (str): Text to type
            interval (float): Delay between characters
        """
        pyautogui.write(text, interval=interval)
        print(f"Typed: {text}")
    
    def press_enter(self):
        """Press Enter key"""
        self.press_key('enter')
    
    def press_backspace(self):
        """Press Backspace key"""
        self.press_key('backspace')
    
    def press_delete(self):
        """Press Delete key"""
        self.press_key('delete')
    
    def press_tab(self):
        """Press Tab key"""
        self.press_key('tab')
    
    def press_escape(self):
        """Press Escape key"""
        self.press_key('esc')

