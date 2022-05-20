import cv2
import pytesseract
import os
import re


def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)

#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

directory = 'images'
src = ''
accounts = []
refined = []
for filename in os.scandir(directory):
    if filename.is_file():
        img = cv2.imread(filename.path)
        img = get_grayscale(img)
        img = thresholding(img)
        img = remove_noise(img)

        src = ocr_core(img)
        # pattern = '/(?<!\w)@\w+/'
        # result = re.findall(pattern, src)
        # print(result)
    # [accounts.append(word) for word in src.split() if word.startswith('@')]
    for word in src.split():
        if (word.startswith('@') and (word.rfind('4') < 0 or word.rfind('&') < 0)):
            accounts.append(word)
    break

print(accounts)
print(len(accounts))


# [refined.append(name) for name in accounts if len(name) < 3]

# print(refined)
# print(len(refined))


