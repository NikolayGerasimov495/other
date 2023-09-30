import cv2
import pytesseract


img = cv2.imread('img2.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(img, lang='rus', config=custom_config)
print(text)