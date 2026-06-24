# 🌿 UAV Crop Disease Detection using YOLOv8

<p align="center">
  <img src="https://img.shields.io/badge/Model-YOLOv8n-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Dataset-42%2C000%20Images-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Classes-30%20Diseases-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Platform-UAV%20%2F%20Drone-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Ultralytics-purple?style=for-the-badge" />
</p>

---

## 📌 Project Overview

This project uses a **YOLOv8n (nano)** object detection model trained on a large-scale multi-crop disease dataset to detect and classify **30 different crop diseases** from aerial UAV/drone imagery in real time.

The goal is to help farmers and agricultural experts identify plant diseases early — before they spread across entire fields — using drone-based surveillance instead of manual inspection.

> **Detected Example:**  
> `radish_black_leaf_spot` → 0.78 confidence  
> `banana_yb_sigatoka` → 0.53 confidence

---

## 🚁 Why UAV-Based Detection?

| Traditional Method | UAV + AI Method |
|---|---|
| Manual field inspection | Automated aerial scanning |
| Slow, labor-intensive | Fast, covers large areas |
| Misses early-stage disease | Detects early symptoms |
| Expensive (human labor) | Cost-effective at scale |
| Limited to ground view | Bird's eye view of entire farm |

---

## 🧠 Model Details

| Parameter | Value |
|---|---|
| Architecture | YOLOv8n (Nano) |
| Framework | Ultralytics |
| Input Size | 512 × 512 px |
| Epochs | 30 |
| Batch Size | 16 |
| Optimizer | SGD |
| Mixed Precision (AMP) | ✅ Enabled |
| Device | GPU (CUDA) |
| Dataset Size | ~42,000 labeled images |
| Number of Classes | 30 |

---

## 🌱 Detected Disease Classes (30)

The model can detect diseases across multiple crops including:

- 🍌 **Banana** — `banana_bract_mosaic_virus`, `banana_cordana`, `banana_healthy`, `banana_insect`, `banana_yb_sigatoka`, and more
- 🌿 **Radish** — `radish_black_leaf_spot`, `radish_healthy`
- 🌾 **Multiple Crops** — 30 total disease/healthy classes

> Full class list available in `Multi-Crop Disease Dataset/data.yaml`

---

## 📁 Project Structure

```
UAV-Crop_disease_detection/
│
├── UAV_model_train.py          # YOLOv8 training script
├── Disease_detect.py           # Inference / detection script
├── .gitignore                  # Excludes weights & dataset images
├── README.md                   # This file
│
└── Multi-Crop Disease Dataset/
    └── data.yaml               # Dataset config (paths + class names)
```

> ⚠️ Dataset images and model weights are **not included** in this repo due to size.  
> Download links are provided below.

---

## ⬇️ Downloads

| File | Link |
|---|---|
| Trained Weights (`best.pt`) | [Download from Google Drive](https://drive.google.com/file/d/1RfDHQ3gm__V3zgx8sxGLC-tARz6s9ac3/view?usp=drive_link) |
| Full Dataset (42K images) | [Roboflow Project](https://app.roboflow.com/multicrop-disease/custom-workflow-object-detection-2nqxa) |

> Replace `#` with your actual Google Drive link after uploading `best.pt`

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/UAV-Crop_disease_detection.git
cd UAV-Crop_disease_detection
```

### 2. Install Dependencies
```bash
pip install ultralytics
```

### 3. Download Weights
Download `best.pt` from the link above and place it at:
```
runs/detect/UAV_crop_detect_model/weights/best.pt
```

### 4. Run Detection on an Image
```bash
python Disease_detect.py
```

### 5. Train from Scratch (Optional)
```bash
python UAV_model_train.py
```

---

## 📊 Training Configuration

```python
model.train(
    data="Multi-Crop Disease Dataset/data.yaml",
    epochs=30,
    imgsz=512,
    batch=16,
    optimizer="SGD",
    amp=True,
    device=0,
    workers=4,
    name="UAV_crop_detect_model"
)
```

---

## 🖼️ Sample Results

| Input | Detection |
|---|---|
| Radish leaf image | `radish_black_leaf_spot` — 78% confidence |
| Banana plant image | `banana_yb_sigatoka` — 53% confidence |

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Ultralytics YOLOv8**
- **PyTorch** (CUDA)
- **Roboflow** (Dataset source)
- **OpenCV**

---

## 👨‍💻 Team

| Name | Role |
|---|---|
| Yash Raj | Model Training, Detection Pipeline |
| Harshit Sharma | Collaborator |

**Institution:** KCC Institute of Technology and Management, Greater Noida  
**Branch:** B.Tech CSE (AI & ML) — Batch 2029

---

## 📄 License

This project is for academic and research purposes only.  
Dataset sourced from Roboflow — license: **Private** (see `data.yaml`)

---

<p align="center">Made with 💚 for Smart Agriculture | YOLOv8 + UAV = Future of Farming</p>
