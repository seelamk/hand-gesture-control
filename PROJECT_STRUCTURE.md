# Project Structure - Hand Gesture Control System

## 📁 Directory Tree

```
HandGestures/
│
├── 📄 README.md                    # Main project documentation
├── 📄 SETUP_GUIDE.md              # Detailed installation guide
├── 📄 QUICK_REFERENCE.md          # Quick reference for users
├── 📄 ARCHITECTURE.md             # Technical architecture documentation
├── 📄 CONTRIBUTING.md             # Contribution guidelines
├── 📄 LICENSE                     # MIT License
├── 📄 PROJECT_STRUCTURE.md        # This file
│
├── 📄 requirements.txt            # Python dependencies
├── 📄 config.json                 # Configuration settings
├── 📄 test_camera.py              # Camera testing utility
│
├── 📂 src/                        # Source code directory
│   ├── 📄 __init__.py            # Package initialization
│   ├── 📄 main.py                # Main application entry point
│   ├── 📄 hand_tracker.py        # Hand tracking with MediaPipe
│   ├── 📄 gesture_recognizer.py  # Gesture classification
│   ├── 📄 mouse_controller.py    # Mouse control logic
│   ├── 📄 keyboard_controller.py # Keyboard control logic
│   ├── 📄 config.py              # Configuration manager
│   │
│   └── 📂 utils/                 # Utility modules
│       ├── 📄 __init__.py       # Utils package initialization
│       ├── 📄 smoothing.py      # Smoothing algorithms
│       ├── 📄 calibration.py    # User calibration
│       └── 📄 feedback.py       # Visual feedback
│
└── 📂 profiles/                   # User profiles (created at runtime)
    └── 📄 default.json           # Default user profile
```

## 📝 File Descriptions

### Root Level Files

#### Documentation Files
- **README.md** - Main project overview, features, and basic usage
- **SETUP_GUIDE.md** - Step-by-step installation and setup instructions
- **QUICK_REFERENCE.md** - Quick reference guide for gestures and settings
- **ARCHITECTURE.md** - Technical architecture and design decisions
- **CONTRIBUTING.md** - Guidelines for contributing to the project
- **PROJECT_STRUCTURE.md** - This file, explaining project organization

#### Configuration Files
- **requirements.txt** - Python package dependencies
- **config.json** - Runtime configuration (camera, sensitivity, etc.)
- **LICENSE** - MIT License with accessibility statement

#### Utility Scripts
- **test_camera.py** - Standalone script to test camera functionality

### Source Code (`src/`)

#### Core Application
- **main.py** (299 lines)
  - Main application class `HandGestureController`
  - Integration of all components
  - Main event loop
  - User interface handling
  - Entry point: `main()` function

#### Hand Tracking
- **hand_tracker.py** (233 lines)
  - `HandTracker` class
  - MediaPipe integration
  - Hand landmark detection (21 points)
  - Finger state detection
  - Visual landmark rendering

#### Gesture Recognition
- **gesture_recognizer.py** (185 lines)
  - `GestureRecognizer` class
  - `Gesture` enum (7 gestures)
  - Rule-based gesture classification
  - Debouncing logic
  - Distance calculations

#### System Control
- **mouse_controller.py** (213 lines)
  - `MouseController` class
  - Cursor movement with smoothing
  - Click actions (left, right, double)
  - Drag and drop
  - Scrolling functionality

- **keyboard_controller.py** (158 lines)
  - `KeyboardController` class
  - Key press simulation
  - Hotkey combinations
  - Common shortcuts (copy, paste, etc.)

#### Configuration
- **config.py** (127 lines)
  - `Config` class
  - JSON configuration loading
  - Dot notation access
  - Default values
  - Runtime updates

### Utilities (`src/utils/`)

- **smoothing.py** (150+ lines)
  - `ExponentialMovingAverage` class
  - `SimpleMovingAverage` class
  - `OneEuroFilter` class
  - Cursor smoothing algorithms

- **calibration.py** (165 lines)
  - `Calibration` class
  - User profile management
  - Settings persistence
  - Accessibility presets

