
# BLE_LED_Display


[<img src=GUI_/Updated_GUI.gif>](https://drive.google.com/file/d/1dxTI01UZD03h1vYZ8bcPw23mdWKPQFrs/view?usp=sharing) 


This project combines the [nano ble 33](https://www.amazon.com/Arduino-Nano-33-BLE-Sense/dp/B07WV5GF17/ref=sr_1_4?dchild=1&keywords=nano+ble+33&qid=1586111070&sr=8-4), python, and bash to create a blueetooth LED display and GUI

## Requirements

- [circuit setup](https://github.com/BarakBinyamin/LED-Display/blob/master/README.md#led-display), in this project Digital IO pins 2-6 control colunms 0-4, and Digital IO pins 7-11 control rows 0-4.
- linux
- python3
- bluez,  ```sudo apt install bluez```
- MAC address and service-attribute of the arduino, [find the MAC address and service attribute](https://github.com/BarakBinyamin/BLE_LED_Display/blob/master/starter%20code/Bluetoothctl.md#bluetoothctl)

## Getting Started

Run these commands to install the GUI
```bash
cd 
git clone https://github.com/BarakBinyamin/BLE_LED_Display.git  
chmod +x ~/BLE_LED_Display/GUI_/Install.sh
bash ~/BLE_LED_Display/GUI_/Install.sh ARDUINO_MAC_ADDRESS SERVICE_ATTRIBUTE
```

## Deployment

1. Upload the [sketch](https://github.com/BarakBinyamin/BLE_LED_Display/blob/master/Arduino%20sketches/BLEArduino.ino#L1)
2. Power up the arduino
3. Trust and launch the appliaction

## Going Further
Take a look at the [starter code](https://github.com/BarakBinyamin/BLE_LED_Display/tree/master/starter%20code#starter-code) for examples and walkthroughs to build your own bluetooth arduino sketch
## Recources
- Inspiration from my Uncle Andrew
- [Blutooth Arduino example](https://github.com/arduino-libraries/ArduinoBLE/blob/master/examples/Peripheral/LED/LED.ino)     
- [Guide to Nano ble 33](https://www.arduino.cc/en/Guide/NANO33BLE)     
- [Guide to bluetooth control](https://docs.ubuntu.com/core/en/stacks/bluetooth/bluez/docs/reference/gatt-services)  
- [Wx python](https://wiki.wxpython.org/How%20to%20install%20wxPython)  
- [Information on Desktop applications](https://wiki.archlinux.org/index.php/Desktop_entries)  
- [guide to linux Desktop applications](https://developer.gnome.org/integration-guide/stable/desktop-files.html.en) 

