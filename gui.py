# Control-Q (when cursor is on function name) brings up a box with the function definition
# Control-P (when cursor inside function call "()") shows a list of parameters and their default values

import PySimpleGUI as sg
from WallpaperEngine.wallpaperEngine import *

# Popups and guessing are suppressed, just getting an exception by key error
sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=True, suppress_key_guessing=True)
# setting color of the window
sg.theme('Dark Blue 3')

listbox_array = []
previous_picture = ""

layout = [[sg.Text('History:')],
          [sg.Listbox(values=(), size=(30, 7), key='-LISTBOX-'),
           sg.Frame('Information', [
               [sg.Text('Current Picture:')],
               [sg.Text(size=(35, 1), key='-PICTURE_OUTPUT-')],
               # [sg.Text('Selected Timer:'), sg.Text('Picture switches in:')],
               # [sg.Input(size=(13, 1), key='-TIMER_INPUT-'), sg.Text('Hello', size=(15, 1), key='-TIMER_OUTPUT-')]
           ])],
          [sg.Text('_' * 77)],
          [sg.Text('Choose your path:')],
          [sg.Input(size=(30, 1), key='-PATH_INPUT-'), sg.Button('Start', tooltip='Press this Button to start'),
           sg.Button('Exit', )]]

window = sg.Window('WallpaperEngine', layout, grab_anywhere=False)

while True:  # Event Loop
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Start':
        user_input_path = values['-PATH_INPUT-']
        current_picture = run_engine(user_input_path)
        window['-PICTURE_OUTPUT-'].update(current_picture)

        if previous_picture == "":
            previous_picture = current_picture
        elif current_picture != previous_picture:
            if len(listbox_array) <= 20:
                listbox_array.append(previous_picture)
                window['-LISTBOX-'].update(listbox_array)
                previous_picture = current_picture
            else:
                listbox_array.clear()
                listbox_array.append(previous_picture)
                window['-LISTBOX-'].update(listbox_array)
                previous_picture = current_picture


window.close()
del window
