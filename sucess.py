from PIL import Image
import pytesseract
import numpy as np

im = Image.open("Screenshot_20.jpg")


left = 120
top = 260
right = 280
bottom = 420
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im2 = im.crop((left, top, right, bottom)) 
ocr_total = pytesseract.image_to_string(im2, config = " --oem 3 --psm 12  -c tessedit_char_whitelist=0123456789")

left = 40
top = 820
right = 140
bottom = 940

arr = []
arr1=[]
for y in range(6):
    left = 40
    right = 140
    for x in range(6):
        im1 = im.crop((left, top, right, bottom))
        
        ocr_result = pytesseract.image_to_string(im1, config = "--oem 3 --psm 6  -c tessedit_char_whitelist=0123456789")
        left = left + 180
        right = right + 180
        
        item = str(ocr_result)

        if(item == 'l\n\x0c'):
            item = '1'
        elif(item == 'б\n\x0c'):
            item = '6'
        elif(item == '\x0c'):
            item = '0'
        arr.append(item)

    top = top + 180
    bottom = bottom +180

arr = np.array(arr, dtype='int')
ocr_total=int(str(ocr_total))
#ocr_total = np.array(str(ocr_total), dtype='int')
print(arr)
print(np.sum(arr))
print(ocr_total)

total=0

if(np.sum(arr)>=ocr_total):
    for z in range(len(arr)):
        
        if(arr[len(arr)-z-1]==0):
            arr1.append(0)
        elif((total+arr[len(arr)-z-1])<=ocr_total):
            total=total+arr[len(arr)-z-1]
            arr1.append(1)
        else:
            arr1.append(0)
    
    if(total<ocr_total):
        total=0
        arr1=[]
        for z in range(len(arr)):
        
            if(arr[z]==0):
                arr1.append(0)
            elif((total+arr[z])<=ocr_total):
                total=total+arr[z]
                arr1.append(1)
            else:
                arr1.append(0)
arr1 = np.array(arr1, dtype='int')       
print(total)
print(arr1)