import json

class DatasetCreator:
    def __init__(self, dataset_output_path: str, dataset_output_name: str):
        self.dataset = []
        self.dataset_output_path = dataset_output_path
        self.dataset_output_name = dataset_output_name

    def add_to_dataset(self,  image_path: str, label : str) -> None:
        self.dataset.append((image_path, label))

    def save_dataset_as_json(self) -> None:
        with open(f"{self.dataset_output_path}/{self.dataset_output_name}", "w") as file:
            file.write('{ "dataset" : [\n')
            for i, (image_path, label) in enumerate(self.dataset):
                json_data = {
                    "image_path": image_path,
                    "label": label
                }
                file.write(json.dumps(json_data))
                if i < len(self.dataset) - 1:
                    file.write(",\n")
                else:
                    file.write("\n")
            file.write("]}")
