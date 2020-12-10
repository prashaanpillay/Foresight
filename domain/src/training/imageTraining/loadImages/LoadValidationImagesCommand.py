from engine.src.utility.logger.Logger import Logger
from engine.src.structure.command.Command import Command
from engine.src.model.DatasetModel import DatasetModel
from tensorflow.keras.preprocessing import image_dataset_from_directory


class LoadValidationImagesCommand(Command):

  def __init__(self):
    super().__init__()
    self.logger =  self.injector.get_instance(Logger)
    self.validation_dataset = None
    self.dataset_model = self.injector.get_instance(DatasetModel)
    self.validation_dataset_directory = self.dataset_model.validation_directory

  def execute(self):
    self.logger.log(str(self.validation_dataset_directory))
    self.validation_dataset = image_dataset_from_directory(
                                                        self.validation_dataset_directory,
                                                        seed=1337,
                                                        color_mode="grayscale",
                                                        image_size=(100,100),
                                                        batch_size=32,
                                                        )
    self.validation_dataset.prefetch(buffer_size=32)
    self.dataset_model.set_validation_dataset(self.validation_dataset)