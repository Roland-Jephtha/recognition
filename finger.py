from pyfingerprint.pyfingerprint import PyFingerprint

# Initialize the fingerprint sensor
try:
    fingerprint_sensor = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
except Exception as e:
    print("Error: " + str(e))
    exit(1)

# Open the sensor
if not fingerprint_sensor.verifyPassword():
    raise ValueError('The given fingerprint sensor password is not correct!')

# Capture a fingerprint image
try:
    print("Place your finger on the sensor...")
    if fingerprint_sensor.readImage():
        # Convert the image to a data buffer
        fingerprint_data = fingerprint_sensor.downloadImage()
        print("Fingerprint captured successfully.")
    else:
        print("Failed to capture fingerprint image.")
except Exception as e:
    print("Error: " + str(e))

# Close the sensor
fingerprint_sensor.close()
