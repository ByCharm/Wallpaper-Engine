import winreg, win32gui, win32con
import os
from random import randrange

copy_num = -1

def check_path(path):
    # checks if access to given path is allowed
    try:
        if os.access(path, os.F_OK and os.R_OK):
            print("Access to: " + path + " " + "allowed")
    except FileNotFoundError:
        print("No access")


def select_pics_in_path(path):
    # stores all the given items at path in list
    path_items = os.listdir(path)
    pic_list = []

    # returns a list with all pics from given path
    for x in path_items:
        if x[-4:] == ".jpg" or x[-4:] == ".png":
            pic_list.append(x)

    # random_num produces a num -> using this num to access a pic in pic_list
    num = random_num(len(pic_list), copy_num)
    return pic_list[num]


def random_num(len_list,copy_num):
    num = randrange(0, len_list, 1)
    if num != copy_num:
        copy_num = num
        return num
    else:
        while(num == copy_num):
            random_num(len_list, copy_num)


def set_wallpaper(new_path):
    key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "0")
    winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, new_path, 1 + 2)


if __name__ == '__main__':
    path = r'C:\Users\Franz\Desktop\test'
    new_path = path + "\\" + select_pics_in_path(path)
    set_wallpaper(new_path)
    print("Current picture: " + select_pics_in_path(path))
