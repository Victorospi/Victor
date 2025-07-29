from ultralytics import YOLO
from collections import Counter
from pathlib import Path

def detect_objects(model: YOLO, image_pass: str) -> None:
    ''' 
    Peform detecting, save in to file
    param - model - Downloaded YOLO model
    param - image_pass - Way to image for detection
    '''
    print("[INFO] start objects recognize...")
    results = model(image_pass, verbose=False)[0]

    print(results)

def main():
    model = YOLO('yolov8n.pt')

    detect_objects(model,'\images\ImgExample_footbalTeam.jpg')

if __name__ == '__main__':
   main()

