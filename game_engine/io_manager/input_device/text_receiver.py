from .input_device import InputDevice
from game_engine.utils import get_logger

class TextReceiver(InputDevice):
    def __init__(self, name='TextReceiver', configuration=None):
        super().__init__(name=name, configuration=configuration)
        self.logger = get_logger(self.__class__.__name__)
        self.logger.debug("Text receiver created.")

    def get_input(self):
        return input("Enter input: ")