🍃 Advanced Mango Disease Detection Using YOLO + Edge Enhancement

A deep-learning powered system for accurate mango leaf disease detection using a YOLO model enhanced with Canny edge features. The project integrates Grey Wolf Optimization (GWO) for hyperparameter tuning, improving the overall accuracy and robustness of the model.

This system helps in early detection of leaf infections, supporting farmers and agriculture analysts in making quick decisions.

🚀 Features

⚡ YOLO-based detection for high-speed and accurate disease classification

🖼 Canny edge enhancement channel for improved pattern extraction

🧠 GWO hyperparameter optimization to maximize performance

🧹 Custom dataset preprocessing pipeline

📈 High accuracy with clear visualization outputs

🌱 Useful for precision agriculture and disease management

🛠 Tech Stack & Skills Used

Python, OpenCV, YOLO, Deep Learning, Computer Vision,
Canny Edge Detection, Grey Wolf Optimization (GWO),
Image Preprocessing, Model Training & Evaluation, NumPy, Matplotlib

📂 Project Structure
📦 mango-disease-detection
 ┣ 📁 dataset/
 ┣ 📁 edge_preprocessing/
 ┣ 📁 yolo_model/
 ┣ 📁 gwo_optimization/
 ┣ 📁 results/
 ┣ 📄 train.py
 ┣ 📄 detect.py
 ┣ 📄 preprocess.py
 ┣ 📄 requirements.txt
 ┗ 📄 README.md

📥 Installation
1. Clone the repository
git clone https://github.com/your-username/mango-disease-detection.git

2. Install dependencies
pip install -r requirements.txt

🧹 Data Preprocessing

Run the preprocessing script to apply:

Resizing

Normalization

Edge detection (Canny)

Channel merging

python preprocess.py

🧠 Training the YOLO Model
python train.py


Includes:

YOLO backbone

Edge-enhanced input

GWO for hyperparameter tuning

🎯 Running Detection
python detect.py --image sample_leaf.jpg

📊 Results & Visualizations

Includes:

YOLO bounding box predictions

Edge-enhanced visual interpretation

Accuracy/loss curves

GWO optimization convergence plot

📝 Project Description (Short Version)

A YOLO-based mango leaf disease detection system enhanced with Canny edge features and optimized using GWO. Designed to improve early disease identification, delivering high accuracy and strong interpretability for agricultural use cases.

💡 Motivation

Agriculture suffers major losses due to late detection of plant diseases. This project focuses on creating a fast, reliable, and automated detection system that assists farmers and researchers in preventing crop damage early.

📌 Future Enhancements

Integration with mobile application

Drone-assisted leaf scanning

Deployment using TensorRT / ONNX

Real-time field-level detection system
