from machine import Pin
import time
from rs485 import RS485

# Initialize RS485 communication
rs485 = RS485()

# Initialize LED on D3 (LOW = off, HIGH = on)
led = Pin("D3", Pin.OUT)
led.value(0)

print("RS485 LED Controller started.")

while True:
    # Wait for incoming data
    msg = rs485.receive(500)  # Poll
    
    if msg:
        msg = msg.strip()
        print("Received:", msg)
        
        if msg == "led=1":
            led.value(1)
            rs485.send("LED ON\n")
            print("LED turned ON")
        
        elif msg == "led=0":
            led.value(0)
            rs485.send("LED OFF\n")
            print("LED turned OFF")
    
    # Optional: add a short delay to reduce CPU load
    time.sleep_ms(10)
