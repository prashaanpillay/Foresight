import importlib


class Injector:

    def __init__(self):
        self.binder = {}

    def as_singleton(self, class_name) -> object:
        if self.binder.get(class_name) is not None:
            return self.binder[class_name]

        self.binder[class_name] = self.__resolve_class(class_name)
        return self.binder[class_name]

    def as_instance(self, class_name):
        self.binder[class_name] = self.__resolve_class(class_name)
        return self.binder[class_name]

    def set_instance(self, class_name, constructed_obj):
        self.binder[class_name] = constructed_obj
        return self.binder[class_name]

    def remove(self, class_name):
        if self.binder.get(class_name) is not None:
            self.binder[class_name] = None
            self.binder.pop(class_name)

    def get_instance(self, class_name):
        if self.binder.get(class_name) is not None:
            return self.binder[class_name]
        else:
            # TODO: somehow get the logger in here
            print("Fatal Error: Injector does not have reference to: "+str(class_name))

    @staticmethod
    def __resolve_class(class_name):
        split_on_class_name = str(class_name).split('.')[-1]
        string_class_name = split_on_class_name.split('\'')[0]

        module = importlib.import_module(class_name.__module__)
        class_ = getattr(module, string_class_name)
        instance = class_()
        return instance

    def destroy(self):
        del self.binder
