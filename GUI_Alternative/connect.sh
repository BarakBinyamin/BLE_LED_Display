'''bluetoothctl <<EOF 
connect F1:05:50:46:F1:9E
menu gatt 
select-attribute "/org/bluez/hci0/dev_F1_05_50_46_F1_9E/service000a/char000b19b10001-e8f2-537e-4f6c-d104768a1214"
sleep 5
write 2
EOF'''

echo 'connect F1:05:50:46:F1:9E'
sleep 0.1
echo 'menu gatt'
sleep 0.1
echo "select-attribute /org/bluez/hci0/dev_F1_05_50_46_F1_9E/service000a/char000b"
sleep 0.1




