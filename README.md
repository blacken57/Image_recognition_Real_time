# Image_recognition_Real_time



Steps:<br><br>
1)set the python path variable. In linux, export PYTHONPATH=[...]/Image_recognition_Real_time/face_recognition where [...] is the address of where the repository is cloned.<br>
2)Collect Images and store them in folders as follows...<br>

Structure:
```
      images/
            <person_1>/
                <person_1_face-1>.jpg
                <person_1_face-2>.jpg
                .
                .
                <person_1_face-n>.jpg
           <person_2>/
                <person_2_face-1>.jpg
                <person_2_face-2>.jpg
                .
                .
                <person_2_face-n>.jpg
            .
            .
            <person_n>/
                <person_n_face-1>.jpg
                <person_n_face-2>.jpg
                .
                .
                <person_n_face-n>.jpg</p>
```
    keep the 'images' folder in the 'Image_recognition_Real_time' folder.
    3)Run the svm_weight_create.py file. A new .joblib file named "encodings.joblib" should be created.
    4)Run the svmcamera.py file, and make sure there is enough lighting. If your face is in the 'images' folder, you should be recognised.
    
    
    Later, I will add a program to take aligned photos in a short time. And probably fix some lagging issues.Any suggestions, please reach out :)
