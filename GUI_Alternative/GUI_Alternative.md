
# Alternative GUI

<img src= GUIAlternative.gif>


This alternative GUI is more user friendly, and aesthetically pleasing

Whats new?
- intuitive controls and resizable elements


## Getting Started

Follow these steps to get it up and running

### Prerequisites
- linux
- auto-Py-to-exe

install auto-Py-to-exe
``` $ pip install auto-py-to-exe  ```


### setup steps

- download this repo and navigate to the GUI_Alternative Folder
- right click and open a terminal from the GUI_Alternative Folder
- make the bash scripts found in the GUI folder excecutable
- make all the files ending in.sh excecutable, ```$sudo chmod +x FILENAME ```
- run auto-py-to-exe, ```$ auto-py-to-exe```

At this point you should see a window pop up, 
<img src= "https://github.com/BarakBinyamin/BLE_LED_Display/blob/master/GUI_Alternative/Auto-Py-to-exe.png">

- Select browse next to the "Script Loactaion" textbox --> "files of type" --> "All Files"
- select "GUI_Alternative.py"
- Select "Window Based"
- Select "Additional Files" --> add all of the following files: connect.sh, LED.png, LEDoff.png, LEDon.png, script2.sh, theWrite.sh, write.sh, write2.sh, writeArray.sh
- Convert Py to Exe

ALMOST DONE!

move the output folder somewhere you can find it  
Copy the Excecutable_Link.desktop to your desktop, and edit the file locations  

[Desktop Entry]  
Type=Application  
Name= NAME_YOU_WANT  
Path= Location/of/folderContaingExcecutable  
Exec= Location/of/excecutable  
Icon= Location/of/folderContaingIcon  
Comment[en_US]= Five by Five GUI  
Terminal=false  


## Deployment

[x] click the Excecutable_Link.desktop and trust it



## Acknowledgments

https://pypi.org/project/auto-py-to-exe/
https://wiki.archlinux.org/index.php/Desktop_entries
https://developer.gnome.org/integration-guide/stable/desktop-files.html.en

