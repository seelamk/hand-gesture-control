"""
Hand Gesture Control System - Main Application

This is the main entry point for the assistive technology system that enables
users to control their computer using hand gestures captured through a webcam.

The system integrates:
- Hand tracking using MediaPipe
- Gesture recognition
- Mouse and keyboard control
- Visual feedback
- User calibration

Usage:
    python main.py

Controls:
    - ESC: Exit the application
    - P: Pause/Resume gesture control
    - C: Open calibration menu
    - S: Save current settings

Author: Hand Gesture Control Team
Purpose: Assistive technology for users with mobility limitations
"""

import cv2
import time
import sys
import os

# Add src directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hand_tracker import HandTracker
from gesture_recognizer import GestureRecognizer, Gesture
from mouse_controller import MouseController
from keyboard_controller import KeyboardController
from config import config
from utils.feedback import VisualFeedback
from utils.calibration import Calibration


class HandGestureController:
    """
    Main application class that integrates all components
    
    This class manages the camera feed, hand tracking, gesture recognition,
    and control actions.
    """
    
    def __init__(self):
        """Initialize the hand gesture control system"""
        print("=" * 60)
        print("Hand Gesture Control System - Assistive Technology")
        print("=" * 60)
        print("\nInitializing components...")
        
        # Load configuration
        self.config = config
        
        # Initialize camera
        camera_id = self.config.get('camera.device_id', 0)
        self.camera = cv2.VideoCapture(camera_id)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.config.get('camera.width', 1280))
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.config.get('camera.height', 720))
        
        if not self.camera.isOpened():
            print("Error: Could not open camera")
            sys.exit(1)
        
        print("✓ Camera initialized")
        
        # Initialize hand tracker
        self.hand_tracker = HandTracker(
            max_hands=self.config.get('hand_tracking.max_hands', 1),
            min_detection_confidence=self.config.get('hand_tracking.min_detection_confidence', 0.7),
            min_tracking_confidence=self.config.get('hand_tracking.min_tracking_confidence', 0.5)
        )
        print("✓ Hand tracker initialized")
        
        # Initialize gesture recognizer
        self.gesture_recognizer = GestureRecognizer(
            debounce_time=self.config.get('gestures.debounce_time', 0.5)
        )
        print("✓ Gesture recognizer initialized")
        
        # Initialize mouse controller
        self.mouse_controller = MouseController(
            sensitivity=self.config.get('mouse_control.sensitivity', 1.5),
            smoothing_factor=self.config.get('mouse_control.smoothing_factor', 0.5)
        )
        print("✓ Mouse controller initialized")
        
        # Initialize keyboard controller
        self.keyboard_controller = KeyboardController()
        print("✓ Keyboard controller initialized")
        
        # Initialize visual feedback
        self.visual_feedback = VisualFeedback(
            show_fps=True,
            show_gesture=self.config.get('accessibility.visual_feedback', True)
        )
        print("✓ Visual feedback initialized")
        
        # Initialize calibration
        self.calibration = Calibration()
        print("✓ Calibration loaded")
        
        # System state
        self.is_paused = False
        self.show_landmarks = self.config.get('accessibility.show_landmarks', True)
        self.prev_gesture = Gesture.NONE
        
        # FPS calculation
        self.fps_time = time.time()
        self.fps = 0
        
        print("\n" + "=" * 60)
        print("System ready! Starting gesture control...")
        print("=" * 60)
        print("\nControls:")
        print("  ESC - Exit application")
        print("  P   - Pause/Resume")
        print("  L   - Toggle landmark display")
        print("  H   - Show help")
        print("\nGestures:")
        print("  POINT - Move cursor")
        print("  PINCH - Left click")
        print("  PEACE - Right click")
        print("  PALM  - Pause control")
        print("  FIST  - Scroll mode")
        print("  THUMB UP/DOWN - Scroll up/down")
        print("=" * 60 + "\n")

    def process_gesture_action(self, gesture: Gesture, landmarks):
        """
        Process gesture and perform corresponding action

        Args:
            gesture (Gesture): Recognized gesture
            landmarks: Hand landmarks
        """
        # Get index finger tip position for cursor control
        index_tip = landmarks[8] if landmarks else None

        if gesture == Gesture.POINT and index_tip:
            # Move cursor with index finger
            self.mouse_controller.move_cursor(
                index_tip[0], index_tip[1],
                self.camera.get(cv2.CAP_PROP_FRAME_WIDTH),
                self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
            )

        elif gesture == Gesture.PINCH:
            # Left click on pinch
            if self.prev_gesture != Gesture.PINCH:
                self.mouse_controller.left_click()

        elif gesture == Gesture.PEACE:
            # Right click on peace sign
            if self.prev_gesture != Gesture.PEACE:
                self.mouse_controller.right_click()

        elif gesture == Gesture.PALM:
            # Pause on open palm
            if self.prev_gesture != Gesture.PALM:
                self.is_paused = not self.is_paused
                print(f"Control {'PAUSED' if self.is_paused else 'RESUMED'}")

        elif gesture == Gesture.THUMB_UP:
            # Scroll up
            self.mouse_controller.scroll('up', 3)

        elif gesture == Gesture.THUMB_DOWN:
            # Scroll down
            self.mouse_controller.scroll('down', 3)

        self.prev_gesture = gesture

    def run(self):
        """
        Main application loop
        """
        try:
            while True:
                # Read frame from camera
                success, frame = self.camera.read()

                if not success:
                    print("Error: Failed to read from camera")
                    break

                # Flip frame horizontally for mirror effect
                frame = cv2.flip(frame, 1)

                # Calculate FPS
                current_time = time.time()
                self.fps = 1 / (current_time - self.fps_time) if (current_time - self.fps_time) > 0 else 0
                self.fps_time = current_time

                # Process hand tracking
                hand_detected = self.hand_tracker.process_frame(frame)

                if hand_detected and not self.is_paused:
                    # Get hand landmarks
                    landmarks = self.hand_tracker.get_hand_landmarks(0)
                    finger_states = self.hand_tracker.get_finger_states(0)

                    if landmarks and finger_states:
                        # Recognize gesture
                        gesture = self.gesture_recognizer.recognize_gesture(landmarks, finger_states)

                        # Process gesture action
                        self.process_gesture_action(gesture, landmarks)

                        # Draw gesture indicator
                        self.visual_feedback.draw_gesture_indicator(
                            frame,
                            self.gesture_recognizer.get_gesture_name()
                        )

                        # Draw hand landmarks if enabled
                        if self.show_landmarks:
                            frame = self.hand_tracker.draw_landmarks(frame, 0)

                        # Draw cursor indicator at index finger tip
                        index_pos = self.hand_tracker.get_landmark_position(8, 0)
                        if index_pos:
                            self.visual_feedback.draw_cursor_indicator(frame, index_pos)

                # Draw FPS
                self.visual_feedback.draw_fps(frame, self.fps)

                # Draw pause indicator
                if self.is_paused:
                    self.visual_feedback.draw_status_message(frame, "PAUSED")

                # Display frame
                cv2.imshow('Hand Gesture Control', frame)

                # Handle keyboard input
                key = cv2.waitKey(1) & 0xFF

                if key == 27:  # ESC
                    print("\nExiting...")
                    break
                elif key == ord('p') or key == ord('P'):
                    self.is_paused = not self.is_paused
                    print(f"Control {'PAUSED' if self.is_paused else 'RESUMED'}")
                elif key == ord('l') or key == ord('L'):
                    self.show_landmarks = not self.show_landmarks
                    print(f"Landmarks {'SHOWN' if self.show_landmarks else 'HIDDEN'}")
                elif key == ord('h') or key == ord('H'):
                    self.print_help()

        except KeyboardInterrupt:
            print("\nInterrupted by user")

        finally:
            self.cleanup()

    def print_help(self):
        """Print help information"""
        print("\n" + "=" * 60)
        print("HELP - Hand Gesture Control System")
        print("=" * 60)
        print("\nKeyboard Controls:")
        print("  ESC - Exit application")
        print("  P   - Pause/Resume gesture control")
        print("  L   - Toggle landmark display")
        print("  H   - Show this help")
        print("\nGesture Controls:")
        print("  POINT       - Move cursor (index finger extended)")
        print("  PINCH       - Left click (thumb + index together)")
        print("  PEACE       - Right click (index + middle extended)")
        print("  PALM        - Pause/Resume (all fingers extended)")
        print("  FIST        - Scroll mode (all fingers closed)")
        print("  THUMB UP    - Scroll up")
        print("  THUMB DOWN  - Scroll down")
        print("=" * 60 + "\n")

    def cleanup(self):
        """Clean up resources"""
        print("\nCleaning up...")
        self.camera.release()
        cv2.destroyAllWindows()
        self.hand_tracker.release()
        print("Cleanup complete. Goodbye!")


def main():
    """Main entry point"""
    app = HandGestureController()
    app.run()


if __name__ == "__main__":
    main()

