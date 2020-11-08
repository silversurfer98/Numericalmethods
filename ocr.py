from PIL import Image
import pytesseract

im = Image.open("s2.png")


# Setting the points for cropped image 
# left = 5
# top = 785
# right = 175
# bottom = 960

# left = 30
# top = 820
# right = 160
# bottom = 940
  
# Cropped image of above dimension 
# (It will not change orginal image) 
#im1 = im.crop((left, top, right, bottom))
# text = pytesseract.image_to_string(im, lang='eng')

#c = "-c tessedit_char_whitelist=0123456789.:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz --psm 13 --oem 0"
ocr_result = pytesseract.image_to_string(im, config="-l osd)
#ocr_result = pytesseract.image_to_string(im, config='outputbase digits')

print(ocr_result)
 
  
# Shows the image in image viewer 
im.show() 