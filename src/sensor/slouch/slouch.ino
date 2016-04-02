#include <Wire.h>
#include "ADXL345.h"

int ROTARY_ANGLE_SENSOR = 0; // pin A0
#define VIBRATION 2 // pin D2
ADXL345 ACCEL; // I2C pin 0x53

float X_ANG = 0;
float Z_ANG = 0;
int CALIB = 5000;

/* Defines inputs and outputs */

void pins_init() {

  pinMode(ROTARY_ANGLE_SENSOR, INPUT);
  pinMode(VIBRATION, OUTPUT);

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
  //    float y_ang = acos(y / vec_mag) * 180 / M_PI; // y axis
  float z_ang = acos(z / vec_mag) * 180 / M_PI;

  if (!CALIB) {

    Serial.print(x_ang);
    Serial.print(" ");
    Serial.println(z_ang);

    if (x_ang < (X_ANG - 5) and z_ang < (Z_ANG - 5)) {

      digitalWrite(VIBRATION, 1);

    } else {
      digitalWrite(VIBRATION, 0);
    }

  }

  else {
    X_ANG = x_ang;
    Z_ANG = z_ang;
    CALIB -= 500;
    if (CALIB == 500) {
      Serial.print(X_ANG);
      Serial.print(" ");
      Serial.println(Z_ANG);
    }
  }

  delay(500);

}


/* Initiates program */

void setup() {

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

