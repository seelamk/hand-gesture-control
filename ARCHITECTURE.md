# System Architecture - Hand Gesture Control System

This document explains the technical architecture and design decisions of the Hand Gesture Control System.

## Overview

The system follows a modular architecture with clear separation of concerns:

```
┌─────────────────────────────────────────────────────────────┐
│                     Main Application                         │
│                      (main.py)                               │
└──────────────┬──────────────────────────────────────────────┘
               │
       ┌───────┴────────┐
       │                │
┌──────▼──────┐  ┌──────▼──────────┐
│   Camera    │  │  Configuration  │
│   Input     │  │    Manager      │
└──────┬──────┘  └─────────────────┘
       │
┌──────▼──────────────────────────────────────────────────────┐
│              Hand Tracker (MediaPipe)                        │
│  - Detects hands in video frames                            │
│  - Extracts 21 landmark points per hand                     │
│  - Determines finger states (up/down)                       │
└──────┬──────────────────────────────────────────────────────┘
       │
┌──────▼──────────────────────────────────────────────────────┐
│           Gesture Recognizer                                 │
│  - Analyzes landmarks and finger states                     │
│  - Classifies gestures (Point, Pinch, Peace, etc.)         │
│  - Implements debouncing logic                              │
└──────┬──────────────────────────────────────────────────────┘
       │
       ├─────────────────┬────────────────────┐
       │                 │                    │
┌──────▼──────┐  ┌───────▼────────┐  ┌───────▼────────┐
│   Mouse     │  │   Keyboard     │  │    Visual      │
│ Controller  │  │  Controller    │  │   Feedback     │
└─────────────┘  └────────────────┘  └────────────────┘
       │                 │                    │
       └─────────────────┴────────────────────┘
                         │
                ┌────────▼────────┐
                │  System Output  │
                │ (Mouse/Keyboard)│
                └─────────────────┘
```

## Core Components

### 1. Hand Tracker (`hand_tracker.py`)

**Purpose:** Interface with MediaPipe for hand detection and landmark extraction.

**Key Responsibilities:**
- Initialize MediaPipe Hands solution
- Process video frames to detect hands
- Extract 21 landmark points (x, y, z coordinates)
- Determine finger states (extended/folded)
- Draw visual landmarks on frames

**Design Decisions:**
- Uses MediaPipe's pre-trained models (no custom training needed)
- Normalizes coordinates (0-1 range) for screen-independent processing
- Provides both normalized and pixel coordinates
- Implements finger state detection using geometric analysis

**Key Methods:**
```python
process_frame(frame)           # Detect hands in frame
get_hand_landmarks(index)      # Get all 21 landmarks
get_landmark_position(id)      # Get specific landmark in pixels
get_finger_states()            # Determine which fingers are up
draw_landmarks(frame)          # Visualize hand skeleton
```

### 2. Gesture Recognizer (`gesture_recognizer.py`)

**Purpose:** Classify hand poses into meaningful gestures.

**Key Responsibilities:**
- Analyze landmark positions and finger states
- Calculate distances between key points (e.g., thumb-index for pinch)
- Classify gestures using rule-based logic
- Implement debouncing to prevent rapid switching
- Track gesture duration

**Design Decisions:**
- Uses rule-based classification (fast, no training required)
- Implements debouncing with configurable time threshold
- Uses Enum for type-safe gesture representation
- Calculates 3D Euclidean distance for pinch detection

**Gesture Detection Logic:**
```
PINCH:  distance(thumb_tip, index_tip) < 0.05
PALM:   all 5 fingers extended
FIST:   0 or 1 finger extended
POINT:  only index finger extended
PEACE:  index + middle extended, others down
THUMB_UP/DOWN: only thumb extended, check y-position
```

### 3. Mouse Controller (`mouse_controller.py`)

**Purpose:** Translate hand positions to mouse movements and clicks.

**Key Responsibilities:**
- Convert normalized hand coordinates to screen coordinates
- Implement cursor smoothing (Exponential Moving Average)
- Perform mouse clicks (left, right, double)
- Handle drag-and-drop operations
- Implement scrolling

**Design Decisions:**
- Uses PyAutoGUI for cross-platform compatibility
- Implements EMA smoothing to reduce jitter
- Includes cooldown timers to prevent accidental clicks
- Mirrors x-axis for natural interaction
- Clamps cursor to screen boundaries

**Smoothing Algorithm:**
```python
# Exponential Moving Average
new_x = smoothing * prev_x + (1 - smoothing) * current_x
```

### 4. Keyboard Controller (`keyboard_controller.py`)

**Purpose:** Simulate keyboard input and shortcuts.

**Key Responsibilities:**
- Press individual keys
- Execute key combinations (hotkeys)
- Provide common shortcuts (copy, paste, etc.)
- Implement key press cooldowns

