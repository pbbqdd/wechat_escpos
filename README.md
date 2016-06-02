# wechat_escpos
#version_0.01
需要flask，wechat_sdk，pyusb
udev中需要加入如下规则
$ sudo su
\# echo "SUBSYSTEM==\"usb\", ATTRS{idVendor}==\"0483\", ATTRS{idProduct}==\"070b\", MODE=\"0664\", GROUP=\"pi\"">>/etc/udev/rules.d/99-escpos.rules



\# sudo service udev restart 
\# sudo udevadm control --reload
