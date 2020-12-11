import datetime
import os


class Logger:

    def __init__(self):
        pass
        # basename = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../bin")) + "/foresight"
        # suffix = datetime.datetime.now().strftime("%y%m%de_%H%M%S") + ".txt"
        # self.filename = "_".join([basename, suffix])
        # self.file = open(self.filename, "w+")
        # self.heading_pad = "========================"

    def log(self, text, heading=False):
        # if heading:
        # text = self.heading_pad + text + self.heading_pad
        output = Colors.OKBLUE + text + Colors.ENDC
        print(output)
        # self.file.write(text + '\n')

    def warn(self, text, heading=False):
        # if heading:
        # text = self.heading_pad + text + self.heading_pad
        output = Colors.WARNING + text + Colors.ENDC
        print(output)
        # self.file.write(text + '\n')

    def error(self, text, heading=False):
        # if heading:
        # text = self.heading_pad + text + self.heading_pad
        output = Colors.FAIL + text + Colors.ENDC
        print(output)
        # self.file.write(text + '\n')

    def progress(self, text, heading=False):
        # if heading:
        # text = self.heading_pad + text + self.heading_pad
        output = Colors.OKGREEN + text + Colors.ENDC
        print(output)
        # self.file.write(text + '\n')

    def dispose(self):
        pass
        # self.file.close()
        # del self.file
        # del self.filename


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
