class InputReceiver(object):
    def __init__(self, configuration=None):
        self._configuration = configuration

    def get_input(self):
        raise NotImplementedError