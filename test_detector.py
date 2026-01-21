                print(f"  Valid (Luhn): {'Yes' if is_valid else 'No'}")

from credit_card_detector import ModernCreditCardDetector
import sys

def test_detection(image_path: str = "sample_card.jpg"):
    """
    Test the credit card detector on a sample image
    """
    print("Initializing Credit Card Detector...")
    # Auto-detect Tesseract path
    import os
    tesseract_path = r'C:\Users\Dell\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    if os.path.exists(tesseract_path):
        detector = ModernCreditCardDetector(tesseract_cmd=tesseract_path)
    else:
        detector = ModernCreditCardDetector()
    
    print(f"\nProcessing image: {image_path}")
    try:
        result = detector.process_image(image_path)
        
        print(f"\n{'='*50}")
        print(f"Cards detected: {result['num_cards_detected']}")
        print(f"{'='*50}")
        
        for i, card in enumerate(result['cards']):
            print(f"\nCard {i+1}:")
            print(f"  Detection Confidence: {card.get('detection_confidence', 0):.2%}")
            print(f"  Card Number: {card['card_number'] or 'Not found'}")
            if card['card_number']:
                is_valid = detector.validate_card_number(card['card_number'])
                print(f"  Valid (Luhn): {'Yes' if is_valid else 'No'}")
            print(f"  Cardholder Name: {card['cardholder_name'] or 'Not found'}")
            print(f"  Expiry Date: {card['expiry_date'] or 'Not found'}")
            print(f"  Bounding Box: {card['bbox']}")
            
            if card.get('all_text'):
                print("\n  All detected text:")
                for text_item in card['all_text']:
                    print(f"    - {text_item['text']} (confidence: {text_item['confidence']:.2%})")
    
    except FileNotFoundError:
        print(f"Error: Image file '{image_path}' not found.")
        print("Please provide a valid image path.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "sample_card.jpg"
    test_detection(image_path)
