"""
Quick test to verify Tesseract OCR is working
"""
import pytesseract
import os

# Set Tesseract path
tesseract_path = r'C:\Users\Dell\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
if os.path.exists(tesseract_path):
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
    print("[OK] Tesseract path configured")
else:
    print("[WARNING] Tesseract not found at expected path, trying default PATH")

try:
    version = pytesseract.get_tesseract_version()
    print(f"[OK] Tesseract version: {version}")
    print("\n[SUCCESS] Tesseract OCR is ready to use!")
except Exception as e:
    print(f"[ERROR] Tesseract not working: {e}")
    print("\nPlease ensure Tesseract is installed correctly.")
