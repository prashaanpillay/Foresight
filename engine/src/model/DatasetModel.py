from engine.src.structure.model.Model import Model


class DatasetModel(Model):

    def __init__(self, injector):
        super().__init__(injector=injector)
        self.training_directory = ""
        self.validation_directory = ""

    def set_training_directory(self, directory):
        self.training_directory = directory

    def set_validation_directory(self, directory):
        self.validation_directory = directory
