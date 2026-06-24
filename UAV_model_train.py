from ultralytics import YOLO 

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")

    results = model.train(
        data=r"C:\UAV-Crop_disease_detection\Multi-Crop Disease Dataset\data.yaml",
        save=True,
        epochs=30,
        imgsz=512,
        batch=16,
        name="UAV_crop_detect_model",
        device=0,
        workers=4,
        cache=False,   
        amp=True,
        optimizer="SGD",
    )