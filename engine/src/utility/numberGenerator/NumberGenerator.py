import numpy as np


class NumberGenerator:

    def __init__(self):
        self.seed = 0

    def random(self, minimum, maximum):
        np.random.seed(self.seed)
        return np.random.randint(minimum, maximum)

    def set_seed(self, seed):
        self.seed = seed

    def get_seed(self):
        return self.seed
