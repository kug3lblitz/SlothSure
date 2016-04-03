import json
from math import pow, sqrt

import serial


class Tacocat(object):

    def __init__(self):

        # NOTE: THIS SERIAL PORT CHANGES DEPENDING YOUR COMPUTER
        # self.portID = "/dev/tty.usbmodem1421"  # for Mac lel
        self.portID = "/dev/ttyACM0"  # for Linux lel

        self.DATA_FILENAME = "data.json"

        self.ACCEL_DICT = {
            'time': [],
            'angle_mag': []
        }

        # Default value for debugging, keep
        self.ghetto_counter = 0

        self.timer = 0

    def racecar(self):

        # Beginning serial input from port
        with serial.Serial(self.portID, 9600, timeout=1) as ser:

            # Loads the file as feedingJSON
            with open(self.DATA_FILENAME, mode='w+') as feedingJson:

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

                            self.ACCEL_DICT['angle_mag'].append(axis_mag)
                            self.ACCEL_DICT['time'].append(self.timer)

                            self.timer += 500
                            self.ghetto_counter += 1

                        except Exception:
                            print("Counting down...")
                            continue

                    elif "null" in serialized_line and self.ghetto_counter:
                        print("Done reading data")
                        feedingJson.write(json.dumps(self.ACCEL_DICT))
                        break

# for testing
# Tacocat().racecar()
