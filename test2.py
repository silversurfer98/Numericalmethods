from PIL import Image
import pytesseract
import numpy as np
import pyautogui
import tkinter as tk


def noway():
    root= tk.Tk()
    canvas1 = tk.Canvas(root, width = 30, height = 30)
    canvas1.pack()
    myButton = tk.Button(text='Take Screenshot', command=takeScreenshot, bg='green',fg='white',font= 10)
    canvas1.create_window(40, 40, window=myButton)
    root.mainloop()

def takeScreenshot ():
    myScreenshot = pyautogui.screenshot()
    # myScreenshot.save(r'/home/silver/Desktop/test/s.png')
    # im = Image.open("sample1.png")
    return(myScreenshot)
    print("sucess")

noway()