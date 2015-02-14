// reads analog input from the five inputs from your arduino board 
// and sends it out via serial

// variables for input pins and
int analogInput[6];
int sample[10];  
// variable to store the value 
int value[6]; 
int flag = 0;
 
void setup()
{
  // declaration of pin modes
  for(int i=0;i<6;i++)
  {
    analogInput[i] = i+1;
    value[i] = 0;     
    pinMode(analogInput[i], INPUT);    
  }
  
  // begin sending over serial port
  Serial.begin(9600);
}

void loop()
{
  // read the value on analog input
  int sum = 0;
  for(int i=0;i<20;i++)
  {
    sum+=analogRead(A0);
    delay(30);    
  }
  //Serial.println(sum/10);
  if((sum/20)>=500)
  {
    if(flag != 1)
    {
      Serial.println(1);  
    }    
  }
  else
  {
    flag = 0;
  }
  delay(30);
//Serial.println(10000 + i + 1); //prefix
    
//    Serial.println(10010); //end signal
  // print out value over the serial port
  // wait for a bit to not overload the port
  
}


