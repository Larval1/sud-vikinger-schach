class ThrowPowerBar:
    def __init__(self):
        self.throw_power = 0

    def get_throw_power(self):
        return self.throw_power

    def trow_power_increase(self, dt):
        if (self.throw_power < 100):
            if (self.throw_power - 100 * dt < 100):
                self.throw_power += 100 * dt
            else:
                self.throw_power = 100

    def trow_power_decrease(self, dt):
        if (self.throw_power > 0):
            if (self.throw_power - 100 * dt > 0):
                self.throw_power -= 100 * dt
            else:
                self.throw_power = 0