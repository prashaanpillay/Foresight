import json


class JsonParser:

    @staticmethod
    def decode(data):
        if data is None:
            return
        with open(data) as data_file:
            config = json.load(data_file)
        return config

