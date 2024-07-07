import tkinter as tk
import tkinter.ttk as ttk
import pyautogui as pgui
import win32gui
import win32con

def switch_left():
    pgui.hotkey('ctrl', 'win', 'left')

def switch_right():
    pgui.hotkey('ctrl', 'win', 'right')

def appear_on_all_desktop():
    p_hWnd = win32gui.FindWindow(None,"DeskTop Switcher")
    window_top_most(p_hWnd)

    pgui.hotkey('win', 'tab')

    win32gui.SetActiveWindow(p_hWnd)

    

    global frame_fix
    frame_fix.destroy()

    create_switcher()

def window_top_most(p_hWnd):
    win32gui.SetWindowPos(p_hWnd,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)


def create_switcher():
    global root
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, pady=20)

    text_left = tk.StringVar(frame)
    text_left.set("<")
    button_left = tk.Button(frame, width=10, textvariable=text_left, command=switch_left)
    button_left.pack(fill='x', padx=20, side='left')

    text_right = tk.StringVar(frame)
    text_right.set(">")

    button_right = tk.Button(frame, width=10, textvariable=text_right, command=switch_right)
    button_right.pack(fill='x', padx=20, side='right')


root = tk.Tk()
root.title("DeskTop Switcher")
root.geometry("250x100")

frame_fix = ttk.Frame(root)
frame_fix.pack(fill=tk.BOTH, pady=20)

text_fix = tk.StringVar(frame_fix)
text_fix.set('Fix the app')
button_fix = tk.Button(frame_fix, textvariable=text_fix, command=appear_on_all_desktop)
button_fix.pack()

root.mainloop()