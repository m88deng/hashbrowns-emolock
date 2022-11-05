from deepface import DeepFace
import cv2

face_cascade_name = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'  # getting a haarcascade xml file
face_cascade = cv2.CascadeClassifier()  # processing it for our project
if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):  # adding a fallback event
    print("Error loading xml file")

video = cv2.VideoCapture(0)

img = "Angry1.jpg"
attributes = ['emotion']

video = cv2.VideoCapture(0)

#while video.isOpened():  # checking if are getting video feed and using it
    #_,
frame = video.read()
print("Read video\n")

gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

demography = DeepFace.analyze(frame, attributes)

print(demography['dominant_emotion'])

print("done")
