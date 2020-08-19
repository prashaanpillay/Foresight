import unittest

from ....src.structure.injector.Injector import Injector
from ....src.structure.model.Model import Model


class InjectorSuite(unittest.TestCase):

    def setUp(self):
        self.injector = Injector()

    def test_constructor(self):
        self.assertIsNotNone(self.injector)
        self.assertIsNotNone(self.injector.binder)

    def test_as_singleton(self):
        self.assertIs(len(self.injector.binder), 0)
        self.injector.as_singleton(Model)
        self.assertIs(len(self.injector.binder), 1)

    def test_as_instance(self):
        self.assertIs(len(self.injector.binder), 0)
        self.injector.as_instance(Model)
        self.assertIs(len(self.injector.binder), 1)
        self.injector.as_instance(Model)
        self.assertIs(len(self.injector.binder), 1)

    def test_get(self):
        injector = Injector()
        injector.as_instance(Model)
        self.assertEqual(injector.get_instance(Model), injector.binder.get(Model))

    def test_remove(self):
        self.assertIs(len(self.injector.binder), 0)
        self.injector.as_instance(Model)
        self.assertIs(len(self.injector.binder), 1)
        self.injector.remove(Model)
        self.assertIs(len(self.injector.binder), 0)
        self.injector.as_singleton(Model)
        self.assertIs(len(self.injector.binder), 1)
        self.injector.remove(Model)
        self.assertIs(len(self.injector.binder), 0)
