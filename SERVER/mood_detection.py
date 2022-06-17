from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import time

class Mood_Detection:
    def __init__(self):
        print("mood_detection object initialized")

    def moduledata(self):# this function contains information about this module
        print("mood detection module info ***************")
        print("     Resize (resize the captured image, all resized images should be of the same type)")
        print("     Preprocess (do some preprocess before using the network)")
        print("     Use google server (give processed image and receive data)")
        print("end of info *****************")
   
    def detect(frame):
    	#detect mood from a photo and return it
        face_classifier = cv2.CascadeClassifier('C:/Users/User/PycharmProjects/twin/haarcascade_frontalface_default2.xml')
        classifier = load_model('C:/Users/User/PycharmProjects/twin/model.h5')

        emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

            #labels = []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
                # cv2.imshow(roi_gray)

            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi, axis=0)

                prediction = classifier.predict(roi)[0]
                label = emotion_labels[prediction.argmax()]

                label_position = (x, y)
                cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, 'No Faces', (30, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Emotion Detector', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cap.release()
        cv2.destroyAllWindows()
        return label
