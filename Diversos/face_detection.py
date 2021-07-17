# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:54:15 2020

@author: Matheus Yokoyama
"""


import cv2

cv2.namedWindow("camera")
captura = cv2.VideoCapture(0) # passando zero para capturar entrada camera

if captura.isOpened(): # try to get the first frame (Se camera aberto)
    rval, frame = captura.read()
else:
    rval = False

while rval:
    cv2.imshow("camera", frame)
    rval, frame = captura.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cv2.imshow("camera cinza", gray)
    
    
    detector = cv2.CascadeClassifier('frontalFace.xml')
    
    rects = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(75,75))

    if rects != ():
      cont =+ 1
      for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #cv2.putText(frame, "Cat #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    
captura.release()
cv2.destroyWindow("camera") # fecha camera normal
cv2.destroyWindow("camera cinza") # 