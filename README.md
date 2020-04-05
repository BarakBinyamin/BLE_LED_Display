
# BLE_LED_Display


[<img src=GUI_/Updated_GUI.gif>](https://drive.google.com/file/d/1dxTI01UZD03h1vYZ8bcPw23mdWKPQFrs/view?usp=sharing) 


This project combines the [nano ble 33](https://www.amazon.com/Arduino-Nano-33-BLE-Sense/dp/B07WV5GF17/ref=sr_1_4?dchild=1&keywords=nano+ble+33&qid=1586111070&sr=8-4), python, and bash to create a blueetooth LED display and GUI

Take a look at the starter code for how-to instructions

## Getting Started

Run these commands to install the GUI
```
cd 
git clone https://github.com/BarakBinyamin/BLE_LED_Display.git  
chmod +x ~/BLE_LED_Display/GUI_/Install.sh
bash ~/BLE_LED_Display/GUI_/Install.sh
```

## Requirements

- [circuit setup](https://github.com/BarakBinyamin/LED-Display/blob/master/README.md), in this project Digital IO pins 2-6 control colunms 0-4, and Digital IO pins 7-11 control rows 0-4.
- linux
- python3

## Deployment

- power up the arduino
- trust and launch the appliaction

## Built With
- arduino
- python wx
- bash 


## Acknowledgments

https://github.com/arduino-libraries/ArduinoBLE/blob/master/examples/Peripheral/LED/LED.ino  
https://www.arduino.cc/en/Guide/NANO33BLE  
https://docs.ubuntu.com/core/en/stacks/bluetooth/bluez/docs/reference/gatt-services

