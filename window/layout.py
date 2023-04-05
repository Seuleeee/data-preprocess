from typing import (
    Any,
    List,
    Generic,
    TypeVar,
    Type,
)
from enum import (
    Enum,
    IntEnum,
)

import PySimpleGUI as sg


SimpleGuiType = TypeVar("SimpleGuiType")


class BaseEnum(Enum):
    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class ComponentKey(BaseEnum):
    input_dir: str = "INPUT-DIR"
    output_dir: str = "OUTPUT-DIR"
    combobox: str = "COMBOBOX"
    run_preprocess: str = "RUN-PREPROCESS"
    resize_width: str = "RESIZE-WIDTH"
    resize_height: str = "RESIZE-HEIGHT"
    flip_direction: str = "FLIP-DIRECTION"
    rotate_angle: str = "ROTATE-ANGLE"
    progress: str = "PROGRES"


class Preprocess(BaseEnum):
    flip: str = "Flip"
    resize: str = "Resize"
    rotate: str = "Rotate"


class DisplayOptions(BaseEnum):
    width: str = "Width"
    height: str = "Height"
    rotate_angle: str = "Rotate Angle(degree)"
    flip_direction: str = "Select Flip Direction"


class DisplayName(BaseEnum):
    input_dir: str = "Input Image Directory"
    output_dir: str = "Output Image Directory"
    combobox: str = "Select Preprocessing Algorithm"
    run_preprocess: str = "Run Preprocess"
    progress: str = "Progress..."


class Rows(list, Enum):
    input_dir: List[SimpleGuiType] = [
        sg.Text(DisplayName.input_dir),
        sg.In(
            size=(25, 1),
            enable_events=True,
            key=ComponentKey.input_dir,
        ),
        sg.FolderBrowse(initial_folder="~/"),
    ]

    output_dir: List[Any] = [
        sg.Text(DisplayName.output_dir),
        sg.In(
            size=(25, 1),
            enable_events=True,
            key=ComponentKey.output_dir,
        ),
        sg.FolderBrowse(initial_folder="~/"),
    ]

    preprocess_combo: List[Any] = [
        sg.Text(DisplayName.combobox),
        sg.Combo(
            Preprocess.list(),
            default_value=Preprocess.resize,
            enable_events=True,
            key=ComponentKey.combobox,
        )
    ]

    resize_options: List[Any] = [
        sg.Text(DisplayOptions.width),
        sg.In(
            size=(5, 1),
            enable_events=True,
            key=ComponentKey.resize_width,
        ),
        sg.Text(DisplayOptions.height),
        sg.In(
            size=(5, 1),
            enable_events=True,
            key=ComponentKey.resize_height,
        ),
    ]

    rotate_options: List[Any] = [
        sg.Text(DisplayOptions.rotate_angle),
        sg.In(
            size=(5, 1),
            enable_events=True,
            key=ComponentKey.rotate_angle,
        ),
    ]

    flip_options: List[Any] = [
        sg.Text(DisplayOptions.flip_direction),
        sg.In(
            size=(10, 1),
            enable_events=True,
            key=ComponentKey.flip_direction,
        ),
    ]

    progress: List[Any] = [
        sg.Text(DisplayName.progress),
        sg.Text(
            "Waiting",
            size=(40, 1),
            key=ComponentKey.progress,
        )
    ]

    run_preprocess_button: List[Any] = [
        sg.Button(
            DisplayName.run_preprocess,
            enable_events=True,
            key=ComponentKey.run_preprocess,
        ),
    ]
