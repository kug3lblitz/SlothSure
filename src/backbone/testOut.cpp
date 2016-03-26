/*
File: testOut.cpp

Generates a test output testData.txt for verifying backbone.py
*/


#include <chrono> // for sleep
#include <cstdlib>
#include <ctime> // for localtime
#include <fstream> // for file IO
#include <iostream> // for IO
#include <thread> // for sleep


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
            float y = static_cast<float> ( rand() % (maxVal - minVal) + minVal );
            float z = static_cast<float> ( rand() % (maxVal - minVal) + minVal );

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