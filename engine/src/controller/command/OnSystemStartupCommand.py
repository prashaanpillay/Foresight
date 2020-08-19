from ...utility.assetLoader.AssetLoader import AssetLoader
from ...structure.command.Command import Command
from ...utility.logger.Logger import Logger
from ...utility.numberGenerator.NumberGenerator import NumberGenerator


class OnSystemStartupCommand(Command):

    def execute(self):
        asset_loader = self.injector.as_singleton(AssetLoader)
        asset_loader.store_config()

        self.injector.as_instance(NumberGenerator)
        self.injector.as_singleton(Logger)

    def destroy(self):
        super.destroy()
