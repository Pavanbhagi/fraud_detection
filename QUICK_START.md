# ⚡ Quick Start Guide

## 🚀 Fastest Way to Run

### **Option 1: Double-Click (Easiest)**
1. Double-click `START_HERE.bat`
2. Wait for server to start
3. Browser opens automatically (or visit http://localhost:8000)

### **Option 2: Command Line**
```powershell
cd C:\Users\Dell\OneDrive\Desktop\Cursor
py api.py
```

### **Option 3: PowerShell Script**
```powershell
.\START_HERE.ps1
```

---

## 📋 First Time Setup

### **1. Install Dependencies**
```powershell
py -m pip install -r requirements.txt
```

### **2. Verify Tesseract**
```powershell
py test_tesseract.py
```

### **3. Run Server**
```powershell
py api.py
```

---

## ✅ Checklist

Before running:
- [ ] Python installed (`py --version`)
- [ ] Dependencies installed (`py -m pip install -r requirements.txt`)
- [ ] Tesseract OCR installed
- [ ] Files organized correctly

---

## 🎯 Usage

1. **Start server:** `py api.py` or double-click `START_HERE.bat`
2. **Open browser:** http://localhost:8000
3. **Upload image:** Drag & drop or click to browse
4. **Detect:** Click "Detect Credit Card"
5. **View results:** See detected card information

---

## 🛑 Stop Server

Press `Ctrl + C` in the terminal window

---

**That's it! Simple and easy.** 🎉
