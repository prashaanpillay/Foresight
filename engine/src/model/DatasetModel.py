from engine.src.structure.model.Model import Model


class DatasetModel(Model):

    # TODO: add another model for the actual learning model stuff

    def __init__(self):
        self.training_directory = ""
        self.validation_directory = ""

        self.training_dataset = None
        self.validation_dataset = None

        self.preprocessing_color_map = {}
        self.data_type = None
    
    def set_data_type(self, data_type):
        self.data_type = data_type

    # Over time this tracks what color space we are actually working with.
    def set_preprocessing_color_map(self, preprocessing_technique, color=""):
        self.training_directory = directory

    def set_training_directory(self, directory):
        self.training_directory = directory

    def set_validation_directory(self, directory):
        self.validation_directory = directory

    def set_training_dataset(self, dataset):
        self.training_dataset = dataset

    def set_validation_dataset(self, dataset):
        self.validation_dataset = dataset
