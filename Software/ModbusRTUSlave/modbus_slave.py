from machine import Pin
import struct

class ModbusRTUSlave:
    def __init__(self, rs485, slave_id=1):
        self.rs485 = rs485
        self.slave_id = slave_id
        self.led = Pin("D3", Pin.OUT)
        self.led.value(0)

    def _crc16(self, data):
        """Compute Modbus RTU CRC16"""
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 1:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        return crc

    def _build_response(self, function, payload):
        pdu = bytes([self.slave_id, function]) + payload
        crc = self._crc16(pdu)
        return pdu + struct.pack("<H", crc)

    def handle_request(self, frame):
        """Parse and respond to a Modbus RTU frame"""
        if len(frame) < 4:
            return None
        
        # Validate CRC
        data, recv_crc = frame[:-2], frame[-2:]
        calc_crc = struct.pack("<H", self._crc16(data))
        if recv_crc != calc_crc:
            return None
        
        slave, func = frame[0], frame[1]
        if slave != self.slave_id:
            return None
        
        # Function 0x05: Write Single Coil
        if func == 0x05 and len(frame) == 8:
            coil_addr = (frame[2] << 8) | frame[3]
            value = (frame[4] << 8) | frame[5]
            if coil_addr == 0:
                self.led.value(1 if value == 0xFF00 else 0)
            return self._build_response(0x05, frame[2:6])

        # Function 0x01: Read Coils
        if func == 0x01 and len(frame) == 8:
            coil_addr = (frame[2] << 8) | frame[3]
            qty = (frame[4] << 8) | frame[5]
            if coil_addr == 0 and qty == 1:
                state = self.led.value()
                byte_count = 1
                return self._build_response(0x01, bytes([byte_count, state]))

        return None
