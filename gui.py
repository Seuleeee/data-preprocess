import os.path
from typing import List

import PySimpleGUI as sg

from preprocess import Image


KEY_FILELIST = "-FILE LIST-"
KEY_TOUT = "-TOUT-"
KEY_IMAGE = "-IMAGE-"

# window 내부에 layout 만들고
# while 문은 run 으로 뺌

file_list_column = [
    [
        sg.Text("Input Image Directory"),
        sg.In(
            size=(25, 1),
            enable_events=True,
            key="INPUT-DIR",
        ),
        sg.FolderBrowse(initial_folder="~/"),
    ],
    [
        sg.Text("output Image Directory"),
        sg.In(
            size=(25, 1),
            enable_events=True,
            key="OUTPUT-DIR",
        ),
        sg.FolderBrowse(initial_folder="~/"),
    ],
    [
        sg.Text("Select Preprocessing Algorithm"),
        sg.Combo(
            ["Flip", "Resize", "Rotate"],
            default_value="Resize",
            enable_events=True,
            key="COMBO",
        )
    ],
    [
        sg.Button(
            "Run Preprocess",
            enable_events=True,
            key="PREPROCESS",
        ),
    ],
]

image_viewer_column = [
    [sg.Text("Preprocessing")],
    [sg.Text("waiting...", size=(40, 1), key=KEY_TOUT)],
    [sg.Image(key=KEY_IMAGE)],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Data Preprocessor", layout)


input_dir_path: str = ''
output_dir_path: str = ''
preprocess_algorithm: str = ''

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    else:
        if event == "INPUT-DIR":
            input_dir_path = values.get(event)
        elif event == "OUTPUT-DIR":
            output_dir_path = values.get(event)
        elif event == "COMBO":
            preprocess_algorithm: str = values.get(event)
            if preprocess_algorithm == "Resize":
                pass
        elif event == "PREPROCESS":
            input_files: List[str] = os.listdir(input_dir_path)
            image_preprocess = Image(
                input_dir_path=input_dir_path,
                output_dir_path=output_dir_path,
            )
            result: bool = image_preprocess.preprocess(input_files=input_files)
            if result:
                window[KEY_TOUT].update("Complete!!!")


window.close()
