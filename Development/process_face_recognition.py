# # # # import cv2
# # # # import os
# # # # import shutil

# # # # input_dir = "cropped_images"
# # # # output_dir = "processed_images"

# # # # # Create output directory if not exists
# # # # os.makedirs(output_dir, exist_ok=True)

# # # # # Process images
# # # # for student_id in os.listdir(input_dir):
# # # #     student_path = os.path.join(input_dir, student_id)
# # # #     # Ensure student_path is a directory
# # # #     if os.path.isdir(student_path):
# # # #         images = [img for img in os.listdir(student_path) if img.endswith(('.png', '.jpg', '.jpeg'))]
# # # #         if not images:
# # # #             print(f"No images found in folder: {student_path}")
# # # #             continue

# # # #         # Display the first image in the folder for renaming
# # # #         first_image_path = os.path.join(student_path, images[0])
# # # #         img = cv2.imread(first_image_path)
# # # #         if img is not None:
# # # #             cv2.imshow(f"Folder: {student_id}", img)
# # # #             new_name = input(f"Enter the new name for the folder '{student_id}': ")
# # # #             cv2.destroyAllWindows()
# # # #         else:
# # # #             print(f"Warning: Unable to read image {first_image_path}")
# # # #             continue

# # # #         # Rename the folder and move it to the processed_images directory
# # # #         save_path = os.path.join(output_dir, new_name)
# # # #         os.makedirs(save_path, exist_ok=True)
# # # #         for img_name in images:
# # # #             img_path = os.path.join(student_path, img_name)
# # # #             img = cv2.imread(img_path)
# # # #             if img is not None:
# # # #                 resized_img = cv2.resize(img, (128, 128))  # Resize to 128x128
# # # #                 cv2.imwrite(os.path.join(save_path, img_name), resized_img)
# # # #                 print(f"Processed and saved: {img_name}")
# # # #             else:
# # # #                 print(f"Warning: Unable to read image {img_path}")

# # # #         # Delete the original folder from cropped_images
# # # #         shutil.rmtree(student_path)
# # # #         print(f"Folder '{student_id}' renamed to '{new_name}' and moved to '{output_dir}'")
# # # #     else:
# # # #         print(f"Skipping non-directory item: {student_path}")

# # # import cv2
# # # import os
# # # import shutil
# # # from sklearn.model_selection import train_test_split
# # # from sklearn.svm import SVC
# # # import numpy as np
# # # import pickle

# # # input_dir = "cropped_images"
# # # output_dir = "processed_images"
# # # model_output_path = "trained_model.pkl"

# # # # Create output directory if not exists
# # # os.makedirs(output_dir, exist_ok=True)

# # # # Process images
# # # for student_id in os.listdir(input_dir):
# # #     student_path = os.path.join(input_dir, student_id)
# # #     # Ensure student_path is a directory
# # #     if os.path.isdir(student_path):
# # #         images = [img for img in os.listdir(student_path) if img.endswith(('.png', '.jpg', '.jpeg'))]
# # #         if not images:
# # #             print(f"No images found in folder: {student_path}")
# # #             continue

# # #         # Display the first image in the folder for renaming
# # #         first_image_path = os.path.join(student_path, images[0])
# # #         img = cv2.imread(first_image_path)
# # #         if img is not None:
# # #             cv2.imshow(f"Folder: {student_id}", img)
# # #             new_name = input(f"Enter the new name for the folder '{student_id}': ")
# # #             cv2.destroyAllWindows()
# # #         else:
# # #             print(f"Warning: Unable to read image {first_image_path}")
# # #             continue

# # #         # Rename the folder and move it to the processed_images directory
# # #         save_path = os.path.join(output_dir, new_name)
# # #         os.makedirs(save_path, exist_ok=True)
# # #         for img_name in images:
# # #             img_path = os.path.join(student_path, img_name)
# # #             img = cv2.imread(img_path)
# # #             if img is not None:
# # #                 resized_img = cv2.resize(img, (128, 128))  # Resize to 128x128
# # #                 cv2.imwrite(os.path.join(save_path, img_name), resized_img)
# # #                 print(f"Processed and saved: {img_name}")
# # #             else:
# # #                 print(f"Warning: Unable to read image {img_path}")

