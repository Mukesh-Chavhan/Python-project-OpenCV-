import cv2
import os
import time
import matplotlib.pyplot as plt
from deepface import DeepFace

def most_common_string(array_string):
    string_count = {}
    for string in array_string:
        if string in string_count:
            string_count[string] += 1
        else:
            string_count[string] = 1

    max_count = 0
    max_string = ""
    for string, count in string_count.items():
        if count > max_count:
            max_count = count
            max_string = string

    print("Most commonly repeated string: ", max_string)
    print("Count: ", max_count)



NUM_PHOTOS = 5

photos = []

cap = cv2.VideoCapture(0)

for i in range(NUM_PHOTOS):

    cv2.waitKey()

    # Capture a photo
    ret, frame = cap.read()

    # Generate a filename based on the current timestamp
    filename = f"photo_{time.time()}.jpg"

    # Generate the file path for the photo
    filepath = os.path.join("images", filename)

    # Save the photo to the disk
    cv2.imwrite(filepath, frame)

    photos.append(filepath)

# Release the camera
cap.release()

string_array=[]

print("Saved photo locations:")
size=len(photos)
for i in range(0,size-1):

    img = cv2.imread(photos[i])
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    pred = DeepFace.analyze(img)
    emotions_dict = pred[0]['emotion']
    emotion = max(emotions_dict, key=emotions_dict.get)
    string_array.append(emotion)
most_common_string(string_array) 

# Destroy all OpenCV windows
cv2.destroyAllWindows()

