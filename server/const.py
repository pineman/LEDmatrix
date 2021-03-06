BAUD = 115200 # Match arduino's baud rate
PATH = '/dev/ttyUSB0'

WIDTH = 10
HEIGHT = 20
NUM_LEDS = WIDTH * HEIGHT
NUM_BYTES = NUM_LEDS * 3
CHALL = b"We're living in..."
REPLY = "The Matrix."

# Writing to the matrix with period > MIN_PERIOD results in corruption.
MIN_PERIOD = 35e-3

PORT = 53777
