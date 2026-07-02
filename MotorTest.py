from machine import Pin, PWM

class DRV8871:
    def __init__(self, pin_in1, pin_in2, freq=1000):
        self.in1 = PWM(Pin(pin_in1))
        self.in2 = PWM(Pin(pin_in2))
        self.in1.freq(freq)
        self.in2.freq(freq)

    def set_speed(self, speed):
        """Speed ranges from -65535 to 65535"""
        if speed > 0:
            self.in1.duty_u16(speed)
            self.in2.duty_u16(0)
        elif speed < 0:
            self.in1.duty_u16(0)
            self.in2.duty_u16(abs(speed))
        else:
            self.in1.duty_u16(0)
            self.in2.duty_u16(0)
            
    def stop(self):
        self.set_speed(0)
