# Hand Gesture Control System 🤲

An assistive technology project that enables users to control their computer using hand gestures captured through a webcam. This system is designed to help people with disabilities, chronic pain, RSI, or mobility limitations interact with their computer without traditional mouse and keyboard input.

## 🎯 Purpose

This project aims to make computer interaction accessible to:
- People with mobility impairments
- Users with repetitive strain injuries (RSI)
- Individuals recovering from injuries
- People with chronic pain conditions
- Anyone who needs hands-free computer control

## ✨ Features

### Core Functionality
- **Real-time Hand Tracking**: Uses Google's MediaPipe for accurate 21-point hand landmark detection
- **Gesture Recognition**: Recognizes 7+ distinct hand gestures
- **Mouse Control**: Smooth cursor movement, clicking, and scrolling
- **Keyboard Shortcuts**: Common shortcuts accessible through gestures
- **Visual Feedback**: On-screen indicators showing current gesture and system status

### Accessibility Features
- Adjustable sensitivity and smoothing
- Customizable gesture mappings
- User calibration and profiles
- Visual feedback with high contrast options
- Pause/resume functionality for rest breaks
- Mirror mode for natural interaction

## 🎮 Supported Gestures

| Gesture | Action | Description |
|---------|--------|-------------|
| **POINT** | Move Cursor | Index finger extended, others folded |
| **PINCH** | Left Click | Thumb and index finger close together |
| **PEACE** | Right Click | Index and middle fingers extended (V sign) |
| **PALM** | Pause/Resume | All fingers extended (open hand) |
| **FIST** | Scroll Mode | All fingers closed |
| **THUMB UP** | Scroll Up | Only thumb extended upward |
| **THUMB DOWN** | Scroll Down | Only thumb extended downward |

## 🛠️ Technology Stack

- **Python 3.8+**: Core programming language
- **MediaPipe**: Hand tracking and landmark detection
- **OpenCV**: Camera input and image processing
- **PyAutoGUI**: Mouse and keyboard control
- **NumPy**: Numerical computations

## 📋 Requirements

### Hardware
- Webcam (720p minimum, 1080p recommended)
- Processor: Intel i5/AMD Ryzen 5 or better
- RAM: 4GB minimum (8GB recommended)
- Operating System: Windows 10/11, macOS, or Linux

### Software
- Python 3.8 or higher
- Webcam drivers
- Administrator privileges (for system control features)

## 🚀 Installation

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd HandGestures
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 🎬 Usage

### Basic Usage
```bash
python src/main.py
```

### Keyboard Controls
- **ESC**: Exit the application
- **P**: Pause/Resume gesture control
- **L**: Toggle landmark display
- **H**: Show help menu

### First Time Setup
1. Position yourself 1-2 feet from the webcam
2. Ensure good lighting (face the light source)
3. Start with the POINT gesture to test cursor movement
4. Adjust sensitivity in `config.json` if needed

## ⚙️ Configuration

Edit `config.json` to customize settings:

```json
{
  "mouse_control": {
    "sensitivity": 1.5,        // Higher = faster cursor
    "smoothing_factor": 0.5    // Higher = smoother but slower
  },
  "gestures": {
    "debounce_time": 0.5       // Minimum time between gesture changes
  }
}
```

## 📁 Project Structure

