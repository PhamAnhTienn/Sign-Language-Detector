import os
import cv2
import time 
import uuid

IMAGE_PATH = "CollectedImages"

labels = ['Thanks', 'Yes', 'No', 'ILoveYou', 'Hello', 'Special']

number_of_images = 5

for label in labels:
    image_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(image_path)
    
    #open cam
    cap = cv2.VideoCapture(0)
    print(f"Caturing images for {label}")
    time.sleep(3)
    
    for num in range(number_of_images):
        ret, frame = cap.read()
        image_name = os.path.join(IMAGE_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(image_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    
    cap.release()