**Design Decisions:**
- Uses PyAutoGUI for keyboard simulation
- Provides high-level methods for common actions
- Implements cooldown to prevent key spam
- Supports modifier keys (Ctrl, Alt, Shift)

### 5. Configuration Manager (`config.py`)

**Purpose:** Centralized configuration management.

**Key Responsibilities:**
- Load settings from JSON file
- Provide dot-notation access to nested settings
- Save runtime changes to disk
- Provide default values

**Design Decisions:**
- Uses JSON for human-readable configuration
- Implements dot notation for easy access
- Provides defaults if config file missing
- Allows runtime updates

### 6. Utility Modules (`utils/`)

#### Smoothing (`smoothing.py`)
- Exponential Moving Average (EMA)
- Simple Moving Average (SMA)
- One Euro Filter (advanced adaptive smoothing)

#### Calibration (`calibration.py`)
- User profile management
- Sensitivity adjustment
- Accessibility presets
- Screen boundary calibration

#### Feedback (`feedback.py`)
- Visual overlays (gesture name, FPS)
- Status messages
- Cursor indicators
- High-contrast options

## Data Flow

### Frame Processing Pipeline

```
1. Camera Capture
   └─> Raw BGR frame (e.g., 1280x720)

2. Hand Tracking
   └─> Flip frame (mirror mode)
   └─> Convert BGR to RGB
   └─> MediaPipe processing
   └─> Extract landmarks (21 points, normalized 0-1)
   └─> Calculate finger states

3. Gesture Recognition
   └─> Analyze landmarks + finger states
   └─> Calculate distances (pinch detection)
   └─> Classify gesture
   └─> Apply debouncing
   └─> Return gesture enum

4. Action Processing
   └─> Map gesture to action
   └─> Execute mouse/keyboard command
   └─> Apply smoothing (for cursor)
   └─> Update system state

5. Visual Feedback
   └─> Draw landmarks on frame
   └─> Add gesture indicator
   └─> Add FPS counter
   └─> Display frame

6. Loop
   └─> Repeat at ~30 FPS
```

## Performance Considerations

### Optimization Strategies

1. **Frame Rate Management**
   - Target: 30 FPS minimum
   - MediaPipe is optimized for real-time processing
   - Reduce resolution if needed (640x480 for slower systems)

2. **Smoothing Trade-offs**
   - Higher smoothing = less jitter, more latency
   - Lower smoothing = more responsive, more jitter
   - Default: 0.5 (balanced)

3. **Gesture Debouncing**
   - Prevents rapid gesture switching
   - Default: 0.5 seconds
   - Adjustable based on user needs

4. **Memory Management**
   - MediaPipe handles model loading
   - Minimal memory footprint (~200MB)
   - No frame buffering (real-time only)

## Error Handling

### Graceful Degradation

1. **Camera Failure**
   - Check camera availability on startup
   - Provide clear error message
   - Exit gracefully

2. **Hand Not Detected**
   - Continue processing frames
   - Reset smoothing values
   - Show "no hand" indicator

3. **Configuration Errors**
   - Fall back to default values
   - Log warnings
   - Continue operation

4. **System Control Failures**
   - PyAutoGUI FailSafe (move to corner to abort)
   - Catch exceptions on mouse/keyboard operations
   - Log errors without crashing

## Extensibility

### Adding New Gestures

1. Define gesture in `Gesture` enum
2. Add detection logic in `recognize_gesture()`
3. Map to action in `process_gesture_action()`
4. Update documentation

### Adding New Actions

1. Implement in appropriate controller
2. Add configuration options
3. Map from gesture
4. Test thoroughly

### Custom Smoothing Algorithms

1. Create new class in `utils/smoothing.py`
2. Implement `smooth()` and `smooth_point()` methods
3. Integrate in `MouseController`

## Security Considerations

1. **System Access**
   - Requires permissions for mouse/keyboard control
   - No network access
   - No data collection

2. **FailSafe Mechanism**
   - PyAutoGUI FailSafe enabled
   - Move mouse to corner to abort
   - Keyboard interrupt (Ctrl+C) works

3. **Privacy**
   - No video recording
   - No data transmission
   - All processing local

## Future Architecture Improvements

1. **Plugin System**
   - Allow custom gesture handlers
   - Third-party action modules

2. **Machine Learning**
   - Custom gesture training
   - User-specific models
   - Improved accuracy

3. **Multi-Modal Input**
   - Combine with voice commands
   - Eye tracking integration
   - Multi-hand gestures

4. **Distributed Processing**
   - Offload ML to GPU
   - Cloud-based gesture recognition
   - Mobile device support

---

This architecture provides a solid foundation for an accessible, extensible, and maintainable assistive technology system.

