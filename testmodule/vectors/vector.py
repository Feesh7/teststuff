from testmodule.utils import zzip

X = 0
Y = 1
Z = 2


class Vec(object):

    def __init__(self, *args):
        self._set(*args)


    """ public methods """
    # Set
    def set(self, *args):
        self._set(*args)

    # Dot product
    def dot(self, vec):
        return self._dot(vec)

    # Addition
    def add(self, vec):
        return Vec(*(self._add(vec)))

    def add_to(self, vec):
        self._vec = self._add(vec)

    # Subtraction
    def sub(self, vec):
        return Vec(*(self._sub(vec)))

    def sub_to(self, vec):
        self._vec = self._sub(vec)

    # Scaling
    def scale(self, factor):
        return Vec(*(self._scale(factor)))

    def scale_to(self, factor):
        self._vec = self._scale(factor)

    # Multiplying across
    def multiply(self, vec):
        return Vec(*(self._multiply(vec)))

    def multiply_to(self, vec):
        self._vec = self._multiply(vec)

    def cross(self, vec):
        return Vec(*(self._cross(vec)))

    def cross_to(self, vec):
        self._vec = self._cross(vec)


    """ internal methods """
    def _set(self, *args):
        try:
            self._vec = [int(a) for a in args]
        except Exception as ex:
            raise TypeError("Could not set vector. Bad input.")

    def _dot(self, vec):
        if isinstance(vec, Vec):
            return sum([a*b for a,b in zip(self._vec, vec._vec)])
        else:
            raise TypeError("Dot product not supported between Vec and {}"
                            .format(type(vec)))

    def _add(self, vec):
        if isinstance(vec, Vec):
            return [a+b for a,b in zzip(self._vec, vec._vec)]
        else:
            raise TypeError("Addition not supported between Vec and {}"
                            .format(type(vec)))

    def _sub(self, vec):
        if isinstance(vec, Vec):
            return [a-b for a,b in zzip(self._vec, vec._vec)]
        else:
            raise TypeError("Addition not supported between Vec and {}"
                            .format(type(vec)))

    def _scale(self, factor):
        if isinstance(factor, int):
            return [a*factor for a in self._vec]
        else:
            raise TypeError("Scaling not supported between Vec and {}"
                            .format(type(factor)))

    def _multiply(self, vec):
        if isinstance(vec, Vec):
            return [a*b for a,b in zzip(self._vec, vec._vec)]
        else:
            raise TypeError("Multiplication not supported between Vec and {}"
                            .format(type(vec)))

    def _cross(self, vec):
        if isinstance(vec, Vec):
            if len(self._vec) != 3 or len(vec._vec) != 3:
                raise TypeError("Cross product requires both vectors to be 3D")

            a = self._vec
            b = vec._vec
            return [a[Y]*b[Z] - b[Y]*a[Z],
                    b[X]*a[Z] - a[X]*b[Z],
                    a[X]*b[Y] - b[X]*a[Y]]
        else:
            raise TypeError("Cross product not supported between Vec and {}"
                            .format(type(vec)))


    """ operator overloads """
    def __add__(self, vec):
        return self.add(vec)

    def __sub__(self, vec):
        return self.sub(vec)
    
    def __mul__(self, obj):
        if isinstance(obj, int):
            return self.scale(obj)
        elif isinstance(obj, Vec):
            return self.multiply(obj)
        else:
            raise TypeError("Multiply operator not supported between Vec and {}"
                            .format(type(obj)))


    """ data overloads """
    def __repr__(self):
        return "<{}>".format(", ".join([str(a) for a in self._vec]))