
# 🖱️ Human-like Mouse Mover & Activity Simulator

This repository contains two main files:

- `WindowsSecurity.py` – Python script that simulates natural mouse movements and detects user activity.
- `systemUpdater.exe` – Executable version of the `WindowsSecurity.py` script.

---

## 🚀 How to Run the Script

### ✅ Run from Python (requires `pip` packages)
1. **Install Dependencies**:
   ```bash
   pip install pyautogui keyboard pywin32
   ```

2. **Run the script**:
   ```bash
   python WindowsSecurity.py
   ```

---

## 🛠️ How to Convert `WindowsSecurity.py` to `.exe`

> You'll need **PyInstaller** to create a `.exe` file.

### 1. Install PyInstaller
```bash
pip install pyinstaller
```

### 2. Convert to .exe (console version)
```bash
pyinstaller --onefile WindowsSecurity.py
```

This will generate a standalone `WindowsSecurity.exe` file inside the `dist` folder.

---

## 🪄 How to Hide the Console Window

If you don’t want a command window to appear when running the `.exe`, use:

```bash
pyinstaller --onefile --noconsole WindowsSecurity.py
```

This creates a silent background process version, suitable for stealthy usage (e.g., system tray tools, silent automation, etc.).

---

## 📁 Files in This Repository

| File                | Description                                      |
|---------------------|--------------------------------------------------|
| `WindowsSecurity.py`| Main script for automated mouse movement         |
| `systemUpdater.exe` | Pre-built executable version of the script       |
| `README.md`         | This documentation                               |

---

## ❗ Notes

- The script pauses if you are typing or actively using the mouse.
- Includes random delays, scrolling, and window activation for natural behavior.
- Built for **Windows OS** only (due to `win32api` and GUI handling).

