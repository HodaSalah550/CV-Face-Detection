# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 20:16:12 2021

@author: Hoda
"""
import cv2

#create a CascadeClassifier Object
face_cascade =  cv2.CascadeClassifier("C:\\Users\\Hoda\\FaceDetection\\Features\haarcascade_frontalface_default.xml")

#Reading the image as it is 
img = cv2.imread("C:\\Users\\Hoda\\FaceDetection\\lena.jpg")

#Reading the image in grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Search the coordinates of the image 
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)

print (type(faces))
print (faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 1)
"""
(x,y) makan ma habd2 arsam el rect.
(x+w,y+h) end of rect. 
y3ni w and h atwal el rect mn el ganben

(0,255,0) ==> BGR value of the rect. outline

1 ==> width of the rect.
"""

#resized = cv2.resize(img, (int(img.shape[1]*2),int(img.shape[0]*2)))

cv2.imshow ("Lena", img)
cv2.waitKey(0)
cv2.destroyAllwindows()
