# Improting Image class from PIL module 
from PIL import Image 
import pytesseract
# Opens a image in RGB mode 
im = Image.open(r"Screenshot_20.jpg") 
  
# Size of the image in pixels (size of orginal image) 
# (This is not mandatory) 
width, height = im.size 

print(width, height)
  
# Setting the points for cropped image 
#left = 120
#top = 260
#right = 280
#bottom = 420

left = 0
top = 820
right = 1080
bottom = 950
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
#im1.save(r'/home/silver/Desktop/test/s2.png')
ocr_result = pytesseract.image_to_string(im1, config = "-l osd  --oem 3 --psm 12 -c tessedit_char_whitelist=0123456789")
#ocr_result = pytesseract.image_to_string(im, config='outputbase digits')

print(ocr_result)
  
# Shows the image in image viewer 
#im1.show() 