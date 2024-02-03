import time
import pyautogui
from PIL import Image 
from pytesseract import pytesseract 

# Defining paths to tesseract.exe 
path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
# Providing the tesseract executable 
# location to pytesseract library 
pytesseract.tesseract_cmd = path_to_tesseract 

image_path = r"image\text.png"
img = Image.open(image_path) 

# Extract text from image
text = pytesseract.image_to_string(img) 
text = text.replace("\n", " ")
print(text[:-1])

# Split text to words to write
words = text.split(" ")
for word in words:
    if word != "":
        time.sleep(0.1)
        pyautogui.typewrite(word)
        pyautogui.typewrite(" ")
