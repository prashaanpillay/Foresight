from engine.src.structure.model.Model import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# model.fit(
#         train_generator,
#         steps_per_epoch=2000,
#         epochs=50,
#         validation_data=validation_generator,
#         validation_steps=800)

class DatasetModel(Model):

    def __init__(self):
        self.training_directory = ""
        self.validation_directory = ""

        self.training_dataset = None
        self.validation_dataset = None

        self.training_generator = ImageDataGenerator(rescale=1./255,
                                                    shear_range=0.2,
                                                    zoom_range=0.2,
                                                    horizontal_flip=True)
        self.validation_generator = ImageDataGenerator(rescale=1./255)

    def set_training_directory(self, directory):
        self.training_directory = directory

    def set_validation_directory(self, directory):
        self.validation_directory = directory

    def set_training_dataset(self, dataset):
        self.training_dataset = dataset

    def set_validation_dataset(self, dataset):
        self.validation_dataset = dataset