path="/home/${USER}"

chmod +x ${path}/BLE_LED_Display/GUI_/Initialize.sh
bash ${path}/BLE_LED_Display/GUI_/Initialize.sh

cd 

pip install pyinstaller

sed -i "s#Path#${path}#g" ${path}/BLE_LED_Display/GUI_/LED_GUI.spec

pyinstaller ${path}/BLE_LED_Display/GUI_/LED_GUI.spec

sed -i "s#path#${path}#g" ${path}/BLE_LED_Display/GUI_/Excecutable_Link.desktop

mv ${path}/BLE_LED_Display/GUI_/Excecutable_Link.desktop Desktop

cd Desktop

chmod +x Excecutable_Link.desktop
