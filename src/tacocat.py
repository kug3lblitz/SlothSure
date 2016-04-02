import json
from sys import exit
from math import pow, sqrt
import serial

# NOTE: THIS SERIAL PORT CHANGES DEPENDING YOUR COMPUTER
# portID = "/dev/tty.usbmodem1421"  # for Mac lel
portID = "/dev/ttyACM0"  # for Linux lel

DATA_FILENAME = "data.json"

ACCEL_DICT = {
    'angles': {
        'x-axis': [],
        'z-axis': []
    }
}

# Default value for debugging, keep
ghetto_counter = 0

if __name__ == '__main__':

    # Beginning serial input from port
    with serial.Serial(portID, 9600, timeout=1) as ser:

        # Loads the file as feedingJSON
        with open(DATA_FILENAME, mode='a+') as feedingJson:

            while ser.is_open:

                serialized_line = ser.readline().split()

                if "slouch" in serialized_line:
                    print "ayyyyyyy slouch lmao"

                elif "null" not in serialized_line:

                    try:
                        ACCEL_DICT['angles']['x-axis'].append(
                            float(serialized_line[0].decode("utf-8")))

                        ACCEL_DICT['angles']['z-axis'].append(
                            float(serialized_line[1].decode("utf-8")))

                        print(ACCEL_DICT)

                        ghetto_counter += 1

                    except:
                        continue

                elif "null" in serialized_line and ghetto_counter:
                    print("Done reading data")
                    feedingJson.write(json.dumps(ACCEL_DICT))
                    exit(0)
