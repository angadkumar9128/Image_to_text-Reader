from PIL import Image
import pytesseract

# Open the image
image_path = 'Screenshot (2).png'
image = Image.open(image_path)

# Apply OCR
extracted_text = pytesseract.image_to_string(image)

# Print or process the extracted text
print(extracted_text)
