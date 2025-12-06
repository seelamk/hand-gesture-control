# Quick Reference Guide - Hand Gesture Control System

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Test camera
python test_camera.py

# 3. Run application
python src/main.py
```

## 🎮 Gesture Cheat Sheet

| Gesture | Hand Position | Action | Visual |
|---------|---------------|--------|--------|
| **POINT** | ☝️ Index up, others down | Move cursor | Green indicator |
| **PINCH** | 🤏 Thumb + index together | Left click | Blue indicator |
| **PEACE** | ✌️ Index + middle up | Right click | Yellow indicator |
| **PALM** | ✋ All fingers extended | Pause/Resume | Red indicator |
| **FIST** | ✊ All fingers closed | Scroll mode | White indicator |
| **THUMB UP** | 👍 Thumb up | Scroll up | Green indicator |
| **THUMB DOWN** | 👎 Thumb down | Scroll down | Red indicator |

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `ESC` | Exit application |
| `P` | Pause/Resume control |
| `L` | Toggle landmark display |
| `H` | Show help menu |

## ⚙️ Common Settings

### Cursor Too Fast
```json
{
  "mouse_control": {
    "sensitivity": 1.0,
    "smoothing_factor": 0.7
  }
}
```

### Cursor Too Slow
```json
{
  "mouse_control": {
    "sensitivity": 2.5,
    "smoothing_factor": 0.3
  }
}
```

### Cursor Too Jittery
```json
{
  "mouse_control": {
    "sensitivity": 1.5,
    "smoothing_factor": 0.8
  }
}
```

### Gestures Too Sensitive
```json
{
  "gestures": {
    "debounce_time": 0.8
  }
}
```

## 🎯 Optimal Setup

### Camera Position
- **Distance:** 1.5 - 2 feet (45-60 cm)
- **Height:** Eye level or slightly below
- **Angle:** Facing you directly

### Lighting
- **Best:** Natural light from front/side
- **Avoid:** Backlight (window behind you)
- **Tip:** Face a window or lamp

### Hand Position
- **Size:** Hand should fill ~25% of screen
- **Clarity:** All fingers clearly visible
- **Background:** Plain background works best

## 🔧 Troubleshooting Quick Fixes

### Camera Not Working
```bash
# Try different camera ID
# In config.json, change:
"device_id": 1  # or 2, 3, etc.
```

### Hand Not Detected
1. Improve lighting
2. Move closer to camera
3. Lower detection confidence:
```json
"min_detection_confidence": 0.5
```

### Gestures Not Recognized
1. Make gestures more distinct
2. Hold gesture for 1 second
3. Check finger positions are clear

### Low FPS
1. Reduce resolution:
```json
"camera": {
  "width": 640,
  "height": 480
}
```

## 📊 Performance Targets

| Metric | Target | Minimum |
|--------|--------|---------|
| FPS | 30+ | 20 |
| Latency | <50ms | <100ms |
| Detection Accuracy | 95%+ | 85% |
| CPU Usage | <30% | <50% |

## 🎓 Learning Path

### Beginner (Day 1)
1. Install and run
2. Test POINT gesture
3. Practice cursor movement
4. Try PINCH for clicking

### Intermediate (Week 1)
1. Master all 7 gestures
2. Adjust sensitivity
3. Use for simple tasks
4. Customize settings

### Advanced (Month 1)
1. Create custom profiles
2. Use for daily tasks
3. Optimize for your needs
4. Contribute improvements

## 📝 Code Examples

### Using Hand Tracker
```python
from hand_tracker import HandTracker

tracker = HandTracker()
success, frame = camera.read()

if tracker.process_frame(frame):
    landmarks = tracker.get_hand_landmarks(0)
    print(f"Hand detected with {len(landmarks)} points")
```

### Recognizing Gestures
```python
from gesture_recognizer import GestureRecognizer, Gesture

recognizer = GestureRecognizer()
gesture = recognizer.recognize_gesture(landmarks, finger_states)

if gesture == Gesture.PINCH:
    print("Pinch detected!")
```

### Controlling Mouse
```python
from mouse_controller import MouseController

mouse = MouseController()
mouse.move_cursor(0.5, 0.5, 1280, 720)  # Center of screen
mouse.left_click()
```

## 🔍 File Locations

| File | Purpose |
|------|---------|
| `config.json` | Main settings |
| `src/main.py` | Run this to start |
| `test_camera.py` | Test camera |
| `profiles/` | User profiles |
| `README.md` | Full documentation |

## 🆘 Getting Help

1. **Check documentation**
   - README.md - Overview
   - SETUP_GUIDE.md - Installation
   - ARCHITECTURE.md - Technical details

2. **Common issues**
   - See troubleshooting section above
   - Check error messages

3. **Still stuck?**
   - Review code comments
   - Check configuration
   - Open an issue

## 💡 Pro Tips

1. **Take breaks** - Use PALM gesture to pause every 15 minutes
2. **Start slow** - Practice each gesture individually first
3. **Adjust settings** - Everyone's needs are different
4. **Good lighting** - Makes huge difference in accuracy
5. **Stable position** - Keep camera and seating position consistent

## 🎯 Daily Usage Workflow

```
1. Start application
   └─> python src/main.py

2. Position hand in frame
   └─> Check landmarks appear

3. Test POINT gesture
   └─> Verify cursor moves smoothly

4. Use for tasks
   └─> Browse, click, scroll

5. Take breaks
   └─> PALM gesture to pause

6. Exit when done
   └─> Press ESC
```

## 📈 Optimization Checklist

- [ ] Camera at correct distance
- [ ] Good lighting setup
- [ ] Sensitivity adjusted
- [ ] Smoothing configured
- [ ] Gestures practiced
- [ ] Breaks scheduled
- [ ] Settings saved

---

**Keep this guide handy for quick reference!**

For detailed information, see the full documentation in README.md and other guides.

