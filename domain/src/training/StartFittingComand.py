from engine.src.utility.logger.Logger import Logger
from engine.src.structure.command.Command import Command
from engine.src.model.DatasetModel import DatasetModel
from .models.TrainingModel import TrainingModel
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense, MaxPooling2D, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.callbacks import TensorBoard
import datetime


class StartFittingCommand(Command):

    def __init__(self):
        super().__init__()
        self.logger = self.injector.get_instance(Logger)
        self.dataset_model = self.injector.get_instance(DatasetModel)
        self.training_model = self.injector.get_instance(TrainingModel)
        self.model = None

    def execute(self):

        # Create the model
        # TODO: move out
        self.model = Sequential()

        self.model.add(Conv2D(16, kernel_size=(3, 3),
                              activation='relu', padding="same", input_shape=self.training_model.input_shape))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Conv2D(32, kernel_size=(3, 3),
                              padding="same", activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Dropout(0.2))

        self.model.add(Conv2D(32, kernel_size=(3, 3),
                              padding="same", activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Dropout(0.1))

        self.model.add(Conv2D(64, kernel_size=(3, 3),
                              padding="same", activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Conv2D(128, kernel_size=(3, 3),
                              padding="same", activation='relu'))
        self.model.add(MaxPooling2D(pool_size=(2, 2)))

        self.model.add(Flatten())
        self.model.add(Dense(256, activation='relu'))
        self.model.add(Dense(131, activation='softmax'))

        # Display a model summary
        self.model.summary()
        # Compile the model
        self.model.compile(loss=self.training_model.loss_function,
                           optimizer=self.training_model.optimizer,
                           metrics=self.training_model.metrics)

        log_dir = "assets/logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)

        self.model.fit(
            self.dataset_model.training_dataset,
            epochs=self.training_model.epochs,
            validation_data=self.dataset_model.validation_dataset,
            callbacks=[tensorboard_callback])

        # TODO: move out
        self.model.save(filepath=self.training_model.save_location)
