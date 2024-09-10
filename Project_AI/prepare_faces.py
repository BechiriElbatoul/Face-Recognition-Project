import face_recognition
import os
import pickle

def load_known_faces(data_dir):
    known_face_encodings = []
    known_face_names = []
    
    for person_name in os.listdir(data_dir):
        person_dir = os.path.join(data_dir, person_name)
        if not os.path.isdir(person_dir):
            continue
        
        for image_file in os.listdir(person_dir):
            image_path = os.path.join(person_dir, image_file)
            image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(image)
            
            if len(face_encoding) > 0:
                known_face_encodings.append(face_encoding[0])
                known_face_names.append(person_name)
    
    return known_face_encodings, known_face_names

# Load known faces
data_dir = 'dataset'  # Update with your dataset path
known_face_encodings, known_face_names = load_known_faces(data_dir)

# Save for later use
with open('known_faces.pkl', 'wb') as f:
    pickle.dump((known_face_encodings, known_face_names), f)
