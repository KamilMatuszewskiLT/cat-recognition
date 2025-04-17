import os
import ImageEditorBuilder
from PIL import Image

class ImagePreparer:
    @staticmethod
    def prepare_images(input_images: list, output_path: str, resize_to_width: int, remove_input=False) -> None:
        image_editor = ImageEditorBuilder.ImageEditorBuilder()

        for file in input_images:
            image = Image.open(file)

            # Perform image processing here
            converted_image = (
                image_editor.set_image(image)
                            .convert_to_grayscale()
                            .resize_image_keep_ratio(resize_to_width)
                            .get_image()
            )

            # Save the processed image and optionally remove the input file
            converted_image.save(os.path.join(output_path, os.path.basename(file)))
            if remove_input:
                os.remove(file)
