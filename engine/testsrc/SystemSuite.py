import unittest

from .utility.assetLoader.AssetLoaderSuite import AssetLoaderSuite
from .structure.command.CommandMapSuite import CommandMapSuite
from .structure.command.CommandSuite import CommandSuite
from .structure.injector.InjectorSuite import InjectorSuite
from .structure.model.ModelSuite import ModelSuite


class SystemSuite(unittest.TestCase):

    @staticmethod
    def test():
        # Run only the tests in the specified classes
        test_classes_to_run = \
            [
                ModelSuite,
                CommandMapSuite,
                CommandSuite,
                InjectorSuite,
                AssetLoaderSuite
            ]

        loader = unittest.TestLoader()

        suites_list = []
        for test_class in test_classes_to_run:
            suite = loader.loadTestsFromTestCase(test_class)
            suites_list.append(suite)

        big_suite = unittest.TestSuite(suites_list)

        runner = unittest.TextTestRunner()
        runner.run(big_suite)
