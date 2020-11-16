import winreg
import win32gui
import win32con
from win32api import GetSystemMetrics
import os
from random import randrange
from PIL import Image

# https://auth0.com/blog/image-processing-in-python-with-pillow/
# https: // pypi.org / project / python - resize - image /


def get_screen_width():
    return GetSystemMetrics(0)


def get_screen_height():
    return GetSystemMetrics(1)


def check_path(given_path):
    # checks if access to given path is allowed
    if os.access(given_path, os.F_OK and os.R_OK):
        print("Access to: " + given_path + " " + "allowed")
        return True
    else:
        print("No access")
        return False


def select_pics_in_path(given_path):
    path_contains_items = os.listdir(given_path)
    picture_list = []

    for possible_picture in path_contains_items:
        if possible_picture[-4:] == ".jpg" or possible_picture[-4:] == ".png":
            picture_list.append(possible_picture)

    length_picture_list = len(picture_list)

    num = random_number(length_picture_list)
    return picture_list[num]


def random_number(length_picture_list):
    num = randrange(1, length_picture_list)
    return num


def create_resized_image_folder():
    # contains the path to desktop on windows
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    desktop = desktop + "\\" + "WallpaperEngine_ResizedImages"
    if not os.access(desktop, os.F_OK):
        os.mkdir(desktop, os.R_OK and os.W_OK)

    return desktop


def picture_resizing(picture_path):
    folder = create_resized_image_folder()
    # picture is the same variable as new_path
    image = Image.open(picture_path)
    image.thumbnail((get_screen_width(), get_screen_height()))
    os.chdir(folder)
    image.save("Wallpaper.png")


def set_wallpaper(new_path):
    key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_SET_VALUE)
    winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, "0")
    winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, new_path, 1 + 2)


def run_engine(given_path):
    if check_path(given_path):
        current_picture = select_pics_in_path(given_path)
        new_path = given_path + "\\" + current_picture
        picture_resizing(new_path)
        set_wallpaper(create_resized_image_folder() + "\\" + "Wallpaper.png")
        return current_picture
