import time
import cv2
import numpy as np 
import pyautogui
from PIL import Image 
from pytesseract import pytesseract 
from pynput import mouse

# Defining paths to tesseract.exe 
path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
# Providing the tesseract executable 
# location to pytesseract library 
pytesseract.tesseract_cmd = path_to_tesseract 

# Take screenshot by giving two points of text rect
xPos, yPos = (0, 0)
xEndPos, yEndPos = (0, 0)
count = 0

def on_click(x, y, button, pressed):
    global xPos, yPos
    global xEndPos, yEndPos
    global count

    if str(button) != "Button.left":
        return
    if pressed:
        count = count + 1
        print(f"position {count} saved")
        if count == 1:
            xPos, yPos = x, y
        else:
            xEndPos, yEndPos = x, y

    if count > 1:
        mouse.Listener.stop(listener)

with mouse.Listener(on_click=on_click) as listener:
    listener.join()

image = pyautogui.screenshot(region=(xPos, yPos, xEndPos - xPos, yEndPos - yPos))
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 
cv2.imwrite("image/text.png", image)

# Read Text Image
image_path = r"image\text.png"
img = Image.open(image_path) 

# Extract text from image
text = pytesseract.image_to_string(img) 
text = text.replace("\n", " ")
print(text[:-1])

# Click input to start typing
input("Ready! click to start typing")
time.sleep(.5)

# Split text to words to write
words = text.split(" ")
for word in words:
    if word != "":
        time.sleep(0.1)
        pyautogui.typewrite(word)
        pyautogui.typewrite(" ")
