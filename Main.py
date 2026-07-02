from machine import Pin
import time

# Import only your motor driver module
from MotorTest import DRV8871

# 1. Initialize the motor driver (Using your pins 16 and 17)
motor = DRV8871(pin_in1=26, pin_in2=27)

# Set the speed level (Choose a safe value between 15000 and 65535)
TEST_SPEED = 65535 

# =========================================================================
# MAIN OPEN-LOOP EXECUTION
# =========================================================================
try:
    print("Running motor without encoder controls...")
    
    while True:
        # Step 1: Spin Forward
        print("Spinning Forward...")
        motor.set_speed(-TEST_SPEED)
        time.sleep(1.0) # Run for 2.5 seconds
        
        # Step 2: Stop/Pause
        print("Stopping...")
        motor.stop()
        time.sleep(1.0) # Rest for 1 second
        
        # Step 3: Spin Backward
        print("Spinning Backward...")
        motor.set_speed(TEST_SPEED)
        time.sleep(1.0) # Run for 2.5 seconds
        
        # Step 4: Stop/Pause
        print("Stopping...")
        motor.stop()
        time.sleep(1.0) # Rest for 1 second

except KeyboardInterrupt:
    print("\nProgram stopped by user. Turning motor off.")
    motor.stop()
