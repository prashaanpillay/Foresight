from engine.src.utility.logger.Logger import Logger
from engine.src.structure.command.Command import Command
from engine.src.model.DatasetModel import DatasetModel
from tensorflow.keras.preprocessing import image_dataset_from_directory


class LoadTrainingImagesCommand(Command):

  def __init__(self):
    super().__init__()
    self.logger =  self.injector.get_instance(Logger)
    self.training_dataset = None
    self.dataset_model = self.injector.get_instance(DatasetModel)
    self.training_dataset_directory = self.dataset_model.training_directory

  def execute(self):
    self.training_dataset = image_dataset_from_directory(
                                                        self.training_dataset_directory,                                                        
                                                        seed=1337,
                                                        color_mode="grayscale",
                                                        image_size=(100,100),
                                                        batch_size=32,
                                                        )
    self.training_dataset.prefetch(buffer_size=32)
    self.dataset_model.set_training_dataset(self.training_dataset)