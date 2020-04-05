/*
  5x5 LED Display
  This example creates a BLE peripheral with service that contains a
  characteristic to control an LED Display.
  The circuit:
  - Arduino MKR WiFi 1010, Arduino Uno WiFi Rev2 board, Arduino Nano 33 IoT,
    Arduino Nano 33 BLE, or Arduino Nano 33 BLE Sense board.
  
  This project utilized bluetoothctl, but you can aslo use a generic BLE central app,
  like LightBlue (iOS and Android) or nRF Connect (Android), to interact with the
  services and characteristics created in this sketch.
  
  This example code is in the public domain.
*/


#include <ArduinoBLE.h>

BLEService ledService("19B10000-E8F2-537E-4F6C-D104768A1214"); // BLE LED Service

// BLE LED Switch Characteristic - custom 128-bit UUID, read and writable by central
BLEByteCharacteristic switchCharacteristic("19B10001-E8F2-537E-4F6C-D104768A1214", BLERead | BLEWrite);

//for this 5X5 display only 25 indeces are needed, one for every LED
int RowColumn[50];

void setup() {
  Serial.begin(9600);
  while (!Serial);

  // set LED pin to output mode
  for(int i=2; i<=12; i++){pinMode(i, OUTPUT);}

  //set all leds off, set all pin indeces to High, its counter intuitive but the voltage change is how the LED's turn on
  for (int a = 0; a < 50; a++) {
    RowColumn[a]=1;}
    
  // begin initialization
  if (!BLE.begin()) {
    Serial.println("starting BLE failed!");

    while (1);
  }

  // set advertised local name and service UUID:
  BLE.setLocalName("LED");
  BLE.setAdvertisedService(ledService);

  // add the characteristic to the service
  ledService.addCharacteristic(switchCharacteristic);

  // add service
  BLE.addService(ledService);

  // set the initial value for the characeristic:
  switchCharacteristic.writeValue(0);

  // start advertising
  BLE.advertise();

  Serial.println("BLE LED Peripheral");
}

void displayLine(int Row, int c1, int c2, int c3, int c4, int c5){
     digitalWrite(Row+6, HIGH);
     digitalWrite(2, c1%2);  //mod 2 allows the second write {RowCoulmn} to turn off that LED
     digitalWrite(3, c2%2);
     digitalWrite(4, c3%2);
     digitalWrite(5, c4%2);
     digitalWrite(6, c5%2);
     delay(2);
     digitalWrite(Row+6, LOW);
}

void printFrame(){
  displayLine(1, RowColumn[0], RowColumn[1],RowColumn[2],RowColumn[3],RowColumn[4]);
  displayLine(2, RowColumn[5],RowColumn[6],RowColumn[7],RowColumn[8],RowColumn[9]);
  displayLine(3, RowColumn[10],RowColumn[11],RowColumn[12],RowColumn[13],RowColumn[14]);
  displayLine(4, RowColumn[15],RowColumn[16],RowColumn[17],RowColumn[18],RowColumn[19]);
  displayLine(5, RowColumn[20],RowColumn[21],RowColumn[22],RowColumn[23],RowColumn[24]);
}


void loop() {
  // listen for BLE peripherals to connect:
  BLEDevice central = BLE.central();

  // if a central is connected to peripheral:
  if (central) {
    Serial.print("Connected to central: ");
    // print the central's MAC address:
    Serial.println(central.address());

    // while the central is still connected to peripheral:
    while (central.connected()) {
      digitalWrite(12, 1); // LED to show bluetooth connection 
      // if the remote device wrote to the characteristic,
      // use the value to control the LEDs:
      if (switchCharacteristic.written()) {
        RowColumn[24-switchCharacteristic.value()]+=1;
        Serial.println(switchCharacteristic.value());             //see the value of what you wrote to the arduino
        Serial.println(RowColumn[switchCharacteristic.value()]);  //check the value of the LED array index
      }
      printFrame();                                               //this is whats running the display
    }
    digitalWrite(12, 0);    // LED to show bluetooth dis-connect                                    
    // when the central disconnects, print it out:
    Serial.print(F("Disconnected from central: "));
    Serial.println(central.address());
  }
}
