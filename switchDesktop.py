import tkinter as tk
import tkinter.ttk as ttk
import pyautogui as pgui
import win32gui
import win32con

def switchLeft():
    pgui.hotkey('ctrl', 'win', 'left')

def switchRight():
    pgui.hotkey('ctrl', 'win', 'right')

def appearOnAllDesktop():
    p_hWnd = win32gui.FindWindow(None,"DeskTop Switcher")
    windowTopMost(p_hWnd)

    pgui.hotkey('win', 'tab')

    win32gui.SetActiveWindow(p_hWnd)

    

    global frameFix
    frameFix.destroy()

    createSwitcher()

def windowTopMost(p_hWnd):
    win32gui.SetWindowPos(p_hWnd,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def createSwitcher():
    global root
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, pady=20)

    text_left = tk.StringVar(frame)
    text_left.set("<")
    button_left = tk.Button(frame, width=10, textvariable=text_left, command=switchLeft)
    button_left.pack(fill='x', padx=20, side='left')

    text_right = tk.StringVar(frame)
    text_right.set(">")

    button_right = tk.Button(frame, width=10, textvariable=text_right, command=switchRight)
    button_right.pack(fill='x', padx=20, side='right')


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