```
HandGestures/
├── src/
│   ├── main.py                  # Main application entry point
│   ├── hand_tracker.py          # MediaPipe hand detection
│   ├── gesture_recognizer.py    # Gesture classification
│   ├── mouse_controller.py      # Mouse control logic
│   ├── keyboard_controller.py   # Keyboard control logic
│   ├── config.py                # Configuration manager
│   └── utils/
│       ├── calibration.py       # User calibration
│       ├── smoothing.py         # Cursor smoothing algorithms
│       └── feedback.py          # Visual feedback
├── config.json                  # Configuration file
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🧪 Testing

To test the system:
1. Run the application
2. Try each gesture individually
3. Adjust sensitivity if cursor is too fast/slow
4. Use pause (PALM gesture) to take breaks

## 🔧 Troubleshooting

### Camera Not Detected
- Check if camera is connected and working
- Try changing `device_id` in `config.json` (0, 1, 2, etc.)
- Ensure no other application is using the camera

### Gestures Not Recognized
- Ensure good lighting conditions
- Keep hand within camera frame
- Adjust `min_detection_confidence` in config
- Try recalibrating with different sensitivity

### Cursor Too Jittery
- Increase `smoothing_factor` in config (0.7-0.9)
- Reduce `sensitivity` value
- Ensure stable hand position

### Cursor Too Slow
- Decrease `smoothing_factor` (0.2-0.4)
- Increase `sensitivity` value

## 🎓 Learning from the Code

This project is extensively documented to help others learn. Each file includes:

### Documentation Features
- **Detailed docstrings**: Every class and function has comprehensive documentation
- **Inline comments**: Complex logic is explained step-by-step
- **Type hints**: Function parameters and return types are clearly specified
- **Usage examples**: Docstrings include example usage where applicable

### Key Learning Areas

#### 1. Computer Vision (`hand_tracker.py`)
Learn how to:
- Use MediaPipe for hand detection
- Process video frames in real-time
- Extract and normalize landmark coordinates
- Determine finger states (extended/folded)

#### 2. Gesture Recognition (`gesture_recognizer.py`)
Learn how to:
- Classify gestures from landmark data
- Calculate distances between points
- Implement debouncing to prevent false triggers
- Use enums for clean gesture representation

#### 3. System Control (`mouse_controller.py`, `keyboard_controller.py`)
Learn how to:
- Control mouse cursor programmatically
- Implement cursor smoothing algorithms
- Simulate mouse clicks and scrolling
- Trigger keyboard shortcuts

#### 4. Configuration Management (`config.py`)
Learn how to:
- Load and parse JSON configuration files
- Implement dot notation for nested settings
- Provide default values and error handling
- Save runtime changes to disk

#### 5. Utility Patterns (`utils/`)
Learn how to:
- Implement smoothing algorithms (EMA, SMA)
- Create user calibration systems
- Build visual feedback overlays
- Manage user profiles

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional gesture recognition
- Voice feedback integration
- Multi-hand support
- Custom gesture training
- Mobile device support
- Accessibility enhancements

## 📝 Code Examples

### Using the Hand Tracker
```python
from hand_tracker import HandTracker

tracker = HandTracker(max_hands=1, min_detection_confidence=0.7)
success, frame = camera.read()

if tracker.process_frame(frame):
    landmarks = tracker.get_hand_landmarks(0)
    finger_states = tracker.get_finger_states(0)
    print(f"Fingers up: {sum(finger_states.values())}")
```

### Recognizing Gestures
```python
from gesture_recognizer import GestureRecognizer

recognizer = GestureRecognizer(debounce_time=0.5)
gesture = recognizer.recognize_gesture(landmarks, finger_states)
print(f"Current gesture: {gesture.value}")
```

### Controlling the Mouse
```python
from mouse_controller import MouseController

mouse = MouseController(sensitivity=1.5, smoothing_factor=0.5)
mouse.move_cursor(hand_x, hand_y, frame_width, frame_height)
mouse.left_click()
```

## 🔒 Safety Features

- **FailSafe**: Move mouse to screen corner to abort (PyAutoGUI feature)
- **Cooldown timers**: Prevent accidental rapid clicks
- **Pause functionality**: Easy way to rest without exiting
- **Boundary checking**: Cursor stays within screen limits

## 🌟 Future Enhancements

- [ ] Custom gesture training with machine learning
- [ ] Voice command integration
- [ ] Eye tracking support
- [ ] Multi-monitor support
- [ ] Gesture macros and automation
- [ ] Mobile app for remote control
- [ ] Accessibility presets for specific conditions
- [ ] Session analytics and usage tracking

## 📄 License

This project is created for educational and assistive technology purposes.

## 🙏 Acknowledgments

- **MediaPipe Team**: For the excellent hand tracking solution
- **OpenCV Community**: For computer vision tools
- **Accessibility Advocates**: For inspiring this project

## 📧 Support

For issues, questions, or suggestions:
1. Check the troubleshooting section
2. Review the code documentation
3. Open an issue on the repository

---

**Made with ❤️ to make technology accessible to everyone**

*This project demonstrates how computer vision and gesture recognition can create
assistive technologies that empower people with disabilities to interact with
computers in new and accessible ways.*