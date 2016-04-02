import json
from sys import exit

import serial

# NOTE: THIS SERIAL PORT CHANGES DEPENDING YOUR COMPUTER
portID = "/dev/tty.usbmodem1421"

DATA_FILENAME = "testing.json"

ACCEL_DICT = {
	'angles': {
		'x-axis': [],
		'z-axis': []
	}
}

# Default value for debugging, keep
currentAxis = 0

if __name__ == '__main__':

	# Opens an empty file to preprocess dumping
	with open(DATA_FILENAME, mode='w') as f:
		json.dump([], f)

	# Beginning serial input from port
	with serial.Serial(portID, 9600, timeout=1) as ser:

		# Loads the file as feedingJSON
		with open(DATA_FILENAME, mode='a+') as feedingJson:
			serialized_line = [',']

			while ser.is_open:
				serialized_line = ser.readline().split()
				if len(serialized_line) > 1:
					# print(float(serialized_line[0].decode("utf-8")))

					try:
						# if len(serialized_line) == 2:
						ACCEL_DICT['angles']['x-axis'].append(
							float(serialized_line[0].decode("utf-8")))
						ACCEL_DICT['angles']['z-axis'].append(
							float(serialized_line[1].decode("utf-8")))

						print(ACCEL_DICT)

					# if len(serialized_line) < 1:
					except:
						print("yoyoyoyooy\n")
						feedingJson.write(json.dumps(ACCEL_DICT))
						exit(0)
