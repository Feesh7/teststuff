from game_engine.utils import get_logger
import game_engine.environment as environment
import game_engine.mathlib as mathlib
import game_engine.io_manager as io_manager
import game_engine.exceptions as exceptions

class TestEnvironment(environment.Environment):
    def __init__(self, configuration):
        super().__init__(configuration)
        self.logger = get_logger(self.__class__.__name__)
        self._state = mathlib.Vec(0,0,0)
        self.logger.debug("Test environment created.")

    def setup_input(self):
        self._text_receiver = io_manager.get_input_device('TextReceiver')
        return [self._text_receiver]

    def setup_output(self):
        self._console = io_manager.get_output_device('ConsoleOutput')
        return [self._console]

    def process(self):
        mov_text = self._input.get('TextReceiver')
        movement = mov_text.split(",")
        self._move_the_vector(movement)

    def _move_the_vector(self, movement):
        try:
            self._state.add_to(mathlib.Vec(*movement))
        except TypeError as ex:
            self._console.put("Not a valid vector")
            return

        self._console.put("The state of the system is: {}".format(self._state))

        if self._state == mathlib.Vec(10,10,10):
            self._console.put("YOU MADE IT TO THE END!")
            raise exceptions.EndOfGame