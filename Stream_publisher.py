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
import paho.mqtt.client as mqtt


class Stream_publisher:
    
    def __init__(self,topic, video_address=0,start_stream=True, host="127.0.0.1", port=1883 ) -> None :
        """
        Construct a new 'stream_publisher' object to broadcast a video stream using Mosquitto_MQTT

        :param topic: MQTT topic to send Stream 
        :param video_address: link for OpenCV to read stream from, default 0 (webcam)

        :param start_stream:  start streaming while making object, default True, else call object.start_streaming()
        
        :param host:  IP address of Mosquitto MQTT Broker
        :param Port:  Port at which Mosquitto MQTT Broker is listening
        
        :return: returns nothing
        """
        
        self.client = mqtt.Client()  # create new instance
        self.client.connect(host, port)
        self.topic=topic
        self.video_source=video_address

        #self.cam = cv2.VideoCapture(0)  # webcam
        #self.cam = cv2.VideoCapture("example_video.mkv")  # place video file 
        self.cam = cv2.VideoCapture(self.video_source)  

        self.streaming_thread= threading.Thread(target=self.stream)
        if start_stream:
            self.streaming_thread.start()
    
    def start_streaming(self):
        self.streaming_thread.start()

    def stream(self):
        print("Streaming from video source : {}".format(self.video_source))
        while True:
            _ , img = self.cam.read()
            #img = cv2.resize(img, (640 ,480))  # to reduce resolution 
            img_str = cv2.imencode('.jpg', img)[1].tobytes()

            self.client.publish(self.topic, img_str)
            

if __name__ == "__main__":
    webcam= Stream_publisher("test", video_address=0)  # streaming from webcam (0) to  topic : "test"
    #file= Stream_publisher("test", video_address="kungfu-panda.mkv")  # streaming from a file to  topic : "test"
    

