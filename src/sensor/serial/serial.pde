/*
    Step 1: Turn on the Arduino and make sure it is generating ouput to the serial terminal. There should be a yellow light on the board called "tx" should be lit
    Step 2: Make sure you specify which port Processing should "listen" to to get the output from arduino search for #AssignPort in this code
    Step 3: Press Play on the processing program
    Step 4: The keyPressed function is listening for specific key presses. This tells Processing to do certain things. Key 'r' = record; Key 'w'= write to file; Key 'p' means print to Processing console
    Step 5: Press on keyboard 'r'. There should be a count down it should print the values it records. The variable Buffersize determines how many datainputs to record
    Step 6: Press on keyboard 'p' to inspect
    Step 7: Press on keyboard 'w' to write to file search for #filename in the code to fine the line of code that specifies file name
    

    */

//Setup variables for serial input
import processing.serial.*;
PrintWriter output;
Serial port ;

int cr = 13;  // ASCII return   == 13r
int lf = 10;  // ASCII linefeed == 10
int zero = 48; //ASCII numeric zero = 48
int counter = 0;
int BufferSize = 30;

String buf="";
char state;

StringList recordData;


void setup() {

    println(Serial.list());

    // #AssignPort
    port = new Serial(this, Serial.list()[0], 9600);
    port.bufferUntil(lf);

    // #filename this specifies the filename to output
    output = createWriter("output.txt");
    recordData = new StringList();

}


void draw() {

    background(0);

}


// Code to test modulation of sin wave amplitude and frequency
void keyPressed() {

    String temp;

    if (key == 'w') {
    println("Writing to File");

    for (int counter = 0; counter < recordData.size(); counter ++) {
        temp= recordData.get(counter);
        output.println(temp); 
    }

    output.flush(); // Writes the remaining data to the file
    output.close(); // Finishes the file
    exit(); // Stops the program

    } else if (key == 'r') {

        println("Recording State in 3 sec");
        delay(1000);
        println("3");
        delay(1000);
        println("2");
        delay(1000);
        println("1");
        delay(1000);


        for (int counter = 0; counter < BufferSize; counter++) {

            print("Recording ");
            println(buf);
            recordData.append(buf);
            delay(100);

        }

        println("End Recording Waiting 5sec");
        delay(5000);
        key = 'k';
        } else if(key == 'p'){
        println("Print");
        for(int counter = 0; counter < recordData.size(); counter ++) {
           print("["+counter+"]");
           println(recordData.get(counter));

       }

       state = 'r';

       } else {

        println("OFF");
        state ='o';

    }

}

// Code to process Serial input from Arduino
// Reads serial input. If the serial input is significant, changes the amplitude and calls draw functio()

void serialEvent(Serial p) {

    buf = p.readStringUntil('\n');

}