# # #         # Delete the original folder from cropped_images
# # #         shutil.rmtree(student_path)
# # #         print(f"Folder '{student_id}' renamed to '{new_name}' and moved to '{output_dir}'")
# # #     else:
# # #         print(f"Skipping non-directory item: {student_path}")

# # # # Train model
# # # def extract_features_and_labels(data_dir):
# # #     features = []
# # #     labels = []
# # #     for label in os.listdir(data_dir):
# # #         label_path = os.path.join(data_dir, label)
# # #         if os.path.isdir(label_path):
# # #             for img_name in os.listdir(label_path):
# # #                 img_path = os.path.join(label_path, img_name)
# # #                 img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
# # #                 if img is not None:
# # #                     img = cv2.resize(img, (128, 128))  # Ensure consistent size
# # #                     features.append(img.flatten())
# # #                     labels.append(label)
# # #     return np.array(features), np.array(labels)

# # # print("Extracting features and labels...")
# # # X, y = extract_features_and_labels(output_dir)

# # # print("Splitting data into training and testing sets...")
# # # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # print("Training the model...")
# # # model = SVC(kernel='linear', probability=True)
# # # model.fit(X_train, y_train)

# # # print("Saving the trained model...")
# # # with open(model_output_path, 'wb') as model_file:
# # #     pickle.dump(model, model_file)

# # # print("Model training complete. Saved to:", model_output_path)

# # import cv2
# # import os
# # import shutil
# # from sklearn.model_selection import train_test_split
# # from sklearn.svm import SVC
# # import numpy as np
# # import pickle

# # input_dir = "cropped_images"
# # output_dir = "processed_images"
# # model_output_path = "trained_model.pkl"

# # # Create output directory if not exists
# # os.makedirs(output_dir, exist_ok=True)

# # # Process images
# # for student_id in os.listdir(input_dir):
# #     student_path = os.path.join(input_dir, student_id)
# #     # Ensure student_path is a directory
# #     if os.path.isdir(student_path):
# #         images = [img for img in os.listdir(student_path) if img.endswith(('.png', '.jpg', '.jpeg'))]
# #         if not images:
# #             print(f"No images found in folder: {student_path}")
# #             continue

# #         # Display the first image in the folder for renaming
# #         first_image_path = os.path.join(student_path, images[0])
# #         img = cv2.imread(first_image_path)
# #         if img is not None:
# #             cv2.imshow(f"Folder: {student_id}", img)
# #             new_name = input(f"Enter the new name for the folder '{student_id}': ")
# #             cv2.destroyAllWindows()
# #         else:
# #             print(f"Warning: Unable to read image {first_image_path}")
# #             continue

# #         # Rename the folder and move it to the processed_images directory
# #         save_path = os.path.join(output_dir, new_name)
# #         os.makedirs(save_path, exist_ok=True)
# #         for img_name in images:
# #             img_path = os.path.join(student_path, img_name)
# #             img = cv2.imread(img_path)
# #             if img is not None:
# #                 resized_img = cv2.resize(img, (128, 128))  # Resize to 128x128
# #                 cv2.imwrite(os.path.join(save_path, img_name), resized_img)
# #                 print(f"Processed and saved: {img_name}")
# #             else:
# #                 print(f"Warning: Unable to read image {img_path}")

# #         # Delete the original folder from cropped_images
# #         shutil.rmtree(student_path)
# #         print(f"Folder '{student_id}' renamed to '{new_name}' and moved to '{output_dir}'")
# #     else:
# #         print(f"Skipping non-directory item: {student_path}")

# # # Train model
# # def extract_features_and_labels(data_dir):
# #     features = []
# #     labels = []
# #     for label in os.listdir(data_dir):
# #         label_path = os.path.join(data_dir, label)
# #         if os.path.isdir(label_path):
# #             for img_name in os.listdir(label_path):
# #                 img_path = os.path.join(label_path, img_name)
# #                 img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
# #                 if img is not None:
# #                     img = cv2.resize(img, (128, 128))  # Ensure consistent size
# #                     features.append(img.flatten())
# #                     labels.append(label)
# #     return np.array(features), np.array(labels)

