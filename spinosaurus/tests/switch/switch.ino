#define ROTARY_ANGLE_SENSOR A0
#define LED 7

void setup()
{
  PinsInit();
}

void PinsInit()
{
  pinMode(ROTARY_ANGLE_SENSOR, INPUT);
  pinMode(LED, OUTPUT);
}

void loop()
{

  int value = analogRead(ROTARY_ANGLE_SENSOR);

  if (value) {
    digitalWrite(LED,1);
  }

  else {
    digitalWrite(LED,0);
  }

}