# RS485 LED Controller Example

This project demonstrates how to use **RS485 communication** with an **Arduino Nicla Vision** running **MicroPython**, controlling a **LED** via commands received over RS485.  

## Features
- **RS485 Half-Duplex Communication** using `UART("LP1", 9600)`
- **Automatic TX/RX Direction Control** on pin **D0**
- **LED Control** on pin **D3**:
  - Receives `led=1` → Turns LED ON, replies `LED ON`
  - Receives `led=0` → Turns LED OFF, replies `LED OFF`
- **Non-blocking receive with timeout** for responsive operation

---

## `rs485.py` – RS485 Communication Library

This module handles:
- UART initialization (`LP1`, 9600 baud)
- TX/RX direction control using **D0**
- Simple `send()` and `receive(timeout)` methods

### Key Methods:
- `send(data)`: Sends string/bytes over RS485, automatically switching to TX mode.
- `receive(timeout)`: Waits for incoming data for up to `timeout` milliseconds, returns received string or `None`.

---

## `main.py` – Application Logic

- Initializes:
  - `RS485` communication
  - LED output on **D3**
- Main loop:
  - Listens for incoming RS485 messages.
  - When `led=1` is received:
    - Turns LED ON
    - Sends `LED ON` feedback.
  - When `led=0` is received:
    - Turns LED OFF
    - Sends `LED OFF` feedback.

---

## Hardware Setup

- **Arduino Nicla Vision** mounted on the NiclaVCarrier
- **D0** → DE/RE pin of RS485 transceiver (direction control).
- **D3** → User LED
- **RS485 A/B lines** connected to RS485 network.

---

## Usage

1. Upload `rs485.py` and `main.py` to the Nicla Vision.
2. Connect to RS485 network.
3. Send `led=1` or `led=0` from another RS485 device to control the LED (in the project you'll find a Node-RED flow example, I used the wavesgare RS485 USB dongle for testing).

---

## Notes

- Ensure **proper RS485 termination resistors** if using long cables.
- Add a **delay (10–20ms)** between sending commands if multiple devices share the bus.
