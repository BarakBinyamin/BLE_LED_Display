path="/home/${USER}"

goober=$1
goober2=$2

echo "connect ${goober}" >  ${path}/BLE_LED_Display/GUI_/config1.txt
echo "select-attribute ${goober2}" > ${path}/BLE_LED_Display/GUI_/config2.txt

pathConfig1=${path}/BLE_LED_Display/GUI_/config1.txt
pathConfig2=${path}/BLE_LED_Display/GUI_/config2.txt

#replace the word "GOOBER" in config with the custom configuration
printf "'/GOOBER1/{r $pathConfig1' -e 'd}' ${path}/BLE_LED_Display/GUI_/connect.sh" | xargs sed -i -e
printf "'/GOOBER2/{r $pathConfig2' -e 'd}' ${path}/BLE_LED_Display/GUI_/connect.sh" | xargs sed -i -e

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
