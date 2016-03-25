#include <Wire.h>
#include "ADXL345.h"

#define ROTARY_ANGLE_SENSOR A0
#define LED 2
ADXL345 ACCEL;


/* The following lines were extracted from a test code */

// #define ACCEL (0x53) // I2C port = gnd, vcc, scl and spi pins
// byte values[6] ;
// char output[512];

// The minimum and maximum values during callibration
#define minVal 265
#define maxVal 402


/* Defines inputs and outputs */

void pins_init() {

    pinMode(ROTARY_ANGLE_SENSOR, INPUT);
    pinMode(LED, OUTPUT);

}


/* Determines if the user is slouching, and alerts if so */

void slouch() {

    double x, y, z;
    int xRead, yRead,zRead;

    // read the ACCELerometer values and store them in variables  x,y,z
    ACCEL.readXYZ(&xRead, &yRead, &zRead);

    // convert read values to degrees -90 to 90 - needed for atan2
    int xAng = map(xRead, minVal, maxVal, -90, 90);
    int yAng = map(yRead, minVal, maxVal, -90, 90);
    int zAng = map(zRead, minVal, maxVal, -90, 90);

    //Caculate 360 degree values like so: atan2(-yAng, -zAng)
    //atan2 outputs the value of -π to π (radians)
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


    // if slouch is detected, activate the notfication sensor
    if (x < 80) {

        // current notificaiton sensor for testing is an LED
        digitalWrite(LED, 1);

    } else {
        digitalWrite(LED, 0);
    }

    delay(500);

}


/* Initiates program */

void setup() {


    // begins the serial monitor
    Serial.begin(9600);

    // define the inputs and outputs
    pins_init();


    /* The following lines were extracted from a test code */

    // Wire.begin();
    // Wire.beginTransmission(ACCEL);
    // Wire.write(0x2D);
    // Wire.write(0);
    // Wire.endTransmission();
    // Wire.beginTransmission(ACCEL);
    // Wire.write(0x2D);
    // Wire.write(16);
    // Wire.endTransmission();
    // Wire.beginTransmission(ACCEL);
    // Wire.write(0x2D);
    // Wire.write(8);
    // Wire.endTransmission();
        
    // ACCEL.powerOn();

}


/* Built in function that constantly loops */

void loop() {


    // if the potentiometer != 0, switch is considered on
    int value = analogRead(ROTARY_ANGLE_SENSOR);

    // call if switch is on
    if (value) { slouch(); }


    /* The following lines were extracted from a test code */

    // int xyzregister = 0x32;
    // int x, y, z;

    // Wire.beginTransmission(ACCEL);
    // Wire.write(xyzregister);
    // Wire.endTransmission();

    // Wire.beginTransmission(ACCEL);
    // Wire.requestFrom(ACCEL, 6);

    // int i = 0;
    // while(Wire.available()){
    // values[i] = Wire.read();
    // i++;
    // }
    // Wire.endTransmission();

    // x = (((int)values[1]) << 8) | values[0];
    // y = (((int)values[3])<< 8) | values[2];
    // z = (((int)values[5]) << 8) | values[4];
    // sprintf(output, "%d %d %d", x, y, z);
    // Serial.print(output);
    // Serial.write(10);
    // delay(1000); 

}
