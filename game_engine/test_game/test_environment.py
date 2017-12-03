from game_engine.utils import get_logger
import game_engine.environment as environment
import game_engine.mathlib as mathlib
import game_engine.exceptions as exceptions

class TestEnvironment(environment.Environment):
    def __init__(self, configuration=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = get_logger(self.__class__.__name__)
        self._state = mathlib.Vec(0,0,0)
        self.logger.debug("Test environment created.")

    def handle_input(self):
        io_input = self._input_receiver.get_input()
        movement = io_input.split(",")
        self._move_the_vector(movement)

    def _move_the_vector(self, movement):
        try:
            self._state.add_to(mathlib.Vec(*movement))
        except TypeError as ex:
            self._output_device.put("Not a valid vector")
            return

        self._output_device.put("The state of the system is: {}".format(self._state))

        if self._state == mathlib.Vec(10,10,10):
            self._output_device.put("YOU MADE IT TO THE END!")
            raise exceptions.EndOfGame