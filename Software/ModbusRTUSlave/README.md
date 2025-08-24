# Modbus RTU LED Controller for Arduino Nicla Vision (MicroPython)

This project demonstrates how to implement a **Modbus RTU Slave** over **RS485** using the **Arduino Nicla Vision Carrier** with **MicroPython**.  
It allows controlling an LED (on **D3**) via Modbus RTU commands, providing feedback and debug information through the serial console.  

---

## Features
- **RS485 Half-Duplex** communication on `UART("LP1", 9600)`
- **Automatic TX/RX Direction Control** via **D0**
- **Modbus RTU Slave (ID=1)**:
  - **Function 0x05 – Write Single Coil** to turn LED ON/OFF
  - **Function 0x01 – Read Coils** to read LED state
- **Debug output** on serial: RX/TX frames, CRC check, LED state changes

---

## Hardware Setup
- **Arduino Nicla Vision** running MicroPython
- **RS485 Transceiver** connected to:
  - `D0` → DE/RE (direction control)
  - `LP1` TX/RX → RS485 transceiver UART pins
- **D3** connected to an LED (with current limiting resistor)
- **RS485 A/B lines** connected to RS485 bus with proper termination

---

## Files

- **rs485.py** – Low-level RS485 communication with automatic TX/RX direction switching  
- **modbus_slave.py** – Minimal Modbus RTU slave implementation (CRC16, coil handling)  
- **main.py** – Main loop: listens for Modbus requests, updates LED, sends responses  


---

## Usage
1. Upload `rs485.py`, `modbus_slave.py`, and `main.py` to your Nicla Vision.
2. Connect the Nicla to the RS485 bus.
3. Run the main application:

