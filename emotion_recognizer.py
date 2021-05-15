"""
emotion_recognizer.py authored by Google Code Next
This program uses the Google Cloud Vision AI API to return the emotion that has the highest confidence score based on a camera input frame (.png)
Run the code in Thonny on the Raspberry Pi with a Camera module attached.
"""

import os, io
from google.cloud import vision
import cv2
from time import sleep
import pprint 


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'GCVision.json' #the credetials to talk to the API.
client = vision.ImageAnnotatorClient()
print("starting emotion recognizer...")

def get_emotion_from_cloud(image_path):

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.face_detection(image=image) #full response from Google cloud vision
    #YOUR CODE UNDER THIS COMMENT
    print(response)
 

def get_image_from_frame(cap):
    ret, frame = cap.read()
    file = 'frame.png'
    cv2.imwrite(file,frame)
    cv2.imshow('frame',frame) #show camera output
    return file

def start_camera():
    os.system('sudo modprobe bcm2835-v4l2') #Force the Raspberry Pi to use the the Picamera, which CV2 will need to capture each frame.

    cap = cv2.VideoCapture(0)
    print("Starting camera")

    while True:
        
        img = get_image_from_frame(cap)
        key = cv2.waitKey(0) #press 0 to move through frames

        if key == ord('q'): #press q to quit
            break
        elif key == ord('s'): #press s to see
            get_emotion_from_cloud(img)
    
    cap.release() #release the object when the app quits.
    cv2.destroyAllWindows()


start_camera()
