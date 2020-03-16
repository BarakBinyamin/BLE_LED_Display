var=${1}
echo 'menu gatt'
sleep 0.1
echo "select-attribute /org/bluez/hci0/dev_F1_05_50_46_F1_9E/service000a/char000b"
sleep 0.1
echo 'write' ${var}
sleep 0.1
