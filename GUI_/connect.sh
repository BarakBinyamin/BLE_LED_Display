
#GOOBER is replaced by the arduino's MAC-Address
'''bluetoothctl <<EOF 
connect GOOBER1
menu gatt 
GOOBER2
sleep 5
write 2
EOF'''

echo 'connect MAC_ADDRESS'
sleep 0.1
echo 'menu gatt'
sleep 0.1
echo "select-attribute SERVCE_ATTRIBUTE"
sleep 0.1




