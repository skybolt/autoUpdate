sudo killall "Xtightvnc"
sudo service lightdm stop
vncserver :0 -geometry 480x320 -depth 16
