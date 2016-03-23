/*
File: testOut.cpp

Generates a test output testData.txt for verifying backbone.py
*/


#include <chrono> // for sleep
#include <cmath>
#include <cstdlib> // for RAND_MAX
#include <ctime> // for localtime
#include <fstream> // for file IO
#include <iostream> // for IO
#include <map>
#include <math.h> // for rounding floats
#include <thread> // for sleep

#define RAD_TO_DEG (180.0/M_PI)


long map(long x, long in_min, long in_max, long out_min, long out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

int main() {


    // current time
    std::time_t currentTime = std::time(nullptr);

    // seed the random number generator at runtime
    srand( static_cast<unsigned> ( currentTime ) );

    // create output file
    std::ofstream dataFile("testData.txt");

    int minVal = 265;
    int maxVal = 402;

    // start writing to file
    if ( dataFile.is_open() ) {

        // output current time and date
        dataFile << std::asctime(std::localtime(&currentTime));

        for ( int i = 0; i < 100; i++ ) {

            // sleep every 50 milliseconds
            std::this_thread::sleep_for(std::chrono::milliseconds(50));


            // generate random numbers for the axes
            float x = static_cast<float> ( rand() % (maxVal - minVal) + minVal );
                // / (static_cast<float> (RAND_MAX / 100));
            float y = static_cast<float> ( rand() % (maxVal - minVal) + minVal );

            float z = static_cast<float> ( rand() % (maxVal - minVal) + minVal );

            std::cout << x << " " << y << " " << z << std::endl;

            // round to the nearest
            x = roundf(x * 100) / 100;
            // y = roundf(y * 100) / 100;
            // z = roundf(z * 100) / 100;


            int xAng = map(x, minVal, maxVal, -90, 90);
            int yAng = map(y, minVal, maxVal, -90, 90);
            int zAng = map(z, minVal, maxVal, -90, 90);

              //Caculate 360deg values like so: atan2(-yAng, -zAng)
              //atan2 outputs the value of -π to π (radians)
              //We are then converting the radians to degrees
            x = RAD_TO_DEG * (atan2(-yAng, -zAng) + M_PI);
            y = RAD_TO_DEG * (atan2(-xAng, -zAng) + M_PI);
            z = RAD_TO_DEG * (atan2(-yAng, -xAng) + M_PI);

            // output the data
            dataFile << x << " " << y << " " << z << std::endl;

        }

        // get and output new time after data output
        std::time_t currentTime = std::time(nullptr);
        dataFile << std::asctime(std::localtime(&currentTime));

    }

    dataFile.close();

    return 0;

}