import machine, time
from machine import Pin


class UltrasonicDistance:
    
    def __init__(self, trigger_pin, echo_pin, max_dist=300):
        
        self._timeout_us = int(max_dist*58.27506)
        self._trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self._trigger.value(0)
        self._echo = Pin(echo_pin, mode=Pin.IN, pull=None)

    def distance(self):
        'return distance in cm'
        self._trigger.value(1)
        time.sleep_us(10)
        self._trigger.value(0)
        try:
            pulse_time = machine.time_pulse_us(self._echo, 1, self._timeout_us)
        except OSError as ex:
            if ex.args[0] == 110: # 110 = ETIMEDOUT
                raise OSError('Out of range')
            raise ex
        return pulse_time/ 58.27506
        