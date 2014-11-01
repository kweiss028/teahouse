import time

class Cup(object):
    def __init__(self, drink, price):
        self.content = drink
        self.price = price
        self.temp = 80
        self.full = 1.0
        self.timestamp = time.time()    #initiate time for cool-down
    
    def heat_up(self, degrees):
        if degrees < 0:
            raise Exception('heat_up accepts only positive numbers')
        new_temp = self.get_temp() + degrees
        if new_temp <= 100:
            self.temp = new_temp
        else:
            self.temp = 100
        self.timestamp = time.time()    #refresh time for cool-down
            
    def drink(self, sip):
        if sip < 0:
            raise Exception('drink only accepts positive numbers')
        self.full -= sip
        if self.full <= 0:
            self.full = 0
            
    def get_temp(self):
        cooled = int(time.time() - self.timestamp)
        self.temp -= cooled
        self.timestamp = time.time()    #refresh time for cool-down
        return self.temp