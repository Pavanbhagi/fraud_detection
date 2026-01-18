import cv2
import numpy as np
import pytesseract
from typing import List, Dict, Optional
import re

class ModernCreditCardDetector:
    """
    Modern AI-powered credit card detection using OpenCV for detection
    and Tesseract OCR for text extraction (2025 technology - Python 3.7 compatible)
    """
    
    def __init__(self, tesseract_cmd: Optional[str] = None):
        """
        Initialize the detector
        
        Args:
            tesseract_cmd: Path to tesseract executable (if not in PATH)
        """
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        
        # Card number pattern (Luhn algorithm compatible)
        self.card_pattern = r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
        
    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """
        Advanced image preprocessing for better detection
        """
        # Convert to grayscale if needed
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()
        
        # Adaptive thresholding for varying lighting
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(gray)
        
        # Denoising
        denoised = cv2.fastNlMeansDenoising(enhanced, h=10)
        
        # Sharpening
        kernel = np.array([[-1, -1, -1],
                          [-1,  9, -1],
                          [-1, -1, -1]])
        sharpened = cv2.filter2D(denoised, -1, kernel)
        
        return sharpened
    
    def detect_card(self, image: np.ndarray) -> List[Dict]:
        """
        Detect credit cards in image using contour detection
        """
        # Preprocess image
        processed = self.preprocess_image(image)
        
        # Apply edge detection
        edges = cv2.Canny(processed, 50, 150)
        
        # Find contours
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filter contours by area and aspect ratio (credit cards are roughly 85.6mm x 53.98mm = 1.586 ratio)
        detections = []
        h, w = image.shape[:2]
        min_area = (w * h) * 0.01  # At least 1% of image
        max_area = (w * h) * 0.8   # At most 80% of image
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if min_area < area < max_area:
                # Get bounding rectangle
                x, y, width, height = cv2.boundingRect(contour)
                aspect_ratio = width / height if height > 0 else 0
                
                # Credit cards have aspect ratio around 1.5-1.7
                if 1.3 < aspect_ratio < 1.8:
                    # Calculate confidence based on how close to ideal ratio
                    ideal_ratio = 1.586
                    confidence = 1.0 - abs(aspect_ratio - ideal_ratio) / ideal_ratio
                    confidence = max(0.5, min(1.0, confidence))
                    
                    detections.append({
                        'bbox': [x, y, x + width, y + height],
                        'confidence': float(confidence)
                    })
        
        # Sort by confidence and return top detections
        detections.sort(key=lambda x: x['confidence'], reverse=True)
        return detections[:5]  # Return top 5 detections
    
    def extract_card_info(self, image: np.ndarray, bbox: List[int]) -> Dict:
        """
        Extract card information using Tesseract OCR
        """
        x1, y1, x2, y2 = bbox
        card_roi = image[y1:y2, x1:x2]
        
        # Preprocess ROI for better OCR
        roi_gray = cv2.cvtColor(card_roi, cv2.COLOR_BGR2GRAY) if len(card_roi.shape) == 3 else card_roi
        roi_enhanced = cv2.resize(roi_gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        _, roi_thresh = cv2.threshold(roi_enhanced, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        # Run OCR with custom config
        custom_config = r'--oem 3 --psm 6'
        ocr_text = pytesseract.image_to_string(roi_thresh, config=custom_config)
        
        # Also get detailed data
        ocr_data = pytesseract.image_to_data(roi_thresh, output_type=pytesseract.Output.DICT)
        
        # Extract text
        all_text = []
        card_number = None
        cardholder_name = None
        expiry_date = None
        
        # Process OCR results
        text_lines = ocr_text.split('\n')
        for line in text_lines:
            line = line.strip()
            if not line:
                continue
            
            all_text.append({'text': line, 'confidence': 0.8})  # Default confidence
            
            # Extract card number (16 digits)
            numbers = re.findall(r'\d+', line.replace(' ', '').replace('-', ''))
            for num in numbers:
                if len(num) == 16:
                    card_number = num
                    break
            
            # Extract expiry date (MM/YY or MM/YYYY)
            expiry_match = re.search(r'(\d{2})[/-](\d{2,4})', line)
            if expiry_match:
                expiry_date = line
            
            # Extract name (usually uppercase, letters only)
            if re.match(r'^[A-Z\s]+$', line) and len(line) > 5:
                if not cardholder_name:  # Take first match
                    cardholder_name = line
        
        return {
            'card_number': card_number,
            'cardholder_name': cardholder_name,
            'expiry_date': expiry_date,
            'all_text': all_text,
            'bbox': bbox
        }
    
    def process_image(self, image_path: str) -> Dict:
        """
        Complete pipeline: detect and extract card information
        """
        # Read image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Could not read image: {}".format(image_path))
        
        # Detect cards
        detections = self.detect_card(image)
        
        results = []
        for detection in detections:
            # Extract information from each detected card
            card_info = self.extract_card_info(image, detection['bbox'])
            card_info['detection_confidence'] = detection['confidence']
            results.append(card_info)
        
        return {
            'num_cards_detected': len(results),
            'cards': results
        }
    
    def process_image_from_array(self, image: np.ndarray) -> Dict:
        """
        Process image from numpy array (for API usage)
        """
        # Detect cards
        detections = self.detect_card(image)
        
        results = []
        for detection in detections:
            # Extract information from each detected card
            card_info = self.extract_card_info(image, detection['bbox'])
            card_info['detection_confidence'] = detection['confidence']
            
            # Validate card number if found
            if card_info['card_number']:
                card_info['is_valid'] = self.validate_card_number(card_info['card_number'])
            
            results.append(card_info)
        
        return {
            'num_cards_detected': len(results),
            'cards': results
        }
    
    def validate_card_number(self, card_number: str) -> bool:
        """
        Validate card number using Luhn algorithm
        """
        def luhn_check(card_num):
            def digits_of(n):
                return [int(d) for d in str(n)]
            digits = digits_of(card_num)
            odd_digits = digits[-1::-2]
            even_digits = digits[-2::-2]
            checksum = sum(odd_digits)
            for d in even_digits:
                checksum += sum(digits_of(d * 2))
            return checksum % 10 == 0
        
        # Remove spaces and dashes
        clean_number = card_number.replace(' ', '').replace('-', '')
        return luhn_check(clean_number) if clean_number.isdigit() else False
