class Temperature:
    _temp = 0.0
    _high = 0.0
    _low = 0.0

    def get_current(self):
        return self._temp

    def set_current(self, x, TempOffset=0):
        self._temp = x + TempOffset
        self.set_highlow(self._temp)
    
    def set_highlow(self, x):
        if (x > self._hightemp): self._hightemp = x
        if (x < self._lowtemp): self._lowtemp = x

    def get_high_temp(self):
        return self._hightemp

    def get_low_temp(self):
        return self._lowtemp

class Humidity:
    _humidity = 0.0
    _dewpoint = 0.0

    def get_current(self):
        return self._humidity

    def set_current(self,x, HumidityOffset=0)
        set self._humidity = x + HumidityOffset

class Rain:
    _total = 0.0
    _hourly = 0.0
    _rate = 0.0

    

class Wind:
    _direction = 0
    _speed = 0
    _high = 0

    
    