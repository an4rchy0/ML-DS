import cv2
import os
import shutil

input_folder = r'D:\(D) Document\Project\Python\ML\CVCropFace\path\to\raw'
output_folder = r'D:\(D) Document\Project\Python\ML\CVCropFace\path\to\faceF'
no_face_folder = r'D:\(D) Document\Project\Python\ML\CVCropFace\path\to\buang'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

if not os.path.exists(no_face_folder):
    os.makedirs(no_face_folder)

# Load Haar Cascade face detector model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

for idx, file in enumerate(files, start=1):
    img = cv2.imread(os.path.join(input_folder, file))
    
    if img is None:
        continue
    
    new_name = f'{idx}.png'
    
    # Cek apakah file dengan nama baru sudah ada
    new_name_path = os.path.join(input_folder, new_name)
    counter = 1
    while os.path.exists(new_name_path):
        new_name = f'{idx}_{counter}.png'
        new_name_path = os.path.join(input_folder, new_name)
        counter += 1
    
    os.rename(os.path.join(input_folder, file), new_name_path)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    if len(faces) == 0:
        shutil.move(new_name_path, os.path.join(no_face_folder, new_name))
    else:
        for face_idx, (x, y, w, h) in enumerate(faces, start=1):
            face = img[y:y + h, x:x + w]
            
            face_filename = f'gg{idx}_{face_idx}.png'
            cv2.imwrite(os.path.join(output_folder, face_filename), face)
