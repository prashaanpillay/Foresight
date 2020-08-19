from engine.src.structure.model.Model import Model


class DatasetModel(Model):

    def __init__(self):
        self.training_directory = ""
        self.validation_directory = ""
        self.training_generator = None

    def update(self, config):
        pass
