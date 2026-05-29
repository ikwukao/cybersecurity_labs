#!/usr/bin/env python3
from pymodbus.client import ModbusTcpClient


def scan_registers(host, start=0, count=20):
    client = ModbusTcpClient(host, port=502)
    if not client.connect():
        print("[-] Connection failed")
        return

    print(f"[+] Scanning holding registers {40001 + start} to {40000 + start + count}")
    result = client.read_holding_registers(start, count)
    if result.isError():
        print("[-] Read error")
    else:
        for i, value in enumerate(result.registers):
            addr = 40001 + start + i
            print(
                f"    Register {addr}: {value} {'<- DELIVERY MODE' if addr == 40005 else ''}"
            )

    client.close()


if __name__ == "__main__":
    scan_registers("plc", 0, 20)
