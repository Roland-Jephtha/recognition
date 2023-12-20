import serial.tools.list_ports


print("testing...")
ports = list(serial.tools.list_ports.comports())
for port, desc, hwid in ports:
    print(f"Port: {port}, Description: {desc}, Hardware ID: {hwid}")
    
    print(port)