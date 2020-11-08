from PIL import Image
import pytesseract
import numpy as np

im = Image.open("Screenshot_20.jpg")


left = 40
top = 820
right = 140
bottom = 940
#top = 1000
#bottom = 1120
#top = 1180
#bottom = 1300
# m = 6
# n = 6
  
# a = [[ocr_result for i in range(y)] for i in range(x)]

# arr = np.array(36, dtype = 'string')
arr = []

for y in range(6):
    left = 40
    right = 140
    for x in range(6):
        im1 = im.crop((left, top, right, bottom))
        #im1.show() 
        #ocr_result = pytesseract.image_to_string(im1, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
        ocr_result = pytesseract.image_to_string(im1, config = " -l osd --oem 3 --psm 6 ")
        # print(ocr_result)
        left = left + 180
        right = right + 180
        
        item = str(ocr_result)
        if(item == 'l\n\x0c'):
            # print("im here")
            item = '1'
        elif(item == 'б\n\x0c'):
            item = '6'
        elif(item == '\x0c'):
            item = '0'
        arr.append(item)
        # print(item)        
    top = top + 180
    bottom = bottom +180


arr = np.array(arr, dtype='int')
print(arr)
print(np.sum(arr))
