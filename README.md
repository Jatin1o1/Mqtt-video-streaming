# Mqtt-video-streaming
**Summary:** Video Streaming using Mosquitto Mqtt broker

 
## Installation
```
$ pip3 install paho-mqtt
$ pip3 install opencv-python
```
## USE
### Publish video stream
To publish video frames with OpenCV over MQTT:
```
$ python3 Stream_publisher.py 
```

### Receive and display video stream
To view the video stream :
```
$ python3 Stream_receiver.py
```

**Note** that this is a high FPS solution, hence it make consume more CPU . This code is written for simplicity and ease of use.

**Note** in Stream_publisher.py  you can set the resolution of the stream to save CPU, RAM, Network bandwidth


## MQTT
Need an MQTT broker?  [click](https://www.vultr.com/docs/how-to-install-mosquitto-mqtt-broker-server-on-ubuntu-16-04)

If you have Docker installed I recommend [eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto). A basic broker can be run with:
```
docker run -p 1883:1883 -d eclipse-mosquitto
```
%
#
