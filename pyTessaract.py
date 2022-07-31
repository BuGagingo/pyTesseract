import pytesseract
from PIL import Image


img = Image.open("second.jpeg")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

custom_config = r'--oem 3, --psm 6'

text = pytesseract.image_to_string(img)
print(text)

with open('text.txt', 'w') as text_file:
    text_file.write(text)