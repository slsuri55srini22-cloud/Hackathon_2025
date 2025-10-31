from google.cloud import vision
#from google.cloud.vision import type

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\Administrator\Documents\Confidential\upheld-pursuit-476707-e1-d6a047bc64f3.json"

def analyze_image(image_path):
    # Initialize the Vision API client
    client = vision.ImageAnnotatorClient()

    # Load the image into memory
    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Create an image object
    image = vision.Image(content=content)

    # Perform label detection on the image
    response = client.label_detection(image=image)
    labels = response.label_annotations

    print("Labels detected:")
    for label in labels:
        print(f"{label.description} (confidence: {label.score:.2f})")

    # Perform text detection (OCR) on the image
    text_response = client.text_detection(image=image)
    texts = text_response.text_annotations

    if texts:
        print("\nDetected Text:")
        for text in texts:
            print(f"Detected text: {text.description}")
    else:
        print("\nNo text detected.")

    # Perform face detection
    face_response = client.face_detection(image=image)
    faces = face_response.face_annotations

    if faces:
        print("\nFaces detected:")
        for face in faces:
            print(f"Joy: {face.joy_likelihood}, Anger: {face.anger_likelihood}, Sorrow: {face.sorrow_likelihood}")
    else:
        print("\nNo faces detected.")

    # Perform landmark detection
    landmark_response = client.landmark_detection(image=image)
    landmarks = landmark_response.landmark_annotations

    if landmarks:
        print("\nLandmarks detected:")
        for landmark in landmarks:
            print(f"Landmark: {landmark.description}")
    else:
        print("\nNo landmarks detected.")

    # Perform logo detection
    logo_response = client.logo_detection(image=image)
    logos = logo_response.logo_annotations

    if logos:
        print("\nLogos detected:")
        for logo in logos:
            print(f"Logo: {logo.description}")
    else:
        print("\nNo logos detected.")

if __name__ == "__main__":

    image_path = r"C:\Users\Administrator\Documents\files\Power-State-Failure-BSOD.jpeg"  # Path to the image you want to analyze
    analyze_image(image_path)