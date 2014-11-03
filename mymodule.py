import time
import math


class Cup(object):
    def __init__(self, drink, price):
        self.content = drink
        self.price = price
        self._init_temp = 80
        self.full = 1.0
        self._timestamp = time.time()    # initiate time for cool-down

    def heat_up(self, degrees):
        if degrees < 0:
            raise Exception('heat_up accepts only positive numbers')
        new_temp = self.temp + degrees
        if new_temp <= 100:
            self._init_temp = new_temp
        else:
            self._init_temp = 100
        self._timestamp = time.time()    # refresh time for cool-down

    def drink(self, sip):
        if sip < 0:
            raise Exception('drink only accepts positive numbers')
        self.full -= sip
        if self.full <= 0:
            self.full = 0

    @property
    def temp(self):
        exponent = time.time() - self._timestamp
        return int(self._init_temp * math.exp(-0.0002 * exponent))