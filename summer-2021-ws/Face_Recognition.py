# Step 2 - Train Model

import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

# Get the training data we previously made
data_path = './FACES/MOHIT/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

# Create arrays for training data and labels
Training_Data, Labels = [], []

# Open training images in our datapath
# Create a numpy array for training data
for i, files in enumerate(onlyfiles):
    image_path = data_path + onlyfiles[i]
    images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

# Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)

# Initialize facial recognizer
# model = cv2.face.createLBPHFaceRecognizer()
# NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()
# pip install opencv-contrib-python
#model = cv2.createLBPHFaceRecognizer()

mohit_model  = cv2.face_LBPHFaceRecognizer.create()
#mohit_model = cv2.face.createLBPHFaceRecognizer()
# Let's train our model 
mohit_model.train(np.asarray(Training_Data), np.asarray(Labels))
print("Model trained sucessefully")



# ---------------------------------------------------------------------------------------



# Step 3 - Run Our Facial Recognition

import cv2
import numpy as np
import os


face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def face_detector(img, size=0.5):

    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi


# Open Webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    image, face = face_detector(frame)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value
        results = mohit_model.predict(face)
        # harry_model.predict(face)

        if results[1] < 500:
            confidence = int( 100 * (1 - (results[1])/400) )
            display_string = str(confidence) + '% Confident it is User Mohit'

        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,120,150), 2)

        if confidence > 90:
            cv2.putText(image, "Hey Mohit", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            #cv2.imshow('Face Recognition', image)
            cv2.imwrite("test-img.png",image)
            image1=cv2.imread("test-img.png")
            cv2.imshow('Face Recognition', image1)
            cv2.waitKey(2000)
            #os.system("python3 /pythonws/NextGen.py")
            #os.system("msedge https://www.google.com/search?q=vimal+daga")
            #os.system("wmplayer   c:\lw.mp3")
            break

        else:

            cv2.putText(image, "I dont know, who r u", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow('Face Recognition', image )

    except:
        cv2.putText(image, "No Face Found", (220, 120) , cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.putText(image, "looking for face", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
        cv2.imshow('Face Recognition', image )
        pass

    if cv2.waitKey(1) == 13: #13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()

os.system("clear")
print("\n\n\n\n\n")
os.system("cd /pythonws && python3 NextGen.py")
