from enum import Enum


class StartupProcesses(Enum):
    Acquisition = "acquisition"
    Preprocessing = "preprocessing"
    Training = "training"
    Classification = "classification"
