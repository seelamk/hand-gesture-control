"""
Camera Test Script

This script tests if your camera is working properly before running the main application.
It's a simple diagnostic tool to ensure camera access is available.

Usage:
    python test_camera.py

Author: Hand Gesture Control Team
"""

import cv2
import sys


def test_camera():
    """
    Test camera access and display video feed
    
    This function attempts to open the default camera and display the feed.
    Press 'q' to quit the test.
    """
    print("=" * 60)
    print("Camera Test - Hand Gesture Control System")
    print("=" * 60)
    print("\nAttempting to open camera...")
    
    # Try to open camera
    camera = cv2.VideoCapture(0)
    
    if not camera.isOpened():
        print("❌ ERROR: Could not open camera!")
        print("\nTroubleshooting:")
        print("1. Check if camera is connected")
        print("2. Close other applications using the camera")
        print("3. Try different device_id in config.json (0, 1, 2)")
        print("4. Check camera permissions")
        return False
    
    print("✓ Camera opened successfully!")
    
    # Get camera properties
    width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = camera.get(cv2.CAP_PROP_FPS)
    
    print(f"\nCamera Properties:")
    print(f"  Resolution: {int(width)}x{int(height)}")
    print(f"  FPS: {int(fps)}")
    print("\nDisplaying camera feed...")
    print("Press 'q' to quit the test")
    print("=" * 60)
    
    frame_count = 0
    
    try:
        while True:
            # Read frame
            success, frame = camera.read()
            
            if not success:
                print("❌ ERROR: Failed to read frame from camera")
                break
            
            frame_count += 1
            
            # Flip frame for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Add text overlay
            cv2.putText(frame, "Camera Test - Press 'q' to quit", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.7, (0, 255, 0), 2)
            
            cv2.putText(frame, f"Frame: {frame_count}", 
                       (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 
                       0.6, (0, 255, 0), 2)
            
            # Display frame
            cv2.imshow('Camera Test', frame)
            
            # Check for 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("\nTest completed successfully!")
                break
    
    except KeyboardInterrupt:
        print("\nTest interrupted by user")
    
    finally:
        # Cleanup
        camera.release()
        cv2.destroyAllWindows()
        print(f"\nTotal frames captured: {frame_count}")
        print("Camera test finished.")
    
    return True


def main():
    """Main entry point"""
    success = test_camera()
    
    if success:
        print("\n" + "=" * 60)
        print("✓ Camera is working properly!")
        print("You can now run the main application:")
        print("  python src/main.py")
        print("=" * 60)
        sys.exit(0)
    else:
        print("\n" + "=" * 60)
        print("❌ Camera test failed")
        print("Please fix camera issues before running the main application")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    main()

