from machine import Pin, UART
import time

class RS485:
    def __init__(self, uart_id="LP1", baudrate=9600, de_pin="D0"):
        # Initialize UART
        self.uart = UART(uart_id, baudrate)
        
        # Initialize DE/RE control pin (HIGH = transmit, LOW = receive)
        self.de = Pin(de_pin, Pin.OUT)
        self.de.value(0)  # Start in receive mode

    def send(self, data):
        """Send data over RS485"""
        self.de.value(1)        # Enable TX mode
        time.sleep_us(100)      # Allow RS485 transceiver to switch
        
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        self.uart.write(data)
        self.uart.flush()       # Ensure all data is transmitted
        
        time.sleep_us(100)      # Wait for last byte to complete
        self.de.value(0)        # Switch back to RX mode

    def receive(self, timeout=1000):
        """Receive data with timeout in milliseconds"""
        start = time.ticks_ms()
        buffer = b""
        
        while time.ticks_diff(time.ticks_ms(), start) < timeout:
            if self.uart.any():
                buffer += self.uart.read(1)
            else:
                time.sleep_ms(1)
        
        return buffer.decode('utf-8') if buffer else None
