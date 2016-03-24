#include <Wire.h>
#include "ADXL345.h"

#define ROTARY_ANGLE_SENSOR A0
#define LED 7
ADXL345 ACCEL;

// The minimum and maximum values during callibration
#define minVal 265
#define maxVal 402


void pinsInit() {

    pinMode(ROTARY_ANGLE_SENSOR, INPUT);
    pinMode(LED, OUTPUT);

}


void slouch() {

    double x, y, z;
    int xRead,yRead,zRead;

    //read the ACCELerometer values and store them in variables  x,y,z
    ACCEL.readXYZ(&xRead, &yRead, &zRead);

    //convert read values to degrees -90 to 90 - Needed for atan2
    int xAng = map(xRead, minVal, maxVal, -90, 90);
    int yAng = map(yRead, minVal, maxVal, -90, 90);
    int zAng = map(zRead, minVal, maxVal, -90, 90);

    //Caculate 360deg values like so: atan2(-yAng, -zAng)
    //atan2 outputs the value of -π to π (radians)
    //We are then converting the radians to degrees
    x = RAD_TO_DEG * (atan2(-yAng, -zAng) + PI);
    y = RAD_TO_DEG * (atan2(-xAng, -zAng) + PI);
    z = RAD_TO_DEG * (atan2(-yAng, -xAng) + PI);

    //Output the calculations
    Serial.print("x: ");
    Serial.print(x);
    Serial.print(" | y: ");
    Serial.print(y);
    Serial.print(" | z: ");
    Serial.println(z);

    if (x < 80) {
        digitalWrite(LED,1);
    } else {
        digitalWrite(LED,0);
    }

    delay(50);

}


void setup() {

    Serial.begin(9600);
    pinsInit();
    ACCEL.powerOn();

}


void loop() {

    int value = analogRead(ROTARY_ANGLE_SENSOR);

    if (value) { slouch(); }

}
