
# Bluetoothctl

## Getting Started

These instructions will give you the tools necessary to comunicate with an arduino nano 33 ble.

### Prerequisites

- bluez, bluetoothctl

```bash
sudo apt install bluez
```

### Talking with the arduino


open blutoothctl, ctrl+alt+t will open a terminal on linux

```bash
$blutoothctl
```


Now we need to find the device, look for the name arduino or LED

```bash
 [bluetooth]: scan on
```

In the midst of all the other devices listed, the one to be looking for should look like this:

**[NEW] Device F1:05:50:46:F1:9E Arduino**  


connect to the arduino:

```bash
 [bluetooth]: connect F1:05:50:46:F1:9E
```

If there was no message other than "attempting to connect" then you are not connected, try again/ or reset the arduino.
The command line header should have also changed from "bluetooth" to "Arduino" or the name of your service

The next step is to open gatt

```bash
[Arduino]: menu gatt
```

```bash
[Arduino]: list-attributes
```

This is what should be seen

> [NEW] Device F1:05:50:46:F1:9E Arduino  
> [NEW] Primary Service  
>	/org/bluez/hci0/dev_F1_05_50_46_F1_9E/service000a  
>	19b10000-e8f2-537e-4f6c-d104768a1214  
>	Vendor specific  
> [NEW] Characteristic  
>	**/org/bluez/hci0/dev_F1_05_50_46_F1_9E/service000a/char000b**  
>	19b10001-e8f2-537e-4f6c-d104768a1214  
>	Vendor specific  
> [NEW] Primary Service  
>	/org/bluez/hci0/dev_F1_05_50_46_F1_9E/service0006  
>	00001801-0000-1000-8000-00805f9b34fb  
>	Generic Attribute Profile  
> [NEW] Characteristic  
>	/org/bluez/hci0/dev_F1_05_50_46_F1_9E/service0006/char0007  
>	00002a05-0000-1000-8000-00805f9b34fb  
>	Service Changed  
> [NEW] Descriptor  
>	/org/bluez/hci0/dev_F1_05_50_46_F1_9E/service0006/char0007/desc0009  
>	00002902-0000-1000-8000-00805f9b34fb  


select the service attribute to comunicate with the arduino

```bash
[Arduino]: select-attribute /org/bluez/hci0/dev_F1_05_50_46_F1_9E/service000a/char000b
```


write a value

```
[/org/bluez/hci0/dev_F1_05_50_46_F1_9E/service000a/char000b]: write 1
```



## Recources/Acknowledgments

https://docs.ubuntu.com/core/en/stacks/bluetooth/bluez/docs/reference/gatt-services
