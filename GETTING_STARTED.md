# Getting Started - Hand Gesture Control System

Welcome! This guide will get you up and running in 10 minutes.

## ⚡ Quick Start (5 Steps)

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```
⏱️ **Time:** 3-5 minutes

### Step 2: Test Your Camera
```bash
python test_camera.py
```
✅ **Expected:** Camera window opens, press 'q' to close

### Step 3: Run the Application
```bash
python src/main.py
```
✅ **Expected:** Application window opens with camera feed

### Step 4: Try Your First Gesture
👉 **POINT** - Extend your index finger
- Move your hand slowly
- Watch the cursor follow your finger

### Step 5: Try Clicking
🤏 **PINCH** - Bring thumb and index finger together
- Should trigger a click
- Try clicking on something!

---

## 🎯 First 5 Minutes Checklist

- [ ] Dependencies installed
- [ ] Camera working
- [ ] Application running
- [ ] Hand detected (landmarks visible)
- [ ] POINT gesture moves cursor
- [ ] PINCH gesture clicks

**If all checked:** Congratulations! You're ready to use the system! 🎉

**If any failed:** See troubleshooting below ⬇️

---

## 🔧 Quick Troubleshooting

### Camera Not Working?
```bash
# Try different camera ID in config.json
"device_id": 1  # Change from 0 to 1, 2, etc.
```

### Hand Not Detected?
1. Improve lighting (face a window)
2. Move closer to camera (1.5-2 feet)
3. Ensure hand is in frame

### Cursor Too Fast/Slow?
Edit `config.json`:
```json
{
  "mouse_control": {
    "sensitivity": 1.5  // Lower = slower, Higher = faster
  }
}
```

---

## 📚 What to Read Next

### For Users
1. **QUICK_REFERENCE.md** - All gestures and shortcuts
2. **README.md** - Full features and usage
3. **SETUP_GUIDE.md** - Detailed setup and calibration

### For Developers
1. **ARCHITECTURE.md** - System design
2. **PROJECT_STRUCTURE.md** - Code organization
3. **Source code** - Start with `src/main.py`

---

## 🎮 Practice Routine (10 Minutes)

### Minute 1-2: POINT Gesture
- Practice moving cursor smoothly
- Try reaching all corners of screen
- Get comfortable with movement

### Minute 3-4: PINCH Gesture
- Practice clicking
- Try double-clicking (pinch twice quickly)
- Click on different targets

### Minute 5-6: PEACE Gesture
- Practice right-clicking
- Try opening context menus
- Get timing right

### Minute 7-8: PALM Gesture
- Practice pausing
- Use when you need to rest
- Resume when ready

### Minute 9-10: Scrolling
- Try THUMB_UP (scroll up)
- Try THUMB_DOWN (scroll down)
- Practice smooth scrolling

---

## 💡 Pro Tips for Beginners

1. **Start Slow**
   - Don't rush
   - Practice each gesture individually
   - Speed comes with practice

2. **Good Lighting**
   - Face a window or lamp
   - Avoid backlighting
   - Consistent lighting helps accuracy

3. **Stable Position**
   - Keep camera stable
   - Maintain consistent distance
   - Use a comfortable seating position

4. **Take Breaks**
   - Use PALM gesture to pause
   - Rest every 15 minutes
   - Don't overdo it on day one

5. **Adjust Settings**
   - Everyone is different
   - Experiment with sensitivity
   - Find what works for you

---

## 🎯 Your First Tasks

Try these simple tasks to build confidence:

### Task 1: Web Browsing
- [ ] Open a web browser
- [ ] Use POINT to move cursor
- [ ] Use PINCH to click links
- [ ] Use THUMB_UP/DOWN to scroll

### Task 2: File Management
- [ ] Open file explorer
- [ ] Navigate folders with POINT
- [ ] Click files with PINCH
- [ ] Right-click with PEACE

### Task 3: Document Reading
- [ ] Open a document
- [ ] Scroll with THUMB gestures
- [ ] Pause with PALM when needed
- [ ] Resume and continue

---

## 📊 Progress Tracking

### Day 1 Goals
- [ ] Successfully install and run
- [ ] Master POINT gesture
- [ ] Comfortable with PINCH
- [ ] Understand PALM (pause)

### Week 1 Goals
- [ ] Use all 7 gestures confidently
- [ ] Customize settings to preference
- [ ] Use for simple daily tasks
- [ ] Comfortable with 15-minute sessions

### Month 1 Goals
- [ ] Use as primary input method
- [ ] Efficient at common tasks
- [ ] Created personal profile
- [ ] Helping others learn

---

## 🆘 Need Help?

### Quick Answers
- **Q: Cursor too jittery?**
  - A: Increase `smoothing_factor` to 0.7-0.8

- **Q: Gestures not recognized?**
  - A: Make gestures more distinct, hold for 1 second

- **Q: System too slow?**
  - A: Reduce camera resolution in config.json

### More Help
1. Check **QUICK_REFERENCE.md** for gesture guide
2. Read **SETUP_GUIDE.md** for detailed setup
3. Review **README.md** troubleshooting section

---

## 🌟 Success Indicators

You're doing great if:
- ✅ Cursor follows your hand smoothly
- ✅ Clicks happen when you want them
- ✅ You can pause/resume easily
- ✅ You're comfortable for 5+ minutes
- ✅ You're having fun! 😊

---

## 🎓 Learning Path

```
Day 1: Basic gestures (POINT, PINCH)
  ↓
Week 1: All gestures + customization
  ↓
Month 1: Daily usage + optimization
  ↓
Beyond: Advanced features + contribution
```

---

## 🚀 Ready to Start?

```bash
# Let's go!
python src/main.py
```

**Remember:** This is assistive technology designed to help you. Take your time, be patient with yourself, and enjoy the journey!

---

**Welcome to the Hand Gesture Control community!** 🤲✨

*If you find this helpful, consider contributing improvements or sharing with others who might benefit.*

