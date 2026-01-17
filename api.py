from flask import Flask, request, jsonify, render_template
from credit_card_detector import ModernCreditCardDetector
import cv2
import numpy as np
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize detector with Tesseract path
detector = None
tesseract_path = r'C:\Users\Dell\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
if os.path.exists(tesseract_path):
    detector = ModernCreditCardDetector(tesseract_cmd=tesseract_path)
else:
    try:
        detector = ModernCreditCardDetector()  # Try default PATH
    except Exception as init_error:
        print(f"Warning: Detector initialization failed: {init_error}")

@app.route('/detect', methods=['POST'])
def detect_credit_card():
    """
    Detect and extract credit card information from uploaded image
    """
    try:
        if detector is None:
            return jsonify({'error': 'Detector not initialized'}), 500
        
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read image
        file_bytes = file.read()
        nparr = np.frombuffer(file_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            return jsonify({'error': 'Invalid image format'}), 400
        
        # Process image
        results = detector.process_image_from_array(image)
        
        # Validate card numbers
        for card in results['cards']:
            if card['card_number']:
                card['is_valid'] = detector.validate_card_number(card['card_number'])
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'model': 'OpenCV + Tesseract OCR'})

@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
