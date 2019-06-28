import face_recognition
from sklearn import svm
import os
import joblib
import numpy

encodings = []
names = []

train_dir = os.listdir('images/')

# Loop through each person in the training directory
for person in train_dir:
    pix = os.listdir("images/" + person)
    
    # Loop through each training image for the current person
    for person_img in pix:
        # Get the face encodings for the face in each image file
        face = face_recognition.load_image_file("images/" + person + "/" + person_img)
        face_enc = face_recognition.face_encodings(face)[0]
        
        # Add face encoding for current image with corresponding label (name) to the training data
        print(person)
        encodings.append(face_enc)
        names.append(person)
        
# Create and train the SVC classifier
clf = svm.SVC(gamma='scale')
clf.fit(encodings,names)

joblib.dump(clf,"encodings.joblib")