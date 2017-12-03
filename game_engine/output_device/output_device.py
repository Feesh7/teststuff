from collections import deque

class OutputDevice(object):
    def __init__(self, configuration=None):
        self._configuration = configuration
        self._buffer = deque([])

    def display_output(self, data=None):
        raise NotImplementedError

    def output_buffer(self):
        while self._buffer:
            data = self._buffer.popleft()
            self.display_output(data)

    def put(self, data):
        self._buffer.append(data)