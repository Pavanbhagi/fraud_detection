# 💳 Credit Card Detection System

A modern, AI-powered web application for detecting and extracting information from credit card images using OpenCV and Tesseract OCR.

## 🚀 Quick Start

### **Easiest Way (Double-Click):**
1. Double-click `START_HERE.bat`
2. Wait for server to start
3. Browser opens automatically at http://localhost:8000

### **Command Line:**
```powershell
# Install dependencies (first time only)
py -m pip install -r requirements.txt

# Start server
py api.py

# Open browser: http://localhost:8000
```

## 📁 Project Structure

```
Cursor/
├── api.py                    # Flask web server (MAIN FILE)
├── credit_card_detector.py   # Detection engine
├── requirements.txt          # Dependencies
├── START_HERE.bat            # Easy startup (double-click)
├── templates/
│   └── index.html           # Web interface
└── static/
    ├── style.css            # Styling
    └── script.js            # JavaScript
```

## 📦 Installation

### **Step 1: Install Python Dependencies**
```powershell
py -m pip install -r requirements.txt
```

### **Step 2: Install Tesseract OCR**
- Download from: https://github.com/UB-Mannheim/tesseract/wiki
- Install to default location
- Or update path in `api.py` (line 13)

### **Step 3: Verify Installation**
```powershell
py test_tesseract.py
```

## ▶️ Running the Application

### **Method 1: Batch File (Easiest)**
Double-click `START_HERE.bat`

### **Method 2: Command Line**
```powershell
py api.py
```

### **Method 3: PowerShell**
```powershell
.\START_HERE.ps1
```

Then open: **http://localhost:8000**

## 🎯 Features

- ✅ **Modern Web Interface** - Beautiful dark theme UI
- ✅ **Drag & Drop Upload** - Easy image upload
- ✅ **Real-time Detection** - Instant card detection
- ✅ **Text Extraction** - OCR-powered text reading
- ✅ **Card Validation** - Luhn algorithm validation
- ✅ **Confidence Scores** - Detection accuracy metrics
- ✅ **Responsive Design** - Works on mobile & desktop

## 📖 Usage

1. **Start Server:** Run `py api.py` or double-click `START_HERE.bat`
2. **Open Browser:** Visit http://localhost:8000
3. **Upload Image:** Drag & drop or click to browse
4. **Detect:** Click "Detect Credit Card" button
5. **View Results:** See extracted card information

## 🔧 Configuration

### **Tesseract Path**
If Tesseract is in a different location, edit `api.py`:
```python
tesseract_path = r'C:\Your\Path\To\Tesseract-OCR\tesseract.exe'
```

### **Change Port**
Edit `api.py` line 62:
```python
app.run(host='0.0.0.0', port=8000, debug=True)  # Change 8000
```

## 📚 Documentation

- **QUICK_START.md** - Fast setup guide
- **PROJECT_SETUP_GUIDE.md** - Complete setup instructions
- **WEB_APP_GUIDE.md** - Web application usage
- **STEP_BY_STEP_EXPLANATION.md** - How it works
- **CODE_WALKTHROUGH.md** - Code explanation

## 🛠️ Technology Stack

- **Python 3.7+** - Programming language
- **Flask** - Web framework
- **OpenCV** - Image processing
- **Tesseract OCR** - Text extraction
- **HTML/CSS/JavaScript** - Frontend

## ✅ Requirements

- Python 3.7 or higher
- Tesseract OCR installed
- Internet connection (for first-time dependency installation)

## 🐛 Troubleshooting

### **Module not found**
```powershell
py -m pip install -r requirements.txt
```

### **Tesseract not found**
- Install Tesseract from: https://github.com/UB-Mannheim/tesseract/wiki
- Update path in `api.py`
- Run: `py find_tesseract.py` to find path

### **Port already in use**
- Change port in `api.py` (line 62)
- Or kill process: `netstat -ano | findstr :8000`

## 📝 File Organization

**Essential Files:**
- `api.py` - Main server
- `credit_card_detector.py` - Detection logic
- `templates/index.html` - Web interface
- `static/style.css` - Styling
- `static/script.js` - JavaScript

**Startup Files:**
- `START_HERE.bat` - Windows batch file
- `START_HERE.ps1` - PowerShell script

## 🔒 Security Note

⚠️ This is a demonstration system. In production:
- Never store card images
- Mask sensitive data
- Use HTTPS encryption
- Implement authentication

## 📄 License

MIT License

## 🆘 Support

For issues or questions:
1. Check `PROJECT_SETUP_GUIDE.md` for setup help
2. Check `QUICK_START.md` for quick reference
3. Verify all dependencies are installed
4. Ensure Tesseract is properly configured

---

**Made with ❤️ using modern AI technology**
