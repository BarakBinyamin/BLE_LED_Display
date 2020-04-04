
# Alternative GUI


[<img src=BLE_LedDisplay.jpg width="50%">](https://drive.google.com/file/d/1dxTI01UZD03h1vYZ8bcPw23mdWKPQFrs/view?usp=sharing)
  <--     click to see video  


This project combines the nano ble 33, python, and bash to create a blueetooth LED display and GUI

Take a look at the starter code for how-to instructions

## Getting Started

This instructional will help guide you in testing this project at home

### Prerequisites

- [circuit setup prerequisites](https://github.com/BarakBinyamin/LED-Display/blob/master/README.md), in this project Digital IO pins 2-6 control colunms 0-4, and Digital IO pins 7-11 control rows 0-4.
- bash command line
- python3
- wxPython


### setup steps

- follow circuit setup
- download the repository
- upload the sketch "BLEArduino.ino" (found in arduino sketches) to the arduino
- make the bash scripts found in the GUI folder excecutable

For each file with ending in ".sh"

```
$sudo chmod +x FILENAME
```

## Deployment

- power up the arduino
- navigate to the GUI folder in the command line
- run the python gui

```

$python3 LedDisplay.py

```


## Built With


- arduino
- python wx
- bash 


## Acknowledgments

https://github.com/arduino-libraries/ArduinoBLE/blob/master/examples/Peripheral/LED/LED.ino  
https://www.arduino.cc/en/Guide/NANO33BLE  
https://docs.ubuntu.com/core/en/stacks/bluetooth/bluez/docs/reference/gatt-services

