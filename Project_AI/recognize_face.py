import face_recognition
import pickle
from tkinter import Tk, filedialog, Label, Button, StringVar

with open('known_faces.pkl', 'rb') as f:
    known_face_encodings, known_face_names = pickle.load(f)

def recognize_face(image_path):
    uploaded_image = face_recognition.load_image_file(image_path)
    uploaded_face_encoding = face_recognition.face_encodings(uploaded_image)
    
    if len(uploaded_face_encoding) == 0:
        return "No face found"
    
    uploaded_face_encoding = uploaded_face_encoding[0]

    matches = face_recognition.compare_faces(known_face_encodings, uploaded_face_encoding)

    if True in matches:
        first_match_index = matches.index(True)
        return known_face_names[first_match_index]
    else:
        return "Unknown"

def upload_image():
    root = Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename()
    if file_path:
        name = recognize_face(file_path)
        result.set(f"Recognized: {name}")


root = Tk()
root.title("Face Recognition")

result = StringVar()
result.set("Upload an image to recognize a face")

label = Label(root, textvariable=result)
label.pack(pady=10)

upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

root.mainloop()
