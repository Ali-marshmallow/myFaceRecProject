from cv2 import cv2
import numpy as np

filename = r"C:\Users\53838\Desktop\pic\test10.jpg"
path = r'C:\Users\53838\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data'

def detect(filename):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    eye_cascade.load(path + '\haarcascade_eye.xml')
    face_cascade.load(path + '\haarcascade_frontalface_default.xml')

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(faces)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 10)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        #print(roi_gray)
        eyes = eye_cascade.detectMultiScale(roi_gray)
    #eyes = np.delete(eyes,0,0)
    for eye in eyes:
        ex = eye[0]
        ey = eye[1]
        ew = eye[2]
        eh = eye[3]
        if ew >= 120 or eh >= 120:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 10)
        

    print(eyes)
    cv2.namedWindow("vikings detected",0)
    cv2.imshow("vikings detected", img)
    cv2.waitKey(0)


detect(filename)
