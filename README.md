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

## Directory structure:

```
src
├── backbone
│   ├── backbone.py
│   ├── Makefile
│   ├── testData.txt
│   └── testOut.cpp
├── graph.json
├── server.py
├── slouch
│   └── slouch.ino
├── static
│   └── js
│       ├── canvasjs.min.js
│       ├── Chart.js
│       ├── Chart.min.js
│       └── gulpfile.js
├── templates
│   ├── js.html
│   ├── samples
│   │   ├── bar.html
│   │   ├── doughnut.color.html
│   │   ├── doughnut.html
│   │   ├── line-customTooltips.html
│   │   ├── line.html
│   │   ├── pie-customTooltips.html
│   │   ├── pie.html
│   │   ├── polar-area.html
│   │   └── radar.html
│   └── success.html
└── tests
    ├── i2c_scanner
    │   └── i2c_scanner.ino
    └── Makefile
```