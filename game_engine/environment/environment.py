class Environment(object):
    def __init__(self, configuration=None):
        self._configuration = configuration

    def setup(self):
        in_devs = self.setup_input()
        out_devs = self.setup_output()
        self._input_map = {dev.name:dev for dev in in_devs}
        self._output_map = {dev.name:dev for dev in out_devs}

    def setup_input(self):
        """ must return a list of input devices """
        raise NotImplementedError

    def setup_output(self):
        """ must return a list of output devices """
        raise NotImplementedError

    def process(self):
        """ process the inputs and generate an output state """
        raise NotImplementedError

    def handle_input(self, *args, **kwargs):
        self._input = {name:dev.get_input() for name,dev in self._input_map.items()}

    def flush_output(self, *args, **kwargs):
        for dev in self._output_map.values():
            dev.flush()
