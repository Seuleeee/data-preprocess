import PySimpleGUI as sg

from window.draw import Window

from window.layout import (
    ComponentKey,
)

layout = Window().get_layout()
window = sg.Window("Image Preprocess", layout)
window.read()
#
#
# while True:
#     event, values = window.read()
#     if event is None or event == 'Exit':
#         break
#     if event == ComponentKey.combobox:
#         window.close()
#         preprocess = values.get(event)
#         window_temp = sg.Window("Image Preprocess", layout)
#
#         window = window_temp
#
# window.close()
