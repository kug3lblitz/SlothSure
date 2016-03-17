# Spinosaurus
Spinosaurus is an Arduino project that detects changes in orientation at the shoulders to determine if the back of the user is slouching, and alerts them to fix their posture. It also keeps track of the number of times the user attempts to slouch in a predetermined duration of time.

## Sensors
* 3-Axis Digital Accelerometer (±16g):  
  * On its way
  * [Demo](https://github.com/Seeed-Studio/Accelerometer_ADXL345)
  * [Physics](http://www.seeedstudio.com/wiki/Grove_-_3-Axis_Digital_Accelerometer(%C2%B11.5g)#Reference) understanding required for the computations with Newtonian mechanics and gravity.
* Rotary Angle Sensor (better known as a potentiometer):
  * Can be used as a switch (see tests/switch.ino).
* LED Socket/ Piezo Buzzer/ Vibration Motor:
  * To alert the user

## Materials
- Suspenders
- Velcro straps
- Glue gun
- Masking tape
