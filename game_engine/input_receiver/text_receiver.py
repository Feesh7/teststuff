from .input_receiver import InputReceiver
from game_engine.utils import get_logger

class TextReceiver(InputReceiver):
    def __init__(self, configuration=None):
        super().__init__(configuration=configuration)
        self.logger = get_logger(self.__class__.__name__)
        self.logger.debug("Text receiver created.")

    def get_input(self):
        return input("Enter input: ")