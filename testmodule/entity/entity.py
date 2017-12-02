import testmodule.vectors as vectors

class entity(object):
    def __init__(self, position):
        if not isinstance(position, vectors.Vec):
            try:
                position = vectors.Vec(*position)
            except Exception as ex:
                raise TypeError("Input position is not valid")
        self._position = position

    def move_to(self, new_position):
        self._position.set(new_position)

    def move(self, movement_vector):
        self._position.add_to(movement_vector)

