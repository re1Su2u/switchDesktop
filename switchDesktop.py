import tkinter as tk
import tkinter.ttk as ttk
import pyautogui as pgui
import win32gui
import win32con
import win32api

def switchLeft():
    pgui.hotkey('ctrl', 'win', 'left')

def switchRight():
    pgui.hotkey('ctrl', 'win', 'right')

def appearOnAllDesktop():
    windowTopMost()

    global frameFix
    frameFix.destroy()

    createSwitcher()

def windowTopMost():
    p_hWnd = win32gui.FindWindow(None,"DeskTop Switcher")
    win32gui.SetWindowPos(p_hWnd,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def createSwitcher():
    global root
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, pady=20)

    textLeft = tk.StringVar(frame)
    textLeft.set("<")
    buttonLeft = tk.Button(frame, textvariable=textLeft, command=switchLeft)
    buttonLeft.pack(fill='x', padx=40, side='left')

    textRight = tk.StringVar(frame)
    textRight.set(">")

    buttonRight = tk.Button(frame, textvariable=textRight, command=switchRight)
    buttonRight.pack(fill='x', padx=40, side='right')


root = tk.Tk()
root.title("DeskTop Switcher")
root.geometry("250x100")

frameFix = ttk.Frame(root)
frameFix.pack(fill=tk.BOTH, pady=20)

textFix = tk.StringVar(frameFix)
textFix.set('Fix the app')
buttonFix = tk.Button(frameFix, textvariable=textFix, command=appearOnAllDesktop)
buttonFix.pack()

root.mainloop()