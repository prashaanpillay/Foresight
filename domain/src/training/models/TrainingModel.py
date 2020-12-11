from engine.src.structure.model.Model import Model
from tensorflow.keras import optimizers
from tensorflow.keras import losses


class TrainingModel(Model):

    def __init__(self):
        self.optimizer = optimizers.Adam()
        self.loss_function = losses.sparse_categorical_crossentropy
        self.epochs = 1
        self.input_shape = (100, 100, 3)
        self.metrics = []
        self.model_location = ""
        self.save_location = ""

    def set_data(self, config):
        self.setOptimizer(config)
        self.setLossFunction(config)
        self.setEpochs(config)
        self.setMetrics(config)
        self.setSaveLocation(config)

    def setSaveLocation(self, config):
        self.save_location = config["model"]["save_location"]

    def setMetrics(self, config):
        self.metrics = config["model"]["metrics"]

    def setEpochs(self, config):
        self.epochs = config["model"]["epochs"]

    def setOptimizer(self, config):
        configOptimizer = config["model"]["optimizer"].lower()

        if configOptimizer == "Adadelta".lower():
            self.optimizer = optimizers.Adadelta()
        elif configOptimizer == "Adagrad".lower():
            self.optimizer = optimizers.Adagrad()
        elif configOptimizer == "Adamax".lower():
            self.optimizer = optimizers.Adamax()
        elif configOptimizer == "Ftrl".lower():
            self.optimizer = optimizers.Ftrl()
        elif configOptimizer == "SGD".lower():
            self.optimizer = optimizers.SGD()
        elif configOptimizer == "Nadam".lower():
            self.optimizer = optimizers.Nadam()
        elif configOptimizer == "Optimizer".lower():
            self.optimizer = optimizers.Optimizer()
        elif configOptimizer == "RMSprop".lower():
            self.optimizer = optimizers.RMSprop()

    def setLossFunction(self, config):
        configLossFunction = config["model"]["loss_function"].lower()

        if configLossFunction == "BinaryCrossentropy".lower():
            self.lossFunction = losses.binary_crossentropy
        elif configLossFunction == "CategoricalCrossentropy".lower():
            self.lossFunction = losses.categorical_crossentropy
        elif configLossFunction == "CategoricalHinge".lower():
            self.lossFunction = losses.categorical_hinge
        elif configLossFunction == "CosineSimilarity".lower():
            self.lossFunction = losses.cosine_similarity
        elif configLossFunction == "Hinge".lower():
            self.lossFunction = losses.hinge
        elif configLossFunction == "Huber".lower():
            self.lossFunction = losses.huber
        elif configLossFunction == "KLDivergence".lower():
            self.lossFunction = losses.kl_divergence
        elif configLossFunction == "LogCosh".lower():
            self.lossFunction = losses.log_cosh
        elif configLossFunction == "MeanAbsoluteError".lower():
            self.lossFunction = losses.mean_absolute_error
        elif configLossFunction == "MeanAbsolutePercentageError".lower():
            self.lossFunction = losses.mean_absolute_percentage
        elif configLossFunction == "MeanSquaredError".lower():
            self.lossFunction = losses.mean_squared_error
        elif configLossFunction == "MeanSquaredLogarithmicError".lower():
            self.lossFunction = losses.meanSquaredLogarithmicError
        elif configLossFunction == "Poisson".lower():
            self.lossFunction = losses.poisson
        elif configLossFunction == "SparseCategoricalCrossentropy".lower():
            self.lossFunction = losses.sparse_categorical_crossentropy
        elif configLossFunction == "SquaredHinge".lower():
            self.lossFunction = losses.squared_hinge
