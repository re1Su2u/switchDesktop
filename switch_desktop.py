import tkinter as tk
from tkinter import ttk
import pyautogui as pgui
import win32gui
import win32con
import configparser
from pynput import mouse
from distutils.util import strtobool

# Define mouse handler
def on_move(x, y):
    return

def on_click(x, y, button, pressed):
    if pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    return

def get_click_coordinate():
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()
    x, y = pgui.position()
    return [x, y]

def fix_window():
    ds_hwnd = win32gui.FindWindow(None,"DeskTop Switcher")
    win32gui.SetWindowPos(ds_hwnd,win32con.HWND_TOPMOST,0,0,0,0,win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    win32gui.SetActiveWindow(ds_hwnd)
    pgui.hotkey('win', 'tab') # Open task view

    # click point coordinates
    fx, fy, sx, sy = 0, 0, 0, 0

    conf = read_config()
    ft_flg = strtobool(conf['flag']['first_time'])

    if ft_flg:
        first_cordinates = get_click_coordinate()
        fx, fy = first_cordinates[0], first_cordinates[1]
        conf['coordinates']['first_x'], conf['coordinates']['first_y'] = str(fx), str(fy)

        second_cordinates = get_click_coordinate()
        sx, sy = second_cordinates[0], second_cordinates[1]
        conf['coordinates']['second_x'], conf['coordinates']['second_y'] = str(sx), str(sy)

        conf['flag']['first_time'] = str('False')
        write_config(conf)
    else:
        fx, fy = int(conf['coordinates']['first_x']), int(conf['coordinates']['first_y'])
        sx, sy = int(conf['coordinates']['second_x']), int(conf['coordinates']['second_y'])
        root.after(1000)
        pgui.rightClick(fx, fy)
        root.after(1000)
        pgui.click(sx, sy)
    
    pgui.hotkey('win', 'tab') # Close task view

def read_config():
    conf = configparser.ConfigParser()
    conf.read('setting.conf', encoding='utf-8')
    return conf

def write_config(conf):
    with open("setting.conf", "w") as file:
        conf.write(file)

def create_control_panel(root):
    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, pady=20)

    text_left = tk.StringVar(frame)
    text_left.set("<")
    button_left = tk.Button(frame, width=10, textvariable=text_left, command=move_left)
    button_left.pack(fill='x', padx=20, side='left')

    text_right = tk.StringVar(frame)
    text_right.set(">")
    button_right = tk.Button(frame, width=10, textvariable=text_right, command=move_right)
    button_right.pack(fill='x', padx=20, side='right')

# Switch Desktop method
def move_left():
    pgui.hotkey('ctrl', 'win', 'left')
    pgui.hotkey('alt', 'tab')

def move_right():
    pgui.hotkey('ctrl', 'win', 'right')
    pgui.hotkey('alt', 'tab')


## Main ##
root = tk.Tk()
root.title("DeskTop Switcher")
root.geometry("250x100")
root.resizable(False, False)
root.after(50, fix_window)
create_control_panel(root)

root.mainloop()