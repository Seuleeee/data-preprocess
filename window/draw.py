from typing import (
    List,
    Any,
    Union,
)
from abc import ABC, abstractmethod

import PySimpleGUI as sg

from window.layout import (
    Rows,
    Preprocess,
)


class Window:
    def __init__(self):
        self.base_left: List[Any] = [
            Rows.input_dir,
            Rows.output_dir,
            Rows.preprocess_combo,
        ]
        self._base_right: List[Any] = [
            Rows.progress,
        ]

    def add_rows(
        self,
        *,
        preprocess: str = Preprocess.resize,
    ):
        if preprocess == "Resize":
            print(preprocess)
            self.base_left.append(Rows.resize_options)
        elif preprocess == "Rotate":
            print(preprocess)
            self.base_left.append(Rows.rotate_options)
        elif preprocess == "Flip":
            self.base_left.append(Rows.flip_options)
        else:
            self.base_left.append(Rows.resize_options)

    def _get_column_left(self):
        return self.base_left

    def get_layout(
        self,
        preprocess: str = Preprocess.resize
    ):
        self.add_rows(preprocess=preprocess)
        column_left: List[Any] = self.base_left
        column_right: List[Any] = self._base_right
        layout = [
            [
                sg.Column(column_left),
                sg.VSeparator(),
                sg.Column(column_right),
            ]
        ]
        return layout
