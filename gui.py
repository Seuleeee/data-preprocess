import os.path
from typing import List

import PySimpleGUI as sg

from preprocess import Image

KEY_FOLDER = "-FOLDER-"
KEY_FILELIST = "-FILE LIST-"
KEY_TOUT = "-TOUT-"
KEY_IMAGE = "-IMAGE-"


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
        sg.Button(
            "Resize Images",
            enable_events=True,
            key="RESIZE",
        ),
    ],
]

image_viewer_column = [
    [sg.Text("Choose an image from list on left: ")],
    [sg.Text(size=(40, 1), key=KEY_TOUT)],
    [sg.Image(key=KEY_IMAGE)],
]

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

window = sg.Window("Image Viewer", layout)


input_dir_path: str = ''
output_dir_path: str = ''

while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    else:
        if event == "INPUT-DIR":
            input_dir_path = values.get(event)
        elif event == "OUTPUT-DIR":
            output_dir_path = values.get(event)
        elif event == "RESIZE":
            input_files: List[str] = os.listdir(input_dir_path)
            print("test", input_files)
            image_preprocess = Image(
                input_dir_path=input_dir_path,
                output_dir_path=output_dir_path,
            )
            image_preprocess.preprocess(input_files=input_files)

window.close()