# # print("Extracting features and labels...")
# # X, y = extract_features_and_labels(output_dir)

# # # Check if there are at least two classes
# # if len(set(y)) < 2:
# #     print("Error: The dataset must contain at least two classes for training.")
# #     print("Add more data with different labels and try again.")
# # else:
# #     if len(X) < 2:
# #         print("Not enough samples to split into training and testing sets. Using all data for training.")
# #         X_train, y_train = X, y
# #         X_test, y_test = X, y  # Optional: Use the same data for testing
# #     else:
# #         print("Splitting data into training and testing sets...")
# #         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# #     print("Training the model...")
# #     model = SVC(kernel='linear', probability=True)
# #     model.fit(X_train, y_train)

# #     print("Saving the trained model...")
# #     with open(model_output_path, 'wb') as model_file:
# #         pickle.dump(model, model_file)

# #     print("Model training complete. Saved to:", model_output_path)

# # filepath: [process_face_recognition.py](http://_vscodecontentref_/3)
# import cv2
# import os
# import shutil
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
# import numpy as np
# import pickle

# input_dir = "cropped_images"
# output_dir = "processed_images"
# model_output_path = "trained_model.pkl"

# # Create output directory if not exists
# os.makedirs(output_dir, exist_ok=True)

# # Process images
# for student_id in os.listdir(input_dir):
#     student_path = os.path.join(input_dir, student_id)
#     # Ensure student_path is a directory
#     if os.path.isdir(student_path):
#         images = [img for img in os.listdir(student_path) if img.endswith(('.png', '.jpg', '.jpeg'))]
#         if not images:
#             print(f"No images found in folder: {student_path}")
#             continue

#         # Display the first image in the folder for renaming
#         first_image_path = os.path.join(student_path, images[0])
#         img = cv2.imread(first_image_path)
#         if img is not None:
#             cv2.imshow(f"Folder: {student_id}", img)
#             new_name = input(f"Enter the new name for the folder '{student_id}': ")
#             cv2.destroyAllWindows()
#         else:
#             print(f"Warning: Unable to read image {first_image_path}")
#             continue

#         # Rename the folder and move it to the processed_images directory
#         save_path = os.path.join(output_dir, new_name)
#         os.makedirs(save_path, exist_ok=True)
#         for img_name in images:
#             img_path = os.path.join(student_path, img_name)
#             img = cv2.imread(img_path)
#             if img is not None:
#                 resized_img = cv2.resize(img, (128, 128))  # Resize to 128x128
#                 cv2.imwrite(os.path.join(save_path, img_name), resized_img)
#                 print(f"Processed and saved: {img_name}")
#             else:
#                 print(f"Warning: Unable to read image {img_path}")

#         # Delete the original folder from cropped_images
#         shutil.rmtree(student_path)
#         print(f"Folder '{student_id}' renamed to '{new_name}' and moved to '{output_dir}'")
#     else:
#         print(f"Skipping non-directory item: {student_path}")

# # Train model
# def extract_features_and_labels(data_dir):
#     features = []
#     labels = []
#     for label in os.listdir(data_dir):
#         label_path = os.path.join(data_dir, label)
#         if os.path.isdir(label_path):
#             for img_name in os.listdir(label_path):
#                 img_path = os.path.join(label_path, img_name)
#                 img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
#                 if img is not None:
#                     img = cv2.resize(img, (128, 128))  # Ensure consistent size
#                     features.append(img.flatten())
#                     labels.append(label)
#     return np.array(features), np.array(labels)

# print("Extracting features and labels...")
# X, y = extract_features_and_labels(output_dir)

# # Check if there are at least two classes
# if len(set(y)) < 2:
#     print("Error: The dataset must contain at least two classes for training.")
#     print("Add more data with different labels and try again.")
# else:
#     if len(X) < 2:
#         print("Not enough samples to split into training and testing sets. Using all data for training.")
#         X_train, y_train = X, y
#         X_test, y_test = X, y  # Optional: Use the same data for testing
#     else:
#         print("Splitting data into training and testing sets...")
#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#     print("Training the model...")
#     model = SVC(kernel='linear', probability=True)
#     model.fit(X_train, y_train)

