class Environment(object):
    def __init__(self, configuration=None):
        self._configuration = configuration
        self._input = None

    def set_input(self, input):
        self._input = input

    def handle_input(self):
        raise NotImplementedError

    def show_state(self):
        raise NotImplementedError
