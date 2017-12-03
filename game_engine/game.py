from .utils import get_logger
from .environment import Environment
from .exceptions import EndOfGame


class Game(object):
    def __init__(self, configuration=None):
        self.logger = get_logger(self.__class__.__name__)
        self._input_receiver = self.create_input(configuration)
        self._output_device = self.create_output(configuration)
        self._environment = self.create_environment(configuration=configuration,
                                                    input_receiver=self._input_receiver,
                                                    output_device=self._output_device)
        self.logger.info("The game was configured")

    def create_input(self, configuration=None):
        raise NotImplementedError

    def create_output(self, configuration):
        raise NotImplementedError

    def create_environment(self, configuration=None, input_receiver=None, output_device=None):
        raise NotImplementedError

    def run(self):
        self.logger.info("Running the game...")
        try:
            while True:
                self._environment.handle_input()
                self._output_device.output_buffer()
        except EndOfGame as ex:
            self._output_device.output_buffer()
            self.logger.info("The game has ended!")

