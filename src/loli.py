# void setup() {
#
#   // Begins serial data communication at 9600 bits per second
#   Serial.begin(9600);
# }
#
# void loop() {
#
#   char z_string[] = "Z axis coordinate is: ";
#
#   char y_string[] = "Y axis coordinate is: ";
#
#   char x_string[] = "X axis coordinate is: ";
#
#
#   float zAxisValue = analogRead(A0);
#   float yAxisValue = analogRead(A1);
#   float xAxisValue = analogRead(A2);
#
#   Serial.println(z_string);
#   Serial.println(zAxisValue);
#   delay(1000);
#
#   Serial.println(y_string);
#   Serial.println(yAxisValue);
#   delay(1000);
#
#   Serial.println(x_string);
#   Serial.println(xAxisValue);
#   delay(1000);
# }
import serial
portID = "/dev/tty.usbmodem1421"

with serial.Serial(portID, 9600, timeout=1) as ser:
    while True:
        while ser.is_open:
            line = ser.readline()
            print line
