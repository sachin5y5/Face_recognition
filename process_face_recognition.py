import cv2
import os

input_dir = "cropped_images"  # Update this path
output_dir = "processed_images"  # Update this path

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Process images
for student_id in os.listdir(input_dir):
    student_path = os.path.join(input_dir, student_id)
    
    # Ensure student_path is a directory
    if os.path.isdir(student_path):
        save_path = os.path.join(output_dir, student_id)
        os.makedirs(save_path, exist_ok=True)

        for img_name in os.listdir(student_path):
            img_path = os.path.join(student_path, img_name)
            img = cv2.imread(img_path)

            if img is not None:
                resized_img = cv2.resize(img, (128, 128))  # Resize to 128x128
                cv2.imwrite(os.path.join(save_path, img_name), resized_img)
                print(f"Processed and saved: {img_name}")
            else:
                print(f"Warning: Unable to read image {img_path}")
    else:
        print(f"Skipping non-directory item: {student_path}")