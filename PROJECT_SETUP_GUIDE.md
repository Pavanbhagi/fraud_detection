# 📁 Complete Project Setup Guide

## 🎯 Project Structure

Here's the complete file structure for your Credit Card Detection System:

```
CreditCardDetection/
│
├── 📁 templates/              # HTML templates (Flask)
│   └── index.html            # Main web interface
│
├── 📁 static/                # Static files (CSS, JS, images)
│   ├── style.css            # Styling
│   └── script.js             # JavaScript functionality
│
├── 📁 __pycache__/           # Python cache (auto-generated, ignore)
│
├── 📄 api.py                 # Flask web server & API
├── 📄 credit_card_detector.py # Main detection logic
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md              # Project documentation
├── 📄 .gitignore             # Git ignore file
│
└── 📄 Documentation files:
    ├── PROJECT_SETUP_GUIDE.md    # This file
    ├── WEB_APP_GUIDE.md          # Web app usage
    ├── STEP_BY_STEP_EXPLANATION.md
    ├── CODE_WALKTHROUGH.md
    └── SYSTEM_STATUS.md
```

---

## 🚀 Step-by-Step Setup Instructions

### **STEP 1: Create Project Folder**

```powershell
# Create main project folder
mkdir CreditCardDetection
cd CreditCardDetection
```

### **STEP 2: Create Folder Structure**

```powershell
# Create necessary folders
mkdir templates
mkdir static
```

### **STEP 3: Create Python Files**

Create these files in the root directory:

#### **3.1 requirements.txt**
```
opencv-python>=4.5.0
numpy>=1.19.0
pillow>=8.0.0
pytesseract>=0.3.8
flask>=2.0.0
werkzeug>=2.0.0
```

#### **3.2 credit_card_detector.py**
*(Copy the existing file - already created)*

#### **3.3 api.py**
*(Copy the existing file - already created)*

### **STEP 4: Create Web Files**

#### **4.1 templates/index.html**
*(Copy from existing templates/index.html)*

#### **4.2 static/style.css**
*(Copy from existing static/style.css)*

#### **4.3 static/script.js**
*(Copy from existing static/script.js)*

---

## 📦 Installation Process

### **Method 1: Fresh Installation (Recommended)**

```powershell
# 1. Navigate to project folder
cd CreditCardDetection

# 2. Create virtual environment (optional but recommended)
py -m venv venv

# 3. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 4. Install dependencies
py -m pip install --upgrade pip
py -m pip install -r requirements.txt

# 5. Install Tesseract OCR
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
# Install to default location or note the path

# 6. Update Tesseract path in api.py if needed
# (Check the path in api.py - line 13)
```

### **Method 2: Quick Setup (If files already exist)**

```powershell
# 1. Navigate to project folder
cd C:\Users\Dell\OneDrive\Desktop\Cursor

# 2. Install/update dependencies
py -m pip install -r requirements.txt

# 3. Verify Tesseract is installed
py test_tesseract.py
```

---

## ▶️ How to Execute

### **Option 1: Run from Command Line**

```powershell
# Navigate to project folder
cd C:\Users\Dell\OneDrive\Desktop\Cursor

# Run the server
py api.py
```

**Output:**
```
 * Running on http://0.0.0.0:8000
 * Debug mode: on
```

### **Option 2: Create a Batch File (Easy Execution)**

Create `start_server.bat`:
```batch
@echo off
echo Starting Credit Card Detection Server...
cd /d "%~dp0"
py api.py
pause
```

**To use:** Double-click `start_server.bat`

### **Option 3: Create PowerShell Script**

Create `start_server.ps1`:
```powershell
Write-Host "Starting Credit Card Detection Server..." -ForegroundColor Green
Set-Location $PSScriptRoot
py api.py
```

**To use:** Right-click → Run with PowerShell

---

## 🔧 Configuration

### **Tesseract OCR Path**

If Tesseract is installed in a different location, update `api.py`:

```python
# Line 13 in api.py
tesseract_path = r'C:\Your\Path\To\Tesseract-OCR\tesseract.exe'
```

**To find Tesseract:**
```powershell
py find_tesseract.py
```

### **Port Configuration**

To change the port (default: 8000), edit `api.py`:

```python
# Line 62 in api.py
app.run(host='0.0.0.0', port=8000, debug=True)
# Change 8000 to your desired port
```

---

## ✅ Verification Checklist

Before running, verify:

- [ ] Python 3.7+ installed (`py --version`)
- [ ] All dependencies installed (`py -m pip list`)
- [ ] Tesseract OCR installed and path configured
- [ ] `templates/` folder exists with `index.html`
- [ ] `static/` folder exists with `style.css` and `script.js`
- [ ] `api.py` and `credit_card_detector.py` are in root folder
- [ ] `requirements.txt` is present

