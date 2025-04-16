import tkinter
from PIL import ImageTk, Image
from os import listdir
from os.path import isfile, join
from ImageLabelingApp.DatasetCreator import DatasetCreator

class ImageLabelerApp:
    input_images_path = "../Images/output/"
    labels = ["object_present", "object_not_present"]

    def __init__(self, master):
        self.master = master
        self.master.title("Image Labeler")

        self.dataset_creator = DatasetCreator(dataset_output_path="./output/", dataset_output_name="labeled_images.json")

        all_filenames = [file for file in listdir(self.input_images_path) if isfile(join(self.input_images_path, file))]
        self.all_images = [ImageTk.PhotoImage(Image.open(self.input_images_path + file_name)) for file_name in all_filenames]

        self.current_index = 0
        self.image_label = tkinter.Label(master, image=self.all_images[self.current_index])
        self.image_label.pack(pady=10)

        for label in self.labels:
            button = tkinter.Button(master, text=label, command=lambda l=label: self.label_image(l, all_filenames[self.current_index]))
            button.pack(side=tkinter.LEFT, padx=10)

    def label_image(self, label: str, image_name: str):
        self.dataset_creator.add_to_dataset(image_path=image_name, label=label)
        print(f"Labeled {image_name} as {label}")
        self.show_next_image()

    def show_next_image(self):
        self.current_index += 1
        if self.current_index < len(self.all_images):
            self.image_label.config(image=self.all_images[self.current_index])
        else:
            print("All images labeled. Exporting dataset...")
            self.dataset_creator.save_dataset_as_json()
            self.master.quit()

if __name__  =="__main__":
    root = tkinter.Tk()
    app = ImageLabelerApp(root)
    root.mainloop()