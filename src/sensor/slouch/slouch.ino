#include <TimeLib.h> // for current time
#include <Wire.h>
#include "ADXL345.h"

int ROTARY_ANGLE_SENSOR = 0; // pin A0
#define LED 2 // pin D2
ADXL345 ACCEL; // I2C pin 0x53

time_t CURRENT_TIME = now();


/* Defines inputs and outputs */

void pins_init() {

    pinMode(ROTARY_ANGLE_SENSOR, INPUT);
    pinMode(LED, OUTPUT);

    // output current time and date
    Serial.println(year(CURRENT_TIME));

}


/* Determines if the user is slouching, and alerts if so */

void slouch() {

    double x, y, z;
    double g_in_xyz[3];

    ACCEL.getAcceleration(g_in_xyz);
    x = g_in_xyz[0];
    y = g_in_xyz[1];
    z = g_in_xyz[2];

    float vec_mag =  sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2));
    float x_ang = acos(x / vec_mag) * 180 / M_PI;
    float y_ang = acos(y / vec_mag) * 180 / M_PI;
    float z_ang = acos(z / vec_mag) * 180 / M_PI;

    Serial.print("X=");
    Serial.print(x_ang);
    Serial.print(" deg");
    Serial.print(" | Y=");
    Serial.print(y_ang);
    Serial.print(" deg");
    Serial.print(" | Z=");
    Serial.print(z_ang);
    Serial.println(" deg");


    // current notification sensor for testing is an LED
    if (x_ang < 80.0) {

        Serial.println("SLOUCH");
        digitalWrite(LED, 1);

    } else {
        digitalWrite(LED, 0);
    }


    delay(1000);

}


/* Initiates program */

void setup() {

    // current time
    //    CURRENT_TIME = std::time(NULL);

    // begins the serial monitor
    Serial.begin(9600);

    // define the inputs and outputs
    pins_init();
    ACCEL.powerOn();

}


/* Built in function that constantly loops */

void loop() {

    // if the potentiometer > 40, switch is considered on
    int value = analogRead(ROTARY_ANGLE_SENSOR);

    // call if switch is on
    if (value > 40) {
        slouch();
    }

}

