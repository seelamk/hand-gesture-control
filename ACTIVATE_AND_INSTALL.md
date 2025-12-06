# Quick Setup Guide - Python 3.12

## ✅ Good News!

I've created a Python 3.12 virtual environment for you at `.venv312`

## 🚀 Next Steps (Copy and Paste These Commands)

### Step 1: Activate the Python 3.12 Environment

```powershell
.\.venv312\Scripts\activate
```

After activation, your prompt should show `(.venv312)` at the beginning.

### Step 2: Verify Python Version

```powershell
python --version
```

Should show: `Python 3.12.x`

### Step 3: Install Dependencies

```powershell
pip install -r requirements.txt
```

This will install:
- mediapipe (hand tracking)
- opencv-python (camera)
- numpy (calculations)
- pyautogui (mouse/keyboard control)
- pynput (input monitoring)
- Pillow (image processing)

### Step 4: Test Camera

```powershell
python test_camera.py
```

### Step 5: Run the Application

```powershell
python src/main.py
```

---

## 📋 Complete Command Sequence

Just copy and paste all of these:

```powershell
.\.venv312\Scripts\activate
python --version
pip install --upgrade pip
pip install -r requirements.txt
python test_camera.py
```

---

## ❓ Troubleshooting

### If activation doesn't work:
```powershell
# Try this instead:
.venv312\Scripts\Activate.ps1
```

### If you get execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv312\Scripts\activate
```

---

## 💡 For Future Sessions

Every time you want to use the application:

```powershell
# Navigate to project folder
cd C:\Users\seela\Downloads\MineCoding\HandGestures

# Activate Python 3.12 environment
.\.venv312\Scripts\activate

# Run the application
python src/main.py
```

---

## 🎯 Why Python 3.12?

- MediaPipe currently supports Python 3.8 - 3.12
- Python 3.14 is too new (released recently)
- MediaPipe team hasn't built wheels for 3.14 yet
- Python 3.12 is stable and fully supported

---

**Ready to proceed? Run the commands above!** 🚀

