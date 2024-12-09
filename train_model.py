import face_recognition
import os
import pickle

image_dir = "processed_images"
embeddings = {}
print(1)

# Generate embeddings for each student
for student_id in os.listdir(image_dir):
    print(2)
    student_path = os.path.join(image_dir, student_id)
    student_embeddings = []

    for img_name in os.listdir(student_path):
        print(3)
        img_path = os.path.join(student_path, img_name)
        img = face_recognition.load_image_file(img_path)
        encodings = face_recognition.face_encodings(img)
        if encodings:
            print(4)
            student_embeddings.append(encodings[0])  # Use the first encoding
    print(5)

    embeddings[student_id] = student_embeddings
print(6)
# Save embeddings to a file
with open("embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

