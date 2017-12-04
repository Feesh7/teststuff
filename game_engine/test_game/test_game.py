import game_engine.game as game
from .test_environment import TestEnvironment

class TestGame(game.Game):
    def create_environment(self, configuration):
        self.logger.debug("Creating environment system...")
        return TestEnvironment(configuration=configuration)
