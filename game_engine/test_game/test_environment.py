from game_engine.utils import get_logger
import game_engine.environment as environment
import game_engine.mathlib as mathlib
import game_engine.exceptions as exceptions

class TestEnvironment(environment.Environment):
    def __init__(self, configuration=None):
        self.logger = get_logger(self.__class__.__name__)
        self.logger.debug("Test environment created.")

        self._state = mathlib.Vec(0,0,0)
        super().__init__()

    def handle_input(self):
        movement = self._input.split(",")
        self._move_the_vector(movement)

    def _move_the_vector(self, movement):
        try:
            self._state.add_to(mathlib.Vec(*movement))
        except TypeError as ex:
            print("Not a valid vector")
            return

        if self._state == mathlib.Vec(10,10,10):
            print("YOU MADE IT TO THE END!")
            raise exceptions.EndOfGame

    def show_state(self):
        print("The state of the system is: {}".format(self._state))