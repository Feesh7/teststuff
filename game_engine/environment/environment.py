class Environment(object):
    def __init__(self, configuration=None, input_receiver=None, output_device=None):
        self._configuration = configuration
        self._input_receiver = input_receiver
        self._output_device = output_device

    def set_input(self, input):
        self._input = input

    def handle_input(self):
        raise NotImplementedError

    def show_state(self):
        raise NotImplementedError
