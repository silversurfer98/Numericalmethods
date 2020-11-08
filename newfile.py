from PIL import Image
import pytesseract
import numpy as np
import pyautogui
import tkinter as tk


def takeScreenshot ():
    myScreenshot = pyautogui.screenshot()
    # myScreenshot.save(r'/home/silver/Desktop/test/s.png')
    # im = Image.open("sample1.png")
    return(myScreenshot)

im = takeScreenshot()


tleft = 285
ttop = 180
tright = tleft + 90 
tbottom = ttop + 90
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im2 = im.crop((tleft, ttop, tright, tbottom)) 
ocr_total = pytesseract.image_to_string(im2, config = " --oem 3 --psm 12  -c tessedit_char_whitelist=0123456789")


ll = 78
lll = 50
left = 265
top = 430
right = left + lll
bottom = top + lll

arr = []
arr1=[]
for y in range(6):
    left = 265
    right = left + lll
    for x in range(6):
        im1 = im.crop((left, top, right, bottom))
        #im1.show()
        ocr_result = pytesseract.image_to_string(im1, config = "--oem 3 --psm 6  -c tessedit_char_whitelist=0123456789")
        left = left + ll
        right = right + ll
        
        item = str(ocr_result)

        if(item == 'l\n\x0c'):
            item = '1'
        elif(item == 'б\n\x0c'):
            item = '6'
        elif(item == '\x0c'):
            item = '0'
        arr.append(item)

    top = top + ll
    bottom = bottom + ll

arr = np.array(arr, dtype='int')
ocr_total=int(str(ocr_total))
#ocr_total = np.array(str(ocr_total), dtype='int')
print(arr)
print(np.sum(arr))
print(ocr_total)
total=0

if(np.sum(arr)>=ocr_total):
    for z in range(36):
        
        if(arr[35-z]==0):
            arr1.append(0)
        elif((total+arr[35-z])<=ocr_total):
            total=total+arr[35-z]
            arr1.append(1)
        else:
            arr1.append(0)
    arr1=np.flipud(arr1)
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



ll = 78
lll = 50
left = 265
top = 430
right = left + lll
bottom = top + lll
i=0
for y in range(6):
    left = 265
    right = left + lll

    for x in range(6):
        if(arr1[i]==1):
            pyautogui.click((left+(lll/2)),(top+(lll/2)))
        #print(arr2[i],(left+(lll/2)),(top+(lll/2)))
        left = left + ll
        right = right + ll
        i=i+1
        

    top = top + ll
    bottom = bottom + ll



