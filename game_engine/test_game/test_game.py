import game_engine.game as game
import game_engine.input_receiver as input_receiver
import game_engine.output_device as output_device
from .test_environment import TestEnvironment

class TestGame(game.Game):

    def create_input(self, *args, **kwargs):
        self.logger.debug("Creating input system...")
        return input_receiver.TextReceiver(*args, **kwargs)

    def create_output(self, *args, **kwargs):
        self.logger.debug("Creating output system...")
        return output_device.ConsoleOutput(*args, **kwargs)

    def create_environment(self, *args, **kwargs):
        self.logger.debug("Creating environment system...")
        return TestEnvironment(*args, **kwargs)