#     print("Saving the trained model...")
#     with open(model_output_path, 'wb') as model_file:
#         pickle.dump(model, model_file)

#     print("Model training complete. Saved to:", model_output_path)

import cv2
import os
import shutil
import face_recognition
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np

input_dir = "cropped_images"
output_dir = "processed_images"
model_output_path = "trained_model.pkl"
embeddings_output_path = "embeddings.pkl"

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Process images
for student_id in os.listdir(input_dir):
    student_path = os.path.join(input_dir, student_id)
    # Ensure student_path is a directory
    if os.path.isdir(student_path):
        images = [img for img in os.listdir(student_path) if img.endswith(('.png', '.jpg', '.jpeg'))]
        if not images:
            print(f"No images found in folder: {student_path}")
            continue

        # Display the first image in the folder for renaming
        first_image_path = os.path.join(student_path, images[0])
        img = cv2.imread(first_image_path)
        if img is not None:
            cv2.imshow(f"Folder: {student_id}", img)
            new_name = input(f"Enter the new name for the folder '{student_id}': ")
            cv2.destroyAllWindows()
        else:
            print(f"Warning: Unable to read image {first_image_path}")
            continue

        # Rename the folder and move it to the processed_images directory
        save_path = os.path.join(output_dir, new_name)
        os.makedirs(save_path, exist_ok=True)
        for img_name in images:
            img_path = os.path.join(student_path, img_name)
            img = cv2.imread(img_path)
            if img is not None:
                resized_img = cv2.resize(img, (128, 128))  # Resize to 128x128
                cv2.imwrite(os.path.join(save_path, img_name), resized_img)
                print(f"Processed and saved: {img_name}")
            else:
                print(f"Warning: Unable to read image {img_path}")

        # Delete the original folder from cropped_images
        shutil.rmtree(student_path)
        print(f"Folder '{student_id}' renamed to '{new_name}' and moved to '{output_dir}'")
    else:
        print(f"Skipping non-directory item: {student_path}")

# Generate embeddings for each student
def generate_student_embeddings(data_dir):
    embeddings = {}
    for student_id in os.listdir(data_dir):
        student_path = os.path.join(data_dir, student_id)
        if os.path.isdir(student_path):
            student_embeddings = []
            for img_name in os.listdir(student_path):
                img_path = os.path.join(student_path, img_name)
                img = face_recognition.load_image_file(img_path)
                encodings = face_recognition.face_encodings(img)
                if encodings:
                    student_embeddings.append(encodings[0])  # Use the first encoding
            embeddings[student_id] = student_embeddings
    return embeddings

print("Generating embeddings for each student...")
embeddings = generate_student_embeddings(output_dir)

print("Saving embeddings to file...")
with open(embeddings_output_path, 'wb') as embeddings_file:
    pickle.dump(embeddings, embeddings_file)

print(f"Embeddings saved to {embeddings_output_path}")

# Train model
def extract_features_and_labels(data_dir):
    features = []
    labels = []
    for label in os.listdir(data_dir):
        label_path = os.path.join(data_dir, label)
        if os.path.isdir(label_path):
            for img_name in os.listdir(label_path):
                img_path = os.path.join(label_path, img_name)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is not None:
                    img = cv2.resize(img, (128, 128))  # Ensure consistent size
                    features.append(img.flatten())
                    labels.append(label)
    return np.array(features), np.array(labels)

print("Extracting features and labels...")
X, y = extract_features_and_labels(output_dir)

# Check if there are at least two classes
if len(set(y)) < 2:
    print("Error: The dataset must contain at least two classes for training.")
    print("Add more data with different labels and try again.")
else:
    if len(X) < 2:
        print("Not enough samples to split into training and testing sets. Using all data for training.")
        X_train, y_train = X, y
        X_test, y_test = X, y  # Optional: Use the same data for testing
    else:
        print("Splitting data into training and testing sets...")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training the model...")
    model = SVC(kernel='linear', probability=True)
    model.fit(X_train, y_train)

    print("Saving the trained model...")
    with open(model_output_path, 'wb') as model_file:
        pickle.dump(model, model_file)

    print("Model training complete. Saved to:", model_output_path)