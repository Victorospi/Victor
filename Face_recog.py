from ultralytics import YOLO
from collections import Counter
from pathlib import Path

def detect_objects(model: YOLO, image_pass: str) -> None:
    ''' 
    Peform object detecting
    param model - Downloaded YOLO model
    param image_pass - Way to image for detection
    '''
    print("[INFO] start objects recognize...")
    results = model(image_pass, verbose=False)[0]

    if results.names and results.boxes is not None:
        #get classify for object classes
        labels = results.boxes.cls.tolist()
        #change ID to class names
        label_names = [results.names[int(cls)] for cls in labels]
        #count each unic object
        counts = Counter(label_names)

        print("[INFO] objects recognized:")
        for label, count in counts.items():
            print(f'[+] {label}: {count}')
    else:
        print('[!] objects not recognized')

def main():
    model = YOLO('yolov8n.pt')

    detect_objects(model,'\images\img_exmpl_1.jpg')

if __name__ == '__main__':
   main()

