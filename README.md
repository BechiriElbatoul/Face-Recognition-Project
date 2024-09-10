Face Recognition System
This project is a simple face recognition system that can identify up to 5 individuals by comparing facial embeddings. 
It uses the face_recognition library along with a Tkinter-based UI to allow users to upload and compare photos.


Features :

= Identify up to 5 persons: The system can recognize up to 5 individuals based on stored facial images.
- Tkinter UI: A simple interface for users to upload images for recognition.
- Pre-trained model: Utilizes pre-trained models for efficient face recognition.

How It Works :

  - Dataset Preparation:
      Store at least one clear image of each person in the dataset/ directory. You can add multiple images per person to improve accuracy. For example:
  
  dataset/
  ├── person_1.jpg
  ├── person_2.jpg
  ├── person_3.jpg
  ├── person_4.jpg
  └── person_5.jpg
  
  - Recognition Process:
  
      - When a user uploads a photo, the system compares it against the stored dataset and returns the closest match based on facial embeddings.
      - The system uses the face_recognition library to compute and compare embeddings.



