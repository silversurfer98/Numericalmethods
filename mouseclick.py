import pyautogui, sys
import numpy as np

def poi():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def move():
    pyautogui.moveTo(500, 100,0.5)  
    # moves mouse to X of 100, Y of 200 over 2 seconds
    pyautogui.click()

def clicklike():
    pyautogui.click(x=100, y=200)  
    # move to 100, 200, then click the left mouse button.


def clicklikewithargs():
    a=input("put x : ")
    b=input("put y : ")

    a=int(a)
    b=int(b)
    pyautogui.click(x=a, y=b)  
    # move to 100, 200, then click the left mouse button.


def randarr (s):
    arr=np.random.randint(2, size=s)
    return arr

def randclickonarr():
    s = input('enter arr size : ')
    s=int(s)
    arr=randarr(s)
    print(arr)
    for i in arr:
        if(arr[i]==1):
            clicklike()
        else:
            move()
    
#randclickonarr()
#clicklikewithargs()
poi()
