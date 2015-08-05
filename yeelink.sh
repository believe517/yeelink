#sudo fswebcam -d /dev/video0 -r 320x240 --bottom-banner --title "RaspberryPi @ Yeelink" --no-timestamp /home/pi/yeelink.jpg
sudo fswebcam --no-banner -r 640x480 yeelink.jpg
sudo curl --request POST --data-binary @"/home/pi/yeelink.jpg" --header "U-ApiKey: 1896c43cef112d1ab0002d9d136a17e1" -url http://api.yeelink.net/v1.0/device/89596/sensor/123217/photos
