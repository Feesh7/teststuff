from .input_device import TextReceiver
from .output_device import ConsoleOutput

io_inputs = {'TextReceiver': TextReceiver}
io_outputs = {'ConsoleOutput': ConsoleOutput}

# Store previously created devices for retrieval
input_map = {}
output_map = {}

def get_input_device(device, name=None, *args, **kwargs):
    try:
        name = name or device
        if name not in input_map:
            input_map[name] = io_inputs[device](name=name, *args, **kwargs)
        return input_map[name]
    except KeyError:
        raise ValueError("Invalid input device type: {}".format(name))

def get_output_device(device, name=None, *args, **kwargs):
    try:
        name = name or device
        if name not in output_map:
            output_map[name] = io_outputs[device](name=name, *args, **kwargs)
        return output_map[name]
    except KeyError:
        raise ValueError("Invalid output device type: {}".format(name))

def remove_input_device(name):
    dev = input_map.pop(name, None)
    if dev is None:
        raise ValueError("Input device does not exist: {}".format(name))
    dev.shutdown()

def remove_output_device(name):
    dev = output_map.pop(name, None)
    if dev is None:
        raise ValueError("Input device does not exist: {}".format(name))
    dev.shutdown()