from ultralytics import YOLO


model = YOLO( r"C:\UAV-Crop_disease_detection\runs\detect\UAV_crop_detect_model\weights\best.pt")

results = model.predict(
    source=r"C:\UAV-Crop_disease_detection\Screenshot 2026-06-24 115208.png",
    save=True,  
    conf = 0.20, 
    show=True  )

