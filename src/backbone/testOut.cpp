/*
File: testOut.cpp

Generates a test output testData.txt for verifying backbone.py

*/


#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iostream>
#include <math.h>


int main() {

    srand( static_cast<unsigned> ( time(0) ) );
    std::ofstream dataFile("testData.txt");

    if ( dataFile.is_open() ) {

        for (int i = 0; i < 100; i++) {

            float x = static_cast<float> (rand())
                / (static_cast<float> (RAND_MAX / 100));
            float y = static_cast<float> (rand())
                / (static_cast<float> (RAND_MAX / 100));
            float z = static_cast<float> (rand())
                / (static_cast<float> (RAND_MAX / 100));

            x = roundf(x * 100) / 100;
            y = roundf(y * 100) / 100;
            z = roundf(z * 100) / 100;

            dataFile << "x=" << x << " y=" << y << " z=" << z << std::endl;

        }

    }

    dataFile.close();

    return 0;

}