from testmodule.utils import get_logger
import testmodule.environment as environment
import testmodule.mathlib as mathlib
import testmodule.exceptions as exceptions

class TestEnvironment(environment.Environment):
    def __init__(self, configuration=None):
        self.logger = get_logger(self.__class__.__name__)
        self.logger.debug("Test environment created.")

        self._state = mathlib.Vec(0,0,0)
        super().__init__()

    def handle_input(self):
        try:
            movement = self._input.split(",")
            self._move_the_vector(movement)
        except TypeError as ex:
            print("Not a valid vector")

    def _move_the_vector(self, movement):
        self._state.add_to(mathlib.Vec(*movement))

        if self._state == mathlib.Vec(10,10,10):
            print("YOU MADE IT TO THE END!")
            raise exceptions.EndOfGame

    def show_state(self):
        print("The state of the system is: {}".format(self._state))