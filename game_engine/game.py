from .utils import get_logger
from .environment import Environment
from .exceptions import EndOfGame


class Game(object):
    def __init__(self, configuration=None):
        self.logger = get_logger(self.__class__.__name__)
        self._input_system = self.create_input(configuration)
        self._environment = self.create_environment(configuration)
        self.logger.info("The game was configured")

    def create_input(self, configuration=None):
        raise NotImplementedError

    def create_environment(self, configuration=None):
        raise NotImplementedError

    def run(self):
        self.logger.info("Running the game...")
        try:
            while True:
                input = self._input_system.get_input()
                self._environment.set_input(input)
                self._environment.handle_input()
                self._environment.show_state()
        except EndOfGame as ex:
            self.logger.info("The game has ended!")

