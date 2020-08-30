from tensorflow.keras.preprocessing.image import ImageDataGenerator
from engine.src.structure.command.Command import Command
from engine.src.model.DatasetImageGeneratorModel import DatasetImageGeneratorModel


class AugmentDatasetCommand(Command):

    def __init__(self):
        super().__init__()
        self.datasetImageGeneratorModel = self.injector.get_instance(
            DatasetImageGeneratorModel)

    def execute(self):
        train_dataGenerator = ImageDataGenerator(rescale=1./255,
                                                 shear_range=0.2,
                                                 zoom_range=0.2,
                                                 horizontal_flip=True)

        test_dataGenerator = ImageDataGenerator(rescale=1./255)

        self.datasetImageGeneratorModel.setImageDataGeneration(train_dataGenerator,
                                                               test_dataGenerator)