- **feedback.py** (150 lines)
  - `VisualFeedback` class
  - On-screen overlays
  - Gesture indicators
  - FPS counter
  - Status messages

## 🔄 Data Flow

```
User Hand
    ↓
Camera (OpenCV)
    ↓
hand_tracker.py (MediaPipe)
    ↓
Landmarks (21 points) + Finger States
    ↓
gesture_recognizer.py
    ↓
Gesture Classification
    ↓
main.py (Action Mapping)
    ↓
    ├─→ mouse_controller.py → System Mouse
    └─→ keyboard_controller.py → System Keyboard
```

## 📊 Module Dependencies

```
main.py
├── hand_tracker.py
│   └── mediapipe
│   └── opencv-python
│   └── numpy
├── gesture_recognizer.py
├── mouse_controller.py
│   └── pyautogui
├── keyboard_controller.py
│   └── pyautogui
├── config.py
└── utils/
    ├── smoothing.py
    ├── calibration.py
    └── feedback.py
        └── opencv-python
```

## 🎯 Key Classes and Their Responsibilities

| Class | File | Responsibility | Lines |
|-------|------|----------------|-------|
| `HandTracker` | hand_tracker.py | Hand detection & landmarks | 233 |
| `GestureRecognizer` | gesture_recognizer.py | Gesture classification | 185 |
| `MouseController` | mouse_controller.py | Mouse control | 213 |
| `KeyboardController` | keyboard_controller.py | Keyboard control | 158 |
| `Config` | config.py | Configuration management | 127 |
| `Calibration` | calibration.py | User calibration | 165 |
| `VisualFeedback` | feedback.py | Visual overlays | 150 |
| `HandGestureController` | main.py | Main application | 299 |

## 📈 Code Statistics

- **Total Python Files:** 12
- **Total Lines of Code:** ~2,000+
- **Documentation Files:** 6
- **Configuration Files:** 2
- **Test Scripts:** 1

## 🔧 Configuration Hierarchy

```
config.json (User settings)
    ↓
config.py (Config manager)
    ↓
main.py (Application)
    ↓
Individual modules (Use config values)
```

## 🎨 Design Patterns Used

1. **Singleton Pattern** - Config instance
2. **Strategy Pattern** - Smoothing algorithms
3. **Observer Pattern** - Gesture state changes
4. **Factory Pattern** - Gesture creation
5. **Facade Pattern** - Main application class

## 📦 External Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| mediapipe | Hand tracking | ≥0.10.0 |
| opencv-python | Camera & image processing | ≥4.8.0 |
| numpy | Numerical operations | ≥1.24.0 |
| pyautogui | System control | ≥0.9.54 |
| pynput | Advanced input control | ≥1.7.6 |
| Pillow | Image handling | ≥10.0.0 |

## 🚀 Execution Flow

1. **Startup** (`main.py`)
   - Load configuration
   - Initialize camera
   - Initialize all controllers
   - Display startup messages

2. **Main Loop** (`main.py::run()`)
   - Capture frame
   - Process hand tracking
   - Recognize gesture
   - Execute action
   - Display feedback
   - Handle keyboard input

3. **Shutdown** (`main.py::cleanup()`)
   - Release camera
   - Close windows
   - Save settings

## 📚 Learning Path Through Code

### Beginner
1. Start with `test_camera.py` - Simple camera access
2. Read `config.py` - Configuration management
3. Explore `feedback.py` - Visual overlays

### Intermediate
4. Study `hand_tracker.py` - MediaPipe integration
5. Understand `gesture_recognizer.py` - Classification logic
6. Review `mouse_controller.py` - System control

### Advanced
7. Analyze `main.py` - Full integration
8. Explore `utils/smoothing.py` - Algorithms
9. Study `calibration.py` - User customization

---

This structure is designed to be:
- **Modular** - Each component has a single responsibility
- **Documented** - Every file is extensively commented
- **Extensible** - Easy to add new features
- **Educational** - Clear code for learning
- **Accessible** - Focused on user needs

