import json
from sys import exit
from math import pow, sqrt
import serial

# NOTE: THIS SERIAL PORT CHANGES DEPENDING YOUR COMPUTER
# portID = "/dev/tty.usbmodem1421"  # for Mac lel
portID = "/dev/ttyACM0"  # for Linux lel

DATA_FILENAME = "data.json"

ACCEL_DICT = {
    'angle_mag': []
}

# Default value for debugging, keep
ghetto_counter = 0

if __name__ == '__main__':

    # Beginning serial input from port
    with serial.Serial(portID, 9600, timeout=1) as ser:

        # Loads the file as feedingJSON
        with open(DATA_FILENAME, mode='w+') as feedingJson:

            while ser.is_open:

                serialized_line = ser.readline().split()

                if "slouch" in serialized_line:
                    print "ayyyyyyy slouch lmao"

                elif "null" not in serialized_line:

                    try:

                        axis_mag = \
                            sqrt(
                                pow(float(serialized_line[0].decode("utf-8")), 2)
                              + pow(float(serialized_line[1].decode("utf-8")), 2)
                            )

                        print(axis_mag)

                        ACCEL_DICT['angle_mag'].append(axis_mag)

                        ghetto_counter += 1

                    except Exception as e:
                        print("Exception yo fix dis", e)
                        continue

                elif "null" in serialized_line and ghetto_counter:
                    print("Done reading data")
                    feedingJson.write(json.dumps(ACCEL_DICT))
                    exit(0)
