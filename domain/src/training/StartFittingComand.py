from engine.src.utility.logger.Logger import Logger
from engine.src.structure.command.Command import Command
from engine.src.model.DatasetModel import DatasetModel
from tensorflow.keras.utils import Sequence
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import sparse_categorical_crossentropy,categorical_crossentropy
from tensorflow.keras.callbacks import TensorBoard
import datetime

class StartFittingCommand(Command):

  def __init__(self):
    super().__init__()
    self.logger =  self.injector.get_instance(Logger)
    self.dataset_model = self.injector.get_instance(DatasetModel)
    self.model = None
    
  def execute(self):
    # Model configuration
    # TODO: move out
    input_shape = (100, 100, 1)
    loss_function = sparse_categorical_crossentropy
    optimizer = Adam()

    # Create the model 
    # TODO: move out
    self.model = Sequential()
    self.model.add(Conv2D(16, kernel_size=(5, 5), activation='relu', input_shape=input_shape))
    self.model.add(Conv2D(32, kernel_size=(5, 5), activation='relu'))
    self.model.add(Conv2D(64, kernel_size=(5, 5), activation='relu'))
    self.model.add(Conv2D(128, kernel_size=(5, 5), activation='relu'))
    self.model.add(Flatten())
    self.model.add(Dense(16, activation='relu'))
    self.model.add(Dense(131, activation='softmax'))

    # Display a model summary
    self.model.summary()
    # Compile the model
    self.model.compile(loss=loss_function,
              optimizer=optimizer,
              metrics=['accuracy'])
    
    log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

    self.model.fit(
          self.dataset_model.training_dataset,
          epochs=2,
          validation_data=self.dataset_model.validation_dataset,
          callbacks=[tensorboard_callback])

    # TODO: move out
    self.model.save('./')