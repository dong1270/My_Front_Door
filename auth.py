import cv2
# import numpy as np
import timeit

def imageDet(img, face_cascade) :
    img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    results = face_cascade.detectMultiScale(gray,
                                            scaleFactor = 1.5,
                                            minNeighbors = 5,
                                            minSize = (20, 20)
                                            )
    for box in results : 
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), thickness=2)
    cv2.imshow('facenet', img)
    cv2.waitKey(10000)
    

face_cascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
# eye_casecade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('./sample/dong/tests0.jpg')

# print(img)

imageDet(img, face_cascade)