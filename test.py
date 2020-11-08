import pyautogui
import tkinter as tk
from PIL import Image
import pytesseract
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 30, height = 30)
canvas1.pack()

def takeScreenshot ():
    
    myScreenshot = pyautogui.screenshot()
    # myScreenshot.save(r'/home/silver/Desktop/test/s.png')
    # im = Image.open("sample1.png")
    text = pytesseract.image_to_string(myScreenshot, lang = 'eng')
    print(text)

myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green',fg='white',font= 10)
canvas1.create_window(40, 40, window=myButton)

root.mainloop()
