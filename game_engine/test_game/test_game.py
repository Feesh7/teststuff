import game_engine.game as game
import game_engine.input_receiver as input_receiver
import game_engine.output_device as output_device
from .test_environment import TestEnvironment

class TestGame(game.Game):

    def create_input(self, configuration):
        self.logger.debug("Creating input system...")
        return input_receiver.TextReceiver(configuration)

    def create_output(self, configuration):
        self.logger.debug("Creating output system...")
        return output_device.ConsoleOutput(configuration)

    def create_environment(self, configuration, input_receiver, output_device):
        self.logger.debug("Creating environment system...")
        return TestEnvironment(configuration=configuration,
                               input_receiver=input_receiver,
                               output_device=output_device)
