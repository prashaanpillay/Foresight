from engine.src.structure.model.Model import Model
from engine.src.model.DatasetModel import DatasetModel


class DatasetImageGeneratorModel(Model):

    def __init__(self, injector):
        super().__init__(injector=injector)
        self.trainingDataGenerator = None
        self.validationDataGenerator = None
        self.dataset_model = self.injector.get_instance(DatasetModel)

    def setImageDataGeneration(self, train_dataGenerator, validation_dataGenerator):
        self.trainingDataGenerator = train_dataGenerator.flow_from_directory(self.dataset_model.training_directory,
                                                                             target_size=(
                                                                                 150, 150),
                                                                             batch_size=32,
                                                                             class_mode='binary')

        self.validationDataGenerator = validation_dataGenerator.flow_from_directory(self.dataset_model.validation_directory,
                                                                                    target_size=(
                                                                                        150, 150),
                                                                                    batch_size=32,
                                                                                    class_mode='binary')
