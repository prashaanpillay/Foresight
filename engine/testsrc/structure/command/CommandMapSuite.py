import unittest

from ....src.structure.command.CommandMap import CommandMap


class CommandMapSuite(unittest.TestCase):

    def test_constructor(self):
        command_map = CommandMap()
        self.assertIsNotNone(command_map)
        self.assertIsNotNone(command_map.commands)

