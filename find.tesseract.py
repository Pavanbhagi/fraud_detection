"""
Helper script to find Tesseract OCR installation
"""
import os
import subprocess

def find_tesseract():
    """Find Tesseract OCR executable"""
    possible_paths = [
        r"C:\Program Files\Tesseract-OCR\tesseract.exe",
        r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
        r"C:\Users\{}\AppData\Local\Programs\Tesseract-OCR\tesseract.exe".format(os.getenv('USERNAME')),
    ]
    
    # Check PATH
    try:
        result = subprocess.run(['tesseract', '--version'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        if result.returncode == 0:
            print("[OK] Tesseract found in PATH")
            print(result.stdout)
            return None  # None means use default PATH
    except:
        pass
    
    # Check common installation paths
    for path in possible_paths:
        if os.path.exists(path):
            print(f"[OK] Tesseract found at: {path}")
            return path
    
    print("[ERROR] Tesseract not found. Please install from:")
    print("  https://github.com/UB-Mannheim/tesseract/wiki")
    print("\nOr add Tesseract to your system PATH")
    return None

if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    tesseract_path = find_tesseract()
    if tesseract_path:
        print(f"\nTo use this path, update credit_card_detector.py:")
        print(f"  detector = ModernCreditCardDetector(tesseract_cmd=r'{tesseract_path}')")
