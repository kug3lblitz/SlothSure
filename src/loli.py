import serial

# NOTE: THIS SERIAL PORT CHANGES DEPENDING YOUR COMPUTER
portID = "/dev/tty.usbmodem1421"

count = 0

recordedDirections = {
	'x-axis': [],
	'y-axis': [],
	'z-axis': []
}

def storingValues(valueOfAxis, nameOfValue):
	recordedDirections[nameOfValue].append(valueOfAxis)


currentAxis = 0

if __name__ == '__main__':
	with serial.Serial(portID, 9600, timeout=1) as ser:
		while True:
			while ser.is_open:
				line = ser.readline()

				try:
					currentAxis = float(line)
					print currentAxis

				except ValueError:
					print "Beginning Program!"

				if line != 0:
					if count == 0:
						storingValues(currentAxis, 'x-axis')
					elif count == 1:
						storingValues(currentAxis, 'y-axis')
					elif count == 2:
						storingValues(currentAxis, 'z-axis')

				count %= 3
				count += 1
