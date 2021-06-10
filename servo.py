from machine import PWM

class Servo:
    def __init__(self, pin, freq_Hz=100, min_us=400, max_us=2400, total_degree=180):
        self._min_us = min_us
        self._max_us = max_us
        self.total_degree=total_degree
        self._freq_Hz = freq_Hz
        self._pwm = PWM(pin, freq=freq_Hz, duty=0)

    def setPosition(self, pos):
        if pos<0:
            pos=0
        elif pos>self.total_degree:
            pos=self.total_degree
        pos_us=self._min_us+(self._max_us-self._min_us)*pos/self.total_degree
        duty = int(pos_us *1024 *self._freq_Hz /1000000)
        self._pwm.duty(duty)

    def deinit(self):
        self._pwm.duty(0)
        self._pwm.deinit()