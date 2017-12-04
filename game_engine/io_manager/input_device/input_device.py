class InputDevice(object):
    def __init__(self, name=None, configuration=None):
        self.name = name
        self._configuration = configuration

    def get_input(self):
        raise NotImplementedError