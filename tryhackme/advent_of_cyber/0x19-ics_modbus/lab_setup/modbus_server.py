#!/usr/bin/env python3
from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusSlaveContext,
    ModbusServerContext,
)

# Simulated holding registers
# 40005: Delivery mode (1=Presents, 2=Eggs)
store = ModbusSlaveContext(
    hr=ModbusSequentialDataBlock(0, [0] * 100)  # 100 registers
)
store.setValues(3, 5, [2])  # Malicious: Eggs mode
context = ModbusServerContext(slaves=store, single=True)

identity = ModbusDeviceIdentification()
identity.VendorName = "Toy Factory PLC"
identity.ProductCode = "TF-PLC-2025"
identity.ModelName = "Christmas Edition"

if __name__ == "__main__":
    print("[+] Starting vulnerable Modbus PLC on port 502...")
    print("[*] Register 40005 currently set to 2 (Eggs)")
    StartTcpServer(context=context, identity=identity, address=("0.0.0.0", 502))
