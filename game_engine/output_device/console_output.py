from .output_device import OutputDevice
from game_engine.utils import get_logger

class ConsoleOutput(OutputDevice):
    def __init__(self, configuration=None, *args, **kwargs):
        super().__init__(configuration, *args, **kwargs)
        self.logger = get_logger(self.__class__.__name__)
        self.logger.debug("Console output device created.")

    def display_output(self, data=None):
        print("CONSOLE OUTPUT: {}".format(data))