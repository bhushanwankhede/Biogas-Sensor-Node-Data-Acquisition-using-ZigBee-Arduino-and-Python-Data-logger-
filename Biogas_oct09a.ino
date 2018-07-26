
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13 , OUTPUT);
}

char in_val=' ';
void loop() {
  // put your main code here, to run repeatedly:
  
   if(Serial.available() > 0 )
   {
    in_val=Serial.read();
    Serial.print(in_val);
      
   }
   
}
