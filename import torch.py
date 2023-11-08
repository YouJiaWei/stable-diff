import PySimpleGUI as sg

layout = [[sg.Text('text1'), sg.Text('text2')],
          [sg.Text('text3'), sg.Text('text4')]]

window = sg.Window("Windows", layout=layout, default_element_size=(70, 32), auto_size_text=False)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()