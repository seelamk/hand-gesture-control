# Installation Troubleshooting Guide

## ❌ Error: "No matching distribution found for mediapipe"

### Problem
```
ERROR: Could not find a version that satisfies the requirement mediapipe>=0.10.0
ERROR: No matching distribution found for mediapipe>=0.10.0
```

### Cause
MediaPipe currently supports **Python 3.8 - 3.12** only. If you're using Python 3.13 or 3.14, MediaPipe doesn't have pre-built wheels yet.

### ✅ Solution 1: Use Python 3.12 (Recommended)

#### Step 1: Check if you have Python 3.12
```bash
py -3.12 --version
```

#### Step 2: Create new virtual environment with Python 3.12
```bash
# Deactivate current environment
deactivate

# Create new environment with Python 3.12
py -3.12 -m venv .venv312

# Activate the new environment
.venv312\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Step 3: Verify installation
```bash
python --version  # Should show Python 3.12.x
pip list  # Should show mediapipe installed
```

### ✅ Solution 2: Install Python 3.12

If you don't have Python 3.12:

1. **Download Python 3.12** from [python.org](https://www.python.org/downloads/)
2. **Install** with "Add to PATH" checked
3. **Follow Solution 1** above

### ✅ Solution 3: Try Alternative Hand Tracking (Advanced)

If you must use Python 3.13+, you can try alternative hand tracking libraries:

#### Option A: Build MediaPipe from Source
```bash
# This is complex and not recommended for beginners
git clone https://github.com/google/mediapipe.git
# Follow build instructions for your platform
```

#### Option B: Use OpenCV DNN with Hand Detection Model
This requires modifying the code to use a different hand tracking approach.

---

## 🔍 Checking Your Python Version

### Windows
```bash
python --version
py --version
py -3.12 --version
py -3.11 --version
```

### List all Python versions
```bash
py --list
```

---

## 📦 Other Common Installation Issues

### Issue: "pip is not recognized"
```bash
# Use python -m pip instead
python -m pip install -r requirements.txt
```

### Issue: "Permission denied"
```bash
# Run as administrator or use --user flag
pip install --user -r requirements.txt
```

### Issue: OpenCV installation fails
```bash
# Try installing opencv-python-headless instead
pip install opencv-python-headless>=4.8.0
```

### Issue: PyAutoGUI installation fails on Linux
```bash
# Install system dependencies first
sudo apt-get install python3-tk python3-dev
pip install -r requirements.txt
```

---

## ✅ Recommended Setup (Step by Step)

### For Windows Users

```bash
# 1. Check Python version
python --version

# 2. If not 3.8-3.12, install Python 3.12
# Download from python.org

# 3. Create virtual environment
py -3.12 -m venv .venv

# 4. Activate virtual environment
.venv\Scripts\activate

# 5. Upgrade pip
python -m pip install --upgrade pip

# 6. Install dependencies
pip install -r requirements.txt

# 7. Test installation
python test_camera.py
```

### For macOS/Linux Users

```bash
# 1. Check Python version
python3 --version

# 2. Create virtual environment
python3.12 -m venv .venv

# 3. Activate virtual environment
source .venv/bin/activate

# 4. Upgrade pip
python -m pip install --upgrade pip

# 5. Install dependencies
pip install -r requirements.txt

# 6. Test installation
python test_camera.py
```

---

## 🧪 Verify Installation

After installation, verify everything works:

```bash
# Test Python version
python --version

# Test imports
python -c "import mediapipe; print('MediaPipe:', mediapipe.__version__)"
python -c "import cv2; print('OpenCV:', cv2.__version__)"
python -c "import numpy; print('NumPy:', numpy.__version__)"
python -c "import pyautogui; print('PyAutoGUI: OK')"

# Test camera
python test_camera.py

# Run application
python src/main.py
```

---

## 📋 Quick Reference

| Python Version | MediaPipe Support | Recommendation |
|----------------|-------------------|----------------|
| 3.7 or lower | ❌ Not supported | Upgrade to 3.12 |
| 3.8 - 3.12 | ✅ Supported | Use this! |
| 3.13 - 3.14 | ❌ Not yet | Downgrade to 3.12 |

---

## 🆘 Still Having Issues?

1. **Check your Python version**
   ```bash
   python --version
   ```

2. **Make sure you're in virtual environment**
   ```bash
   # You should see (.venv) or (.venv312) in your prompt
   ```

3. **Try installing packages one by one**
   ```bash
   pip install mediapipe
   pip install opencv-python
   pip install numpy
   pip install pyautogui
   pip install pynput
   pip install Pillow
   ```

4. **Check for error messages**
   - Copy the full error message
   - Search for it online
   - Check MediaPipe GitHub issues

---

## 💡 Pro Tips

1. **Always use virtual environments**
   - Keeps dependencies isolated
   - Prevents conflicts

2. **Keep pip updated**
   ```bash
   python -m pip install --upgrade pip
   ```

3. **Use specific Python version**
   ```bash
   py -3.12 -m pip install -r requirements.txt
   ```

4. **Check compatibility before upgrading Python**
   - Not all libraries support latest Python immediately
   - Stick with stable versions (3.10-3.12)

---

## 📞 Getting Help

If you're still stuck:

1. Check the error message carefully
2. Verify Python version is 3.8-3.12
3. Make sure virtual environment is activated
4. Try the solutions above in order
5. Search for the specific error online

---

**Most Common Solution:** Use Python 3.12 instead of 3.14! 🎯

