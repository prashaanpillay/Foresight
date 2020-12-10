from engine.src.structure.model.Model import Model

# model.fit(
#         train_generator,
#         steps_per_epoch=2000,
#         epochs=50,
#         validation_data=validation_generator,
#         validation_steps=800)Z

class DatasetModel(Model):

##TODO: add another model for the actual learning model stuff

    def __init__(self):
        self.training_directory = ""
        self.validation_directory = ""

        self.training_dataset = None
        self.validation_dataset = None

    def set_training_directory(self, directory):
        self.training_directory = directory

    def set_validation_directory(self, directory):
        self.validation_directory = directory

    def set_training_dataset(self, dataset):
        self.training_dataset = dataset

    def set_validation_dataset(self, dataset):
        self.validation_dataset = dataset