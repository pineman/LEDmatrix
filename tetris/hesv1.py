from serial import Serial
from serial.tools.list_ports import comports
import time
import sys

BAUD = 9600
CHALL = b"Hi. Who are you?"
RESP = b"Hi. I'm HES."

class HESv1:
    def __init__(self):
        self.bindings = ['Select', 'Start', 'Up', 'Down', 'Left', 'Right', 'A', 'B']
        self.hesv1 = self.find_hesv1()

        if not self.hesv1:
            raise Exception('HESv1 Error: HESv1 device not found.')

    def find_hesv1(self):
        dev = Serial('/dev/ttyUSB1', BAUD)
        time.sleep(2)

        dev.write(CHALL)
        reply = dev.read(len(RESP))
        if reply == RESP:
            # HESv1 always sends one empty message on connection.
            # It's weird, so we absorb that first read.
            dev.read()
            dev.timeout = None
            return dev

    def read(self):
        d = self.hesv1.readline().rstrip().decode()
        if d:
            return d[0], self.bindings[int(d[1])]
