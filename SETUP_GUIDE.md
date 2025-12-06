# Setup Guide - Hand Gesture Control System

This guide will walk you through setting up the Hand Gesture Control System step by step.

## Prerequisites Check

Before starting, ensure you have:
- [ ] A working webcam (built-in or external)
- [ ] Python 3.8 or higher installed
- [ ] Administrator/sudo privileges on your computer
- [ ] At least 2GB of free disk space
- [ ] Good lighting in your workspace

## Step-by-Step Installation

### 1. Verify Python Installation

Open a terminal/command prompt and run:

```bash
python --version
# or
python3 --version
```

You should see Python 3.8 or higher. If not, download from [python.org](https://www.python.org/downloads/).

### 2. Download the Project

```bash
# If using git
git clone <repository-url>
cd HandGestures

# Or download and extract the ZIP file
```

### 3. Create a Virtual Environment

**Why?** This keeps project dependencies isolated from your system Python.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- MediaPipe (hand tracking)
- OpenCV (camera and image processing)
- PyAutoGUI (mouse/keyboard control)
- NumPy (numerical operations)
- Pillow (image handling)

**Note:** Installation may take 5-10 minutes depending on your internet speed.

### 5. Test Camera Access

Run this quick test:

```python
python -c "import cv2; cap = cv2.VideoCapture(0); print('Camera OK' if cap.isOpened() else 'Camera Error'); cap.release()"
```

If you see "Camera OK", you're ready to proceed!

### 6. Configure Settings (Optional)

Edit `config.json` to customize:

```json
{
  "camera": {
    "device_id": 0,          // Change if you have multiple cameras
    "width": 1280,
    "height": 720
  },
  "mouse_control": {
    "sensitivity": 1.5,      // Adjust cursor speed
    "smoothing_factor": 0.5  // Adjust cursor smoothness
  }
}
```

### 7. First Run

```bash
python src/main.py
```

You should see:
1. Initialization messages
2. A window showing your camera feed
3. Hand landmarks when you show your hand

## Initial Calibration

### Finding the Right Distance
1. Sit 1.5 to 2 feet (45-60 cm) from the camera
2. Position your hand so it's clearly visible
3. Your hand should take up about 1/4 of the screen

### Testing Gestures

Try each gesture in order:

1. **POINT** (Index finger extended)
   - Move your hand slowly
   - Watch the cursor follow
   - If too fast/slow, adjust sensitivity

2. **PINCH** (Thumb + index together)
   - Bring thumb and index fingertips together
   - Should trigger a click
   - Release to stop

3. **PEACE** (V sign)
   - Extend index and middle fingers
   - Should trigger right-click

4. **PALM** (Open hand)
   - Extend all fingers
   - Should pause/resume the system

### Adjusting Sensitivity

If cursor movement feels wrong:

**Too Fast:**
- Decrease `sensitivity` to 1.0 or 0.8
- Increase `smoothing_factor` to 0.7

**Too Slow:**
- Increase `sensitivity` to 2.0 or 2.5
- Decrease `smoothing_factor` to 0.3

**Too Jittery:**
- Increase `smoothing_factor` to 0.8
- Keep sensitivity moderate (1.5)

## Common Setup Issues

### Issue: "No module named 'cv2'"
**Solution:**
```bash
pip install opencv-python
```

### Issue: "Camera not found"
**Solutions:**
1. Check if another app is using the camera
2. Try different `device_id` values (0, 1, 2)
3. Grant camera permissions to Python

### Issue: "Permission denied" on Linux
**Solution:**
```bash
sudo usermod -a -G video $USER
# Then log out and log back in
```

### Issue: Hand not detected
**Solutions:**
1. Improve lighting (face a window or lamp)
2. Ensure hand is in frame
3. Lower `min_detection_confidence` to 0.5
4. Check camera focus

### Issue: Gestures not recognized
**Solutions:**
1. Make gestures more distinct
2. Hold gesture for 1 second
3. Increase `debounce_time` to 0.7
4. Check finger states are correct

## Performance Optimization

### For Slower Computers:
```json
{
  "camera": {
    "width": 640,
    "height": 480,
    "fps": 24
  },
  "hand_tracking": {
    "min_detection_confidence": 0.5
  }
}
```

### For Better Accuracy:
```json
{
  "camera": {
    "width": 1920,
    "height": 1080
  },
  "hand_tracking": {
    "min_detection_confidence": 0.8,
    "min_tracking_confidence": 0.7
  }
}
```

## Next Steps

Once setup is complete:
1. Practice each gesture until comfortable
2. Adjust settings to your preference
3. Try using it for simple tasks (browsing, clicking)
4. Take breaks every 15 minutes
5. Gradually increase usage time

## Getting Help

If you encounter issues:
1. Check this guide's troubleshooting section
2. Review error messages carefully
3. Check the main README.md
4. Look at code comments in the source files

## Accessibility Tips

- **For limited mobility:** Increase sensitivity, reduce required movement
- **For tremors:** Increase smoothing, use larger gestures
- **For fatigue:** Enable auto-pause, use one-handed mode
- **For vision impairment:** Enable audio feedback (future feature)

---

**Congratulations!** You're now ready to use the Hand Gesture Control System.

Remember: This is assistive technology. Take your time, adjust settings to your comfort, and take regular breaks.

