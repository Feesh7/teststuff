import testmodule.game as game
import testmodule.input_system as input_system
from .test_environment import TestEnvironment

class TestGame(game.Game):

    def create_input(self, configuration):
        self.logger.debug("Creating input system...")
        return input_system.TextReceiver(configuration)

    def create_environment(self, configuration):
        self.logger.debug("Creating environment system...")
        return TestEnvironment(configuration)