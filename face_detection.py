



import cv2
import dlib
import os

# Load Dlib's pre-trained face detector
detector = dlib.get_frontal_face_detector()

def detect_faces_in_image(image_path):
    # Read the image
    frame = cv2.imread(image_path)
    if frame is None:
        print("Error: Unable to read the image.")
        return

    # Convert frame to grayscale for better performance
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)

    # Create an output folder for cropped faces
    output_folder = "cropped_images"
    os.makedirs(output_folder, exist_ok=True)
    # os.makedirs(output_folder, exist_ok=True)

    # # Ask user for subfolder name
    # subfolder_name = input("Enter the name for the subfolder to save cropped images: ")
    # subfolder_path = os.path.join(output_folder, subfolder_name)
    # os.makedirs(subfolder_path, exist_ok=True)

    # Draw bounding boxes and save cropped faces
    for i, face in enumerate(faces):
        x, y, w, h = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Face Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break
        # Crop the face from the frame
        face_crop = frame[y:y+h, x:x+w]

        subfolder_path=os.path.join(output_folder,f"face_{i}")
        os.makedirs(subfolder_path,exist_ok=True)
        
        # Save the cropped face image
        cropped_image_path = os.path.join(subfolder_path, f"face_{i}.jpg")
        cv2.imwrite(cropped_image_path, face_crop)
        print(f"Cropped face saved: {cropped_image_path}")

    # Show the frame with detected faces
    cv2.imshow("Face Detection", frame)
    cv2.waitKey(0)  # Wait for a key press to close the image window
    cv2.destroyAllWindows()

def detect_faces_in_real_time():
    # Access video feed
    cap = cv2.VideoCapture(0)

# Create the main folder for cropped images if it doesn't exist
    output_folder = "cropped_images"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

    # Convert frame to grayscale for better performance
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
        faces = detector(gray)

    # Draw bounding boxes
        for face in faces:
            x, y, w, h = (face.left(), face.top(), face.width(), face.height())
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Face Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    # Save cropped faces into subfolders
        for i, face in enumerate(faces):
            x, y, w, h = (face.left(), face.top(), face.width(), face.height())
            if y >= 0 and x >= 0 and (y + h) <= frame.shape[0] and (x + w) <= frame.shape[1]:
                face_crop = frame[y:y+h, x:x+w]

        # Create a subfolder for each cropped face
                subfolder_name = f"face_{i}"
                subfolder_path = os.path.join(output_folder, subfolder_name)
                if not os.path.exists(subfolder_path):
                    os.makedirs(subfolder_path)

        # Save the cropped face image
                image_path = os.path.join(subfolder_path, f"{subfolder_name}.jpg")
                cv2.imwrite(image_path, face_crop)

            else:
                print(f"Invalid face coordinates for face {i}: ({x}, {y}, {w}, {h})")


    cap.release()
    cv2.destroyAllWindows()


# Main program
if __name__ == "__main__":
    choice = input("Choose an option:\n1. Detect faces in real-time\n2. Upload an image for face detection\nEnter your choice (1 or 2): ")

    if choice == '1':
        detect_faces_in_real_time()
    elif choice == '2':
        image_path = input("Enter the path of the image: ")
        detect_faces_in_image(image_path)
    else:
        print("Invalid choice. Please enter 1 or 2.")

    output_folder="cropped_images"
    
    subfolders = [f for f in os.listdir(output_folder) if os.path.isdir(os.path.join(output_folder, f))]

# Loop through each subfolder
    for subfolder in subfolders:
        selected_folder_path = os.path.join(output_folder, subfolder)

    # List all images in the selected subfolder
        images = [f for f in os.listdir(selected_folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]

        print(f"\nDisplaying images in subfolder: {subfolder}")

    # Display images one by one
        for img_name in images:
            img_path = os.path.join(selected_folder_path, img_name)
            img = cv2.imread(img_path)

            if img is not None:
                cv2.imshow(f"Image: {img_name}", img)
                cv2.waitKey(0)  # Wait for a key press to display the next image
                cv2.destroyAllWindows()
            else:
                print(f"Warning: Unable to read image {img_path}")

    # Get the new name for the current subfolder
        new_name = input(f"Enter the new name for the subfolder '{subfolder}': ")

    # Rename the subfolder
        new_path = os.path.join(output_folder, new_name)
        os.rename(selected_folder_path, new_path)
        print(f"Renamed '{subfolder}' to '{new_name}' successfully.")

    print("All subfolders have been processed.")

