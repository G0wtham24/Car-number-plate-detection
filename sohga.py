from ultralytics import YOLO
model=YOLO("yolov8m-seg-custom.pt")
model.predict(source="136.jpg" , show=True ,save=True  , hide_labels=True, hide_conf=True, conf=0.5,save_txt=False,save_crop=False,line_thickness=2)
# In source give images(136 images)