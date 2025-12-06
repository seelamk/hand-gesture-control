# Contributing to Hand Gesture Control System

Thank you for your interest in contributing to this assistive technology project! This guide will help you understand how to contribute effectively.

## 🎯 Project Goals

This project aims to:
- Make computer interaction accessible to people with disabilities
- Provide well-documented, educational code
- Create a reliable, user-friendly assistive technology
- Foster an inclusive development community

## 🤝 Ways to Contribute

### 1. Code Contributions
- Bug fixes
- New gesture implementations
- Performance improvements
- New features (see Future Enhancements in README)

### 2. Documentation
- Improve existing documentation
- Add tutorials and guides
- Create video demonstrations
- Translate documentation

### 3. Testing
- Test on different hardware
- Test with different accessibility needs
- Report bugs and issues
- Suggest improvements

### 4. Accessibility Feedback
- Share user experiences
- Suggest accessibility improvements
- Test with assistive technologies
- Provide use case scenarios

## 📝 Code Style Guidelines

### Python Style
Follow PEP 8 with these specifics:

```python
# Use descriptive variable names
hand_landmarks = tracker.get_hand_landmarks()  # Good
hl = tracker.get_hl()  # Bad

# Add comprehensive docstrings
def recognize_gesture(self, landmarks: List, finger_states: dict) -> Gesture:
    """
    Recognize gesture from hand landmarks and finger states
    
    Args:
        landmarks: List of 21 hand landmarks (x, y, z)
        finger_states: Dictionary of finger states
        
    Returns:
        Gesture: Recognized gesture enum
    """
    pass

# Use type hints
def move_cursor(self, x: float, y: float) -> None:
    pass

# Keep functions focused and small
# One function = one responsibility
```

### Documentation Standards

Every file should include:
```python
"""
Module Name

Brief description of what this module does and why it exists.

Key Features:
- Feature 1
- Feature 2

Author: Hand Gesture Control Team
Purpose: Assistive technology for users with mobility limitations
"""
```

Every class should include:
```python
class ClassName:
    """
    Brief description of the class
    
    Detailed explanation of what this class does, how it works,
    and when to use it.
    """
```

Every function should include:
```python
def function_name(param1: type, param2: type) -> return_type:
    """
    Brief description
    
    Detailed explanation if needed.
    
    Args:
        param1 (type): Description
        param2 (type): Description
        
    Returns:
        return_type: Description
        
    Example:
        >>> result = function_name(value1, value2)
    """
```

## 🔧 Development Setup

1. Fork the repository
2. Clone your fork
3. Create a virtual environment
4. Install dependencies
5. Create a feature branch

```bash
git clone https://github.com/yourusername/HandGestures.git
cd HandGestures
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
git checkout -b feature/your-feature-name
```

## 🧪 Testing Your Changes

Before submitting:

1. **Test basic functionality**
   ```bash
   python test_camera.py
   python src/main.py
   ```

2. **Test all gestures**
   - Verify each gesture works
   - Check for false positives
   - Test edge cases

3. **Check performance**
   - Monitor FPS (should be 25+ on average hardware)
   - Check CPU usage
   - Test on different resolutions

4. **Test accessibility**
   - Try with different lighting
   - Test at different distances
   - Verify visual feedback is clear

## 📤 Submitting Changes

### Commit Messages

Use clear, descriptive commit messages:

```
Good:
- "Add thumb gesture detection for scrolling"
- "Fix cursor jitter by improving smoothing algorithm"
- "Update documentation for gesture calibration"

Bad:
- "Update"
- "Fix bug"
- "Changes"
```

### Pull Request Process

1. **Update documentation**
   - Update README if adding features
   - Add docstrings to new code
   - Update ARCHITECTURE.md if changing structure

2. **Create pull request**
   - Describe what you changed and why
   - Reference any related issues
   - Include screenshots/videos if relevant

3. **Pull request template**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Performance improvement
   
   ## Testing
   How did you test these changes?
   
   ## Accessibility Impact
   How does this affect users with disabilities?
   
   ## Screenshots/Videos
   If applicable
   ```

## 🐛 Reporting Bugs

Use this template for bug reports:

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: Windows 10 / macOS / Linux
- Python version: 3.x
- Camera: Built-in / External
- Resolution: 1280x720

## Screenshots/Logs
If applicable
```

## 💡 Suggesting Features

Use this template for feature requests:

```markdown
## Feature Description
Clear description of the feature

## Use Case
Who would benefit and how?

## Accessibility Impact
How does this improve accessibility?

## Implementation Ideas
Any thoughts on how to implement?
```

## 🌟 Priority Areas

We especially welcome contributions in:

1. **Accessibility Features**
   - Voice feedback
   - High contrast modes
   - Customizable gesture sensitivity
   - One-handed operation modes

2. **Performance**
   - Optimization for slower hardware
   - Reduced latency
   - Better smoothing algorithms

3. **Gesture Recognition**
   - More robust detection
   - Custom gesture training
   - Multi-hand support

4. **Documentation**
   - Video tutorials
   - Accessibility guides
   - Translation to other languages

## 📜 Code of Conduct

### Our Standards

- Be respectful and inclusive
- Welcome newcomers
- Focus on accessibility
- Provide constructive feedback
- Prioritize user needs

### Unacceptable Behavior

- Harassment or discrimination
- Dismissing accessibility concerns
- Unconstructive criticism
- Sharing private information

## 🙏 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Acknowledged in documentation

## 📧 Questions?

- Open an issue for questions
- Tag with "question" label
- Be patient - we're volunteers!

---

**Thank you for helping make technology more accessible!**

Every contribution, no matter how small, makes a difference in someone's life.

