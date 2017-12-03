from .input_receiver import InputReceiver
from testmodule.utils import get_logger

class TextReceiver(InputReceiver):
    def __init__(self, configuration=None):
        self.logger = get_logger(self.__class__.__name__)
        self.logger.debug("Text receiver created.")
        super().__init__(configuration)

    def get_input(self):
        return input("Enter input: ")