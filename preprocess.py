from __future__ import annotations
from typing import List

from PIL import Image as p_img


class Image:
    def __init__(
        self,
        *,
        input_dir_path: str,
        output_dir_path: str,
    ):
        self._input_dir_path: str = input_dir_path
        self._output_dir_path: str = output_dir_path

    def preprocess(
        self,
        *,
        input_files: List[str],
    ):
        try:
            for file in input_files:
                resized_image_instance = self.resize(file)
                self._save(resized_image_instance, file)
            return True
        except Exception:
            return False

    def resize(
        self,
        input_file: str,
        *,
        width: int = 128,
        height: int = 128,
    ):
        image = p_img.open(f"{self._input_dir_path}/{input_file}")
        resized_image_instance = image.resize((width, height))
        return resized_image_instance

    def _save(
        self,
        resized_image_instance,
        output_file: str
    ):
        resized_image_instance.save(f"{self._output_dir_path}/{output_file}")
