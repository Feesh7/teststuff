from .utils import get_logger
from .environment import Environment
from .exceptions import EndOfGame

class Game(object):
    def __init__(self, configuration=None):
        self.logger = get_logger(self.__class__.__name__)
        self._configuration = configuration
        self.logger.info("The game was configured")

    def create_environment(self, configuration=None):
        raise NotImplementedError

    def run(self):
        self._environment = self.create_environment(configuration=self._configuration)
        self._environment.setup()

        self.logger.info("Running the game...")
        try:
            while True:
                self._environment.handle_input()
                self._environment.process()
                self._environment.flush_output()
        except EndOfGame as ex:
            self._environment.flush_output()
            self.logger.info("The game has ended!")

