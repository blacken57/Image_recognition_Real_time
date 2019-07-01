import face_recognition
import cv2
import numpy as np
import joblib
import time

clf = joblib.load('encodings.joblib')
naam = joblib.load("name.joblib")
enc = joblib.load("pics.joblib")


video_capture = cv2.VideoCapture(0)


face_locations = []
face_encodings = []
face_names_set1 = set()
face_names = []
process_this_frame = True
print(type(face_names_set1))
timeinit = time.time()


while (time.time()-timeinit<=8.0):
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        l = 0
        
        
        face_names = []
        if(face_encodings !=[]):
            face_names = clf.predict(face_encodings)
            print(clf.predict_proba(face_encodings))
            #print(np.shape(clf.predict_proba(face_encodings))
            for x in face_names:
                face_names_set1.add(x)
       
        
    
    process_this_frame = not process_this_frame

  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(face_names_set1)
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
