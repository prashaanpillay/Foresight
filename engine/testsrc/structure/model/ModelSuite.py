import unittest

from ....src.structure.model.Model import Model


class ModelSuite(unittest.TestCase):

    def test_constructor(self):
        model = Model()
        self.assertIsNotNone(model)
