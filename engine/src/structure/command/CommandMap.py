import importlib


class CommandMap:

    def __init__(self):
        self.commands = {}

    def execute(self, command):
        self.commands[command.__class__] = self.__resolve_class(command)
        self.commands[command.__class__].execute()

    def _destroy_command(self, command):
        self.commands[command.__class__] = None
        self.commands.pop(command.__class__)

    def destroy(self):
        self.commands = None

    def view_command_stack(self):
        for command in self.commands:
            print(command)

    @staticmethod
    def __resolve_class(class_name):
        split_on_class_name = str(class_name).split('.')[-1]
        string_class_name = split_on_class_name.split('\'')[0]

        module = importlib.import_module(class_name.__module__)
        class_ = getattr(module, string_class_name)
        instance = class_()
        return instance