**Quick check:**
```powershell
# Check Python
py --version

# Check dependencies
py -m pip list | Select-String "opencv|flask|pytesseract"

# Check Tesseract
py test_tesseract.py

# Check file structure
Get-ChildItem -Recurse | Select-Object FullName
```

---

## 🗂️ Complete File Organization

### **Root Directory Files:**
```
api.py                          # Main Flask application
credit_card_detector.py         # Detection engine
requirements.txt                # Dependencies
README.md                       # Documentation
.gitignore                      # Git configuration
test_detector.py                # Testing script
test_tesseract.py               # Tesseract verification
find_tesseract.py               # Tesseract finder
```

### **templates/ Directory:**
```
templates/
  └── index.html               # Web interface HTML
```

### **static/ Directory:**
```
static/
  ├── style.css                # CSS styling
  └── script.js                # JavaScript
```

---

## 🔄 Daily Usage Workflow

### **Starting the Application:**

1. **Open Terminal/PowerShell**
2. **Navigate to project:**
   ```powershell
   cd C:\Users\Dell\OneDrive\Desktop\Cursor
   ```
3. **Start server:**
   ```powershell
   py api.py
   ```
4. **Open browser:**
   ```
   http://localhost:8000
   ```

### **Stopping the Application:**

- Press `Ctrl + C` in the terminal
- Or close the terminal window

---

## 📝 Creating a Startup Script

### **Windows Batch File (.bat)**

Create `START_HERE.bat`:
```batch
@echo off
title Credit Card Detection Server
color 0A
echo ========================================
echo   Credit Card Detection System
echo ========================================
echo.
echo Starting server...
echo.
echo Open your browser and visit:
echo http://localhost:8000
echo.
echo Press Ctrl+C to stop the server
echo.
cd /d "%~dp0"
py api.py
pause
```

### **PowerShell Script (.ps1)**

Create `START_HERE.ps1`:
```powershell
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Credit Card Detection System" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Starting server..." -ForegroundColor Green
Write-Host ""
Write-Host "Open your browser and visit:" -ForegroundColor Yellow
Write-Host "http://localhost:8000" -ForegroundColor Yellow
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Gray
Write-Host ""

Set-Location $PSScriptRoot
py api.py
```

---

## 🐛 Troubleshooting

### **Issue: Module not found**
```powershell
# Solution: Install dependencies
py -m pip install -r requirements.txt
```

### **Issue: Tesseract not found**
```powershell
# Solution 1: Install Tesseract
# Download from: https://github.com/UB-Mannheim/tesseract/wiki

# Solution 2: Update path in api.py
# Run: py find_tesseract.py
```

### **Issue: Port already in use**
```powershell
# Solution: Change port in api.py
# Or kill process using port 8000:
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### **Issue: Flask not found**
```powershell
# Solution: Install Flask
py -m pip install flask
```

---

## 📦 Backup & Transfer

### **Files to Backup:**
```
✅ All .py files
✅ requirements.txt
✅ templates/ folder
✅ static/ folder
✅ README.md
✅ .gitignore
```

### **Files to Ignore:**
```
❌ __pycache__/ (auto-generated)
❌ *.pyc files (compiled Python)
❌ venv/ (virtual environment - recreate)
❌ .vscode/ (editor settings)
```

### **Creating a Portable Version:**

1. **Copy project folder**
2. **Include requirements.txt**
3. **Note Tesseract installation path**
4. **On new machine:**
   - Install Python
   - Install Tesseract
   - Run: `py -m pip install -r requirements.txt`
   - Update Tesseract path in `api.py`
   - Run: `py api.py`

---

## 🎯 Quick Reference

### **Essential Commands:**

```powershell
# Install dependencies
py -m pip install -r requirements.txt

# Run server
py api.py

# Test Tesseract
py test_tesseract.py

# Test detector
py test_detector.py image.jpg

# Check health
Invoke-WebRequest http://localhost:8000/health
```

### **Important Paths:**

- **Project Root:** `C:\Users\Dell\OneDrive\Desktop\Cursor`
- **Templates:** `templates/index.html`
- **Static Files:** `static/style.css`, `static/script.js`
- **Tesseract:** `C:\Users\Dell\AppData\Local\Programs\Tesseract-OCR\tesseract.exe`

---

## 📚 Next Steps

1. ✅ **Organize files** as shown above
2. ✅ **Create startup script** for easy execution
3. ✅ **Test the application** with sample images
4. ✅ **Bookmark this guide** for future reference

---

**Your project is now properly organized and ready for future use!** 🚀
