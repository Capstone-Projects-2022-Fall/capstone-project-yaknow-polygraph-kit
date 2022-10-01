/*
The following is responsible for collecting data from the examinee wearing the GSR sensor connected to the Arduino Board and is displayed results in the terminal.
For the following code to run, the actual device is required.
*/

const int BUZZER=3;
const int GSR=A2;
int threshold=0;
int sensorValue;

/*
serial functions are responsible for interacting with the board.
analogRead function is responsible for capturing the data from the GSR input, which has been pre-defined to the A2 port of the board.
threshold value has been set to the first 500 values collected by the port before it is worn by the user to get a consistent value.
*/
void setup()
{
  long sum=0;
  Serial.begin(9600);
  pinMode(BUZZER,OUTPUT);
  digitalWrite(BUZZER,LOW);
  delay(1000);

  for(int i=0;i<500;i++)
  {
    sensorValue=analogRead(GSR);
    sum += sensorValue;
    delay(5);
  }
  threshold = sum/500;
  Serial.print("threshold =");
  Serial.println(threshold);
}
/*
with the threshold values defined, sensorValue reads the immediate reading from the board.
The temp variable (threshold - sensorValue) is then analysed further.
*/
void loop()
{
  int temp;
  sensorValue=analogRead(GSR);
  Serial.print("sensorValue=");
  Serial.println(sensorValue);
  temp = threshold - sensorValue;
  if(abs(temp)>50)
  {
    sensorValue=analogRead(GSR);
    temp = threshold - sensorValue;
    if(abs(temp)>50)
    {
      digitalWrite(BUZZER,HIGH);
      Serial.println("YES!");
      delay(3000);
      digitalWrite(BUZZER,LOW);
      delay(1000);
    }
  }
}