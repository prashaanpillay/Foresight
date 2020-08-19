from StartupProcesses import StartupProcesses
from Model import Model


class StartupConfigModel(Model):

    def __init__(self):
        self.startup_processes = []

    def update(self, config):
        self.startup_processes = config["processes"]

    def has_acquisition(self):
        return self.startup_processes.__contains__(StartupProcesses.Acquisition.value)

    def has_preprocessing(self):
        return self.startup_processes.__contains__(StartupProcesses.Preprocessing.value)