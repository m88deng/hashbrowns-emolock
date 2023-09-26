import time
import cv2
from deepface import DeepFace
import serial
from playsound import playsound
import numpy as np


def detect4emotionstostr():
    face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'  # getting a haarcascade xml file
    face_cascade = cv2.CascadeClassifier()  # processing it for our project
    if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):  # adding a fallback event
        print("Error loading xml file")

    video = cv2.VideoCapture(0)  # requesting the input from the webcam or camera

    while video.isOpened():  # checking if are getting video feed and using it
        playsound('beep.mp3')
        time.sleep(2)
        _, frame = video.read()
        print("change face")  # IMPROVEMENT IDEA, PLAY A SOUND
        playsound('beep.mp3') #This line plays sound
        time.sleep(2)
        _, frame2 = video.read()
        print("change face")
        playsound('beep.mp3')
        time.sleep(3)
        _, frame3 = video.read()
        print("change face")
        playsound('beep.mp3')
        time.sleep(3)
        _, frame4 = video.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        gray3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
        gray4 = cv2.cvtColor(frame4, cv2.COLOR_BGR2GRAY)
        # changing the video to grayscale to make the face analysis work properly
        face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        face2 = face_cascade.detectMultiScale(gray2, scaleFactor=1.1, minNeighbors=5)
        face3 = face_cascade.detectMultiScale(gray3, scaleFactor=1.1, minNeighbors=5)
        face4 = face_cascade.detectMultiScale(gray4, scaleFactor=1.1, minNeighbors=5)

        for x, y, w, h in face:
            # making a recentangle to show up and detect the face and setting it position and colour
            img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
            img2 = cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 0, 255), 1)
            img3 = cv2.rectangle(frame3, (x, y), (x + w, y + h), (0, 0, 255), 1)
            img4 = cv2.rectangle(frame4, (x, y), (x + w, y + h), (0, 0, 255), 1)

        try:
            analyze = DeepFace.analyze(frame, actions=["emotion"])
            # same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
            print(analyze['dominant_emotion'])
            DomEmo = analyze['dominant_emotion']
            if DomEmo == 'neutral':
                emo1 = '1'
            if DomEmo == 'happy':
                emo1 = '2'
            if DomEmo == 'sad':
                emo1 = '3'
            if DomEmo == 'fear':
                emo1 = '4'
            if DomEmo == 'angry':
                emo1 = '5'
            if DomEmo == 'surprise':
                emo1 = '6'

            # here we will only go print out the dominant emotion also explained in the previous example
        except:
            print("no face")

        try:
            analyze2 = DeepFace.analyze(frame2, actions=["emotion"])
            # same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
            print(analyze2['dominant_emotion'])
            DomEmo2 = analyze2['dominant_emotion']
            if DomEmo2 == 'neutral':
                emo2 = '1'
            if DomEmo2 == 'happy':
                emo2 = '2'
            if DomEmo2 == 'sad':
                emo2 = '3'
            if DomEmo2 == 'fear':
                emo2 = '4'
            if DomEmo2 == 'angry':
                emo2 = '5'
            if DomEmo2 == 'surprise':
                emo2 = '6'
            # here we will only go print out the dominant emotion also explained in the previous example
        except:
            print("no face")

        try:
            analyze3 = DeepFace.analyze(frame3, actions=["emotion"])
            # same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
            print(analyze3['dominant_emotion'])
            DomEmo3 = analyze3['dominant_emotion']
            if DomEmo3 == 'neutral':
                emo3 = '1'
            if DomEmo3 == 'happy':
                emo3 = '2'
            if DomEmo3 == 'sad':
                emo3 = '3'
            if DomEmo3 == 'fear':
                emo3 = '4'
            if DomEmo3 == 'angry':
                emo3 = '5'
            if DomEmo3 == 'surprise':
                emo3 = '6'
            # here we will only go print out the dominant emotion also explained in the previous example
        except:
            print("no face")

        try:
            analyze4 = DeepFace.analyze(frame4, actions=["emotion"])
            # same thing is happing here as the previous example, we are using the analyze class from deepface and using ‘frame’ as input
            print(analyze4['dominant_emotion'])
            DomEmo4 = analyze4['dominant_emotion']
            if DomEmo4 == 'neutral':
                emo4 = '1'
            if DomEmo4 == 'happy':
                emo4 = '2'
            if DomEmo4 == 'sad':
                emo4 = '3'
            if DomEmo4 == 'fear':
                emo4 = '4'
            if DomEmo4 == 'angry':
                emo4 = '5'
            if DomEmo4 == 'surprise':
                emo4 = '6'
            # here we will only go print out the dominant emotion also explained in the previous example
        except:
            print("no face")

            # PLS VERIFY, CHANGING HERE FOR TEST should be 1 2 3 4
        EmoPassList = [emo1, emo2, emo3, emo4]

        EmoPassString = ''.join(EmoPassList)

        print(EmoPassString)

        video.release()

        return EmoPassString


def sendtoarduino(emostring):
    arduino = serial.Serial('COM7', 9600)
    arduino.timeout = 1

    continueloop = True
    while continueloop:
        arduino.write(emostring.encode())
        time.sleep(0.5)
        print(arduino.readline().decode('ascii'))
        if emostring != "2561":  # HERE WE HAVE TO CHANGE THE PASSWORD !!!!! Happy-Angry-Surprise-Neutral
            continueloop = False

    # serial.close()

# 1: Neutral / 2: Happy / 3: sad / 4: fear
while True:
    EmoString = detect4emotionstostr()
    sendtoarduino(EmoString)