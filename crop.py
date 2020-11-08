# Improting Image class from PIL module 
from PIL import Image 
  
# Opens a image in RGB mode 
im = Image.open(r"Screenshot_20.jpg") 
  
# Size of the image in pixels (size of orginal image) 
# (This is not mandatory) 
width, height = im.size 

print(width, height)
  
# Setting the points for cropped image 
left = 0
top = 780
right = 1080
bottom = 1890
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 
im1.save(r'/home/silver/Desktop/test/s2.png')
  
# Shows the image in image viewer 
im1.show() 