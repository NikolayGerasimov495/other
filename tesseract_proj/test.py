import cv2
import pytesseract
from PIL import Image

# img = Image.open('phone_number.png')
# img = Image.open('avito_page.png')
# img = Image.open('eng_text.png')
# img = Image.open('img2.jpg')
img = Image.open('rus_text.png')

# custom_config = r'--oem 3 --psm 13'
# custom_config = r'--oem 3 --psm 6'


text = pytesseract.image_to_string(img, lang='rus')
print(text)

# with open('img2_text.txt', 'w') as text_file:e
#     text_file .write(text)

#
# img = cv2.imread('rus_text.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# custom_config = r'--oem 3 --psm 6'
#
#
# data = pytesseract.image_to_data(img, lang='rus')
# for i, el in enumerate(data.splitlines()):
#     if i == 0:
#         continue
#
#     el = el.split()
#     try:
#         x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
#         cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
#         cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 1)
#     except IndexError:
#         print("Операция была пропущена")
# cv2.imshow('Result', img)
# cv2.waitKey(0)


