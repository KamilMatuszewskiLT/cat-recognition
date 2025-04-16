import PIL
import sys
import json
import numpy
import tensorflow as tf

image_folder = "../output/"

def load_dataset(dataset_json_path: str) -> tuple[numpy.ndarray, numpy.ndarray]:
    dataset_json_file = open(dataset_json_path)
    dataset_json = json.load(dataset_json_file)

    dataset_images = []
    dataset_labels = []
    for record in dataset_json["dataset"]:
        image_name = record["image_path"]
        image_label = record["label"]
        loaded_image = load_image(image_folder + image_name)
        dataset_images.append(loaded_image)

        label = 1 if image_label == "object_present" else 0
        dataset_labels.append(label)

    return numpy.array(dataset_images), numpy.array(dataset_labels)

def load_image(image_path: str) -> numpy.ndarray:
    loaded_image = PIL.Image.open(image_path)
    image_as_array = numpy.array(loaded_image)
    image_as_array = image_as_array / 255.0
    return image_as_array

def run():
    class myCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self, epoch, logs={}):
            if (logs.get('accuracy') > 0.8):
                print("\nReached 80% accuracy so cancelling training!")
                self.model.stop_training = True

    callbacks = myCallback()
    (training_images, training_labels) = load_dataset("../../ImageLabelingApp/output/training_labeled_images.json")
    (test_images, test_labels) = load_dataset("../../ImageLabelingApp/output/test_labeled_images.json")

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(512, activation=tf.nn.relu),
        tf.keras.layers.Dense(2, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # numpy.set_printoptions(threshold=sys.maxsize)
    # print(training_labels[0])
    # print(training_images[0])
    # return

    model.fit(training_images, training_labels, epochs=10, callbacks=[callbacks])

    classifications = model.predict(test_images)
    for i, (classification, test_label) in enumerate(zip(classifications, test_labels)):
        print(f"Image {i}: Predicted: { 0 if classification[0] > classification[1] else 1}, Actual: {test_label}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


