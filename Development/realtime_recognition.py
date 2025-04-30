import face_recognition
import cv2
import pickle
import numpy as np
import sqlite3
from datetime import datetime 

try:
    with open("embeddings.pkl", "rb") as f:
        embeddings = pickle.load(f)
    print("Loaded embeddings:", embeddings)
except Exception as e:
    print(f"Error loading embeddings: {e}")
    exit()
conn = sqlite3.connect('attendance.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS detected_faces (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open video feed.")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    print("Face Locations:", face_locations)
    face_encodings = []
    if face_locations:
        try:
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            print("Real-time encodings:", face_encodings)
        except Exception as e:
            print(f"Error in face encodings: {e}")
    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = []
        for student_id, student_encodings in embeddings.items():
            if not student_encodings:
                print(f"No embeddings for {student_id}. Skipping.")
                continue
            distances = face_recognition.face_distance(student_encodings, face_encoding)
            matches.append((student_id, np.mean(distances)))
        if matches:
            best_match = min(matches, key=lambda x: x[1])
            student_id, distance = best_match
            print(f"Best match: {student_id} with distance: {distance}")
            if distance < 0.6:  # You can adjust this threshold
                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, student_id, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                current_time = datetime.now()  # Get current date and time
                print(f"Recognition time: {current_time}")  # Print recognition time
                c.execute("SELECT COUNT(*) FROM detected_faces WHERE student_id = ?", (student_id,))
                count = c.fetchone()[0]
                if count == 0:  # If the student_id does not exist, insert it
                    c.execute("INSERT INTO detected_faces (student_id, timestamp) VALUES (?, ?)", (student_id, current_time))
                    conn.commit()
                else:
                    print(f"{student_id} is already in the database. Skipping insertion.")
            else:
                print("No match within threshold.")
        else:
            print("No matches found.")
    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break
conn.close()
cap.release()
cv2.destroyAllWindows()