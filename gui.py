# Control-Q (when cursor is on function name) brings up a box with the function definition
# Control-P (when cursor inside function call "()") shows a list of parameters and their default values

import PySimpleGUI as sg


# Popups and guessing are suppressed, just getting an exception by key error
sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=True, suppress_key_guessing=True)
# setting color of the window
sg.theme('Dark Blue 3')

layout = [[sg.Text('History:')],
          [sg.Listbox(values=('test1', 'test2'), size=(30, 7)),
           sg.Frame('Information', [
               [sg.Text('Current Pic:')],
               [sg.Text('Hello', size=(35, 1), key='-OUTPUT-')],
               [sg.Text('Selected Timer:'), sg.Text('Pic switches in:')],
               [sg.Input(size=(13, 1), key='-IN-'), sg.Text('Hello', size=(15, 1), key='-OUTPUT1-')]
           ])],
          [sg.Text('_' * 77)],
          [sg.Text('Choose your path:')],
          [sg.Input(size=(30, 1), key='-IN1-'), sg.Button('Start', tooltip='Press this Button to start'),
           sg.Button('Exit', )]]

window = sg.Window('WallpaperEngine', layout, grab_anywhere=True)

while True:  # Event Loop
    event, values = window.read()
    # print(event, values) this statement shows the values of each input element
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Start':
        # the '-output-' element gets the value(s) of '-in-' element
        window['-OUTPUT-'].update(values['-IN-'])
        # val = values['-IN-']


window.close()
del window
