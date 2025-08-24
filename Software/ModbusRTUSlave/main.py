import time
from rs485 import RS485
from modbus_slave import ModbusRTUSlave

rs485 = RS485()
slave = ModbusRTUSlave(rs485, slave_id=1)

print("Modbus RTU Slave started (ID=1). Listening...")

while True:
    frame = rs485.receive(500)
    if frame:
        response = slave.handle_request(frame)
        if response:
            rs485.send(response)
    time.sleep_ms(10)
