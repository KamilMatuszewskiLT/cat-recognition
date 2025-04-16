from typing import Self
from PIL import Image

class ImageEditorBuilder:
    image: Image.Image

    def set_image(self, image: Image.Image) -> Self:
        self.image = image
        return self

    def convert_to_grayscale(self) -> Self:
        self.image = self.image.convert('L')
        return self

    def resize_image(self, result_size_in_pixels: tuple[int, int]) -> Self:
        self.image = self.image.resize(result_size_in_pixels)
        return self

    def get_image(self) -> Image.Image:
        return self.image
