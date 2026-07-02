from machine import Pin
import time

print("---")
print("SCRIPT START")
print("---")

#-----------------------------------------------------------------------
# Pin setup
#-----------------------------------------------------------------------
PIN_STEP = 15
PIN_DIR  = 14

step_pin = Pin(PIN_STEP, Pin.OUT)
dir_pin  = Pin(PIN_DIR, Pin.OUT)
led = Pin("LED", Pin.OUT)

#-----------------------------------------------------------------------
# Movement function
# steps: number of step pulses to send
# direction: True/False sets DIR pin state
# step_delay_us: microseconds between step pulses (controls speed)
#-----------------------------------------------------------------------
def move_steps(steps, direction, step_delay_us=1000):
    dir_pin.value(1 if direction else 0)
    time.sleep_us(5)  # small setup delay after changing direction

    for _ in range(steps):
        step_pin.value(1)
        time.sleep_us(step_delay_us // 2)
        step_pin.value(0)
        time.sleep_us(step_delay_us // 2)

#-----------------------------------------------------------------------
# Run the motor
#-----------------------------------------------------------------------

led.value(1)
time.sleep(3)
led.value(0)

print("Moving 4000 steps forward")
move_steps(4000, True, step_delay_us=1000)   # ~1000us/step -> adjust for speed
print("Movement finished")

print("---")
print("SCRIPT FINISHED")
print("---")
