import glob2
import pickle


class AssetLoader:

    def __init__(self):
        self.config = {}
        self.images = {}

    def store(self):
        self.store_config()
        self.store_image()

    def store_config(self):
        for filename in glob2.glob('assets/**/*.json', recursive=True):
            self.config[self.__asset_name_to_string(
                glob2.os.path.basename(filename))] = filename

    def store_image(self, data_set=None):
        if data_set is None:
            for filename in glob2.glob('assets/dataset/**', recursive=True):
                self.images[self.__asset_name_to_string(filename)] = filename
        else:
            for filename in glob2.glob("assets/dataset/" + data_set + "/**", recursive=True):
                self.images[self.__asset_name_to_string(filename)] = filename

    def get_config(self, filename):
        return self.config.get(filename)

    def get_image(self, filename):
        return self.images.get(filename)

    def pop_image_asset(self, filename):
        return self.images.pop(filename)

    def pop_config_asset(self, filename):
        return self.config.pop(filename)

    def read_pickle(self, filename):
        infile = open(filename, 'rb')
        unpickled = pickle.load(infile)
        infile.close()
        return unpickled

    @staticmethod
    def __asset_name_to_string(file_path):
        return file_path + ""
