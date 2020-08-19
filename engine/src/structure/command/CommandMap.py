class CommandMap:

    def __init__(self):
        self.commands = {}

    def execute(self, command):
        self.commands[command.__class__] = command
        command.execute()

    def _destroy_command(self, command):
        self.commands[command.__class__] = None
        self.commands.pop(command.__class__)

    def destroy(self):
        self.commands = None

    def view_command_stack(self):
        for command in self.commands:
            print(command)
