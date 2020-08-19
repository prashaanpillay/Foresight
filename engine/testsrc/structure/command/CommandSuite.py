import unittest

from ....src.structure.command.Command import Command


class CommandSuite(unittest.TestCase):

    def test_constructor(self):
        command = Command()
        self.assertIsNotNone(command)
        self.assertIsNotNone(command.injector)
        self.assertIsNotNone(command.command_map)

    def test_destroy(self):
        command = Command()
        command.destroy()
        self.assertIsNone(command.injector)
        self.assertIsNone(command.command_map)

