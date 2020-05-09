path="/home/${USER}"

goober=$1

echo "connect ${goober}" >  ${path}/BLE_LED_Display/GUI_/config.txt

pathConfig=${path}/BLE_LED_Display/GUI_/config.txt

#replace the word "GOOBER" in config with the custom configuration 
printf "'/GOOBER/{r $pathConfig' -e 'd}' ${path}/BLE_LED_Display/GUI_/connect.sh" | xargs sed -i -e

chmod +x ${path}/BLE_LED_Display/GUI_/Initialize_files.sh
bash ${path}/BLE_LED_Display/GUI_/Initialize_files.sh

cd  

pip install pyinstaller

sed -i "s#Path#${path}#g" ${path}/BLE_LED_Display/GUI_/LED_GUI.spec

pyinstaller ${path}/BLE_LED_Display/GUI_/LED_GUI.spec

sed -i "s#path#${path}#g" ${path}/BLE_LED_Display/GUI_/Excecutable_Link.desktop

mv ${path}/BLE_LED_Display/GUI_/Excecutable_Link.desktop Desktop

cd Desktop

chmod +x Excecutable_Link.desktop
