import unittest

from ....src.utility.assetLoader.AssetLoader import AssetLoader


class AssetLoaderSuite(unittest.TestCase):

    def setUp(self):
        self.asset_loader = AssetLoader()

    def test_constructor(self):
        self.assertIsNotNone(self.asset_loader)
        self.assertIsNotNone(self.asset_loader.config)
        self.assertIsNotNone(self.asset_loader.images)

    def test_store(self):
        pass

    def test_get_image(self):
        self.asset_loader.store()
        self.assertIsNotNone(self.asset_loader.images)
