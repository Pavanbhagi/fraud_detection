# ✅ Installation Checklist

Use this checklist to ensure everything is set up correctly.

## 📋 Pre-Installation

- [ ] Python 3.7+ installed
  ```powershell
  py --version
  ```
  Should show: Python 3.7.0 or higher

- [ ] pip is working
  ```powershell
  py -m pip --version
  ```

## 📦 Installation Steps

### Step 1: Project Files
- [ ] All project files are in the same folder
- [ ] `api.py` exists
- [ ] `credit_card_detector.py` exists
- [ ] `requirements.txt` exists
- [ ] `templates/` folder exists with `index.html`
- [ ] `static/` folder exists with `style.css` and `script.js`

### Step 2: Install Dependencies
```powershell
py -m pip install -r requirements.txt
```

- [ ] opencv-python installed
- [ ] numpy installed
- [ ] pillow installed
- [ ] pytesseract installed
- [ ] flask installed
- [ ] werkzeug installed

**Verify:**
```powershell
py -m pip list | Select-String "opencv|flask|pytesseract|numpy|pillow"
```

### Step 3: Install Tesseract OCR
- [ ] Tesseract downloaded from: https://github.com/UB-Mannheim/tesseract/wiki
- [ ] Tesseract installed on system
- [ ] Path noted or added to system PATH

**Verify:**
```powershell
py test_tesseract.py
```
Should show: `[OK] Tesseract version: X.X.X`

### Step 4: Configure Tesseract Path
- [ ] Checked Tesseract path in `api.py` (line 13)
- [ ] Path is correct for your system
- [ ] Or Tesseract is in system PATH

**Find path:**
```powershell
py find_tesseract.py
```

## 🧪 Testing

### Test 1: Tesseract
```powershell
py test_tesseract.py
```
- [ ] Shows Tesseract version
- [ ] No errors

### Test 2: Server Start
```powershell
py api.py
```
- [ ] Server starts without errors
- [ ] Shows: "Running on http://0.0.0.0:8000"
- [ ] No import errors

### Test 3: Web Interface
1. Open browser: http://localhost:8000
- [ ] Page loads
- [ ] Upload area visible
- [ ] No console errors (F12)

### Test 4: API Health
```powershell
Invoke-WebRequest http://localhost:8000/health
```
- [ ] Returns: `{"status": "healthy"}`

## ✅ Final Verification

- [ ] All dependencies installed
- [ ] Tesseract working
- [ ] Server starts successfully
- [ ] Web interface loads
- [ ] Can upload images
- [ ] Detection works

## 🎯 Quick Test

1. Start server: `py api.py`
2. Open: http://localhost:8000
3. Upload a credit card image
4. Click "Detect Credit Card"
5. Verify results appear

## ❌ Common Issues

### Issue: ModuleNotFoundError
**Solution:**
```powershell
py -m pip install -r requirements.txt
```

### Issue: Tesseract not found
**Solution:**
1. Install Tesseract
2. Update path in `api.py`
3. Run `py test_tesseract.py`

### Issue: Port 8000 in use
**Solution:**
- Change port in `api.py` (line 62)
- Or: `netstat -ano | findstr :8000` then kill process

### Issue: Flask not found
**Solution:**
```powershell
py -m pip install flask
```

---

**If all checkboxes are checked, you're ready to go!** ✅
