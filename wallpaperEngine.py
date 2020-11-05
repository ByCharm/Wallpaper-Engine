import winreg
import win32gui, win32con
import os
from random import randrange
import time


def change_pic_after_time(given_path):
    # https://docs.python.org/3/library/threading.html
    # time.sleep(10) this function will freeze the gui - not recommended to use
    # implementing two different threads - t1 will handle wallpaper engine and t2 will handle the gui
    run_engine(given_path)


def check_path(given_path):
    # checks if access to given path is allowed
    if os.access(given_path, os.F_OK and os.R_OK):
        print("Access to: " + given_path + " " + "allowed")
        return True
    else:
        print("No access")
        return False


def select_pics_in_path(given_path):
    # stores all the given items at path in list
    path_items = os.listdir(given_path)
    picture_list = []

    for possible_picture in path_items:
        if possible_picture[-4:] == ".jpg" or possible_picture[-4:] == ".png":
            picture_list.append(possible_picture)

    # random_num produces a num -> using this num to access a pic in pic_list
    length_picture_list = len(picture_list)
    num = random_number(length_picture_list)
    return picture_list[num]


def random_number(length_picture_list):
    num = randrange(1, length_picture_list)
    return num


def set_wallpaper(new_path):
    key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "0")
    winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, new_path, 1 + 2)


def run_engine(given_path):
    if check_path(given_path):
        # new_path contains the picture that set_wallpaper will show
        new_path = given_path + "\\" + select_pics_in_path(given_path)
        set_wallpaper(new_path)


# if __name__ == '__main__':
    # path = r'C:\Users\Franz\Desktop\pics'
    # change_pic_after_time(path)
