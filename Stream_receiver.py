#!/usr/bin/env python
"""Stream_publisher.py: Send video stream via Mosquitto Mqtt topic """

__author__ = "Jatin Goyal"
__copyright__ = "Copyright 2022, Video surveillance Project"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Jatin Goyal"
__email__ = "robojatin@gmail.com"
__status__ = "Production"


import cv2
import threading
import numpy as np
import paho.mqtt.client as mqtt

class Stream_receiver:

    def __init__(self, topic='',host="127.0.0.1",port=1883):

        """
        Construct a new 'stream_receiver' object to retreive a video stream using Mosquitto_MQTT

        :param topic: MQTT topic to send Stream         
        :param host:  IP address of Mosquitto MQTT Broker
        :param Port:  Port at which Mosquitto MQTT Broker is listening
        
        :return: returns nothing

        : use " object.frame  "  it contains latest frame received
        """

        self.topic=topic
        self.frame=None  # empty variable to store latest message received
        
        self.client = mqtt.Client()  # Create instance of client 

        self.client.on_connect = self.on_connect  # Define callback function for successful connection
        self.client.message_callback_add(self.topic,self.on_message)
        
        self.client.connect(host,port)  # connecting to the broking server
        
        t=threading.Thread(target=self.subscribe)       # make a thread to loop for subscribing
        t.start() # run this thread
        
    def subscribe(self):
        self.client.loop_forever() # Start networking daemon
        
    def on_connect(self,client, userdata, flags, rc):  # The callback for when the client connects to the broker
        client.subscribe(self.topic)  # Subscribe to the topic, receive any messages published on it
        print("Subscring to topic :",self.topic)


    def on_message(self,client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
        
        nparr = np.frombuffer(msg.payload, np.uint8)
        self.frame = cv2.imdecode(nparr,  cv2.IMREAD_COLOR)

        #frame= cv2.resize(frame, (640,480))   # just in case you want to resize the viewing area
        cv2.imshow('recv', self.frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return

        

if __name__ == "__main__":
    # creatign 4 instances of the MQ_subs class
    j=Stream_receiver(topic="test")
    
    
