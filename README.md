MangoCare: Mango Fruit Disease Prediction using Dual-Input Edge-Guided Optimized YOLO Approach
Overview
MangoCare is a lightweight and highly accurate disease detection system designed specifically for mango fruits. It integrates RGB and edge map cues to improve disease detection accuracy while being optimized for efficient deployment on edge devices such as smartphones or drones.

Early and precise mango disease detection is critical for minimizing crop loss and ensuring agricultural sustainability. MangoCare leverages a novel dual-input architecture using an optimized YOLOv8 model enhanced with edge-guided information and hyperparameter tuning.

Model Training
We developed and trained a custom YOLOv8 model, modifying the input channels to accept 4-channel images (RGB + edge map).

Training dataset consisted of approximately 1,500 images of mango fruits covering multiple disease classes.

Edge maps were generated using Canny edge detection with Gaussian blur preprocessing to highlight structural disease features.

The model was initially trained with baseline hyperparameters for 80 epochs.

Hyperparameter optimization was performed using the Grey Wolf Optimizer (GWO) algorithm tuning learning rate, momentum, weight decay, and loss weights.

Final model retraining was done for 20 epochs using optimized hyperparameters for superior performance.

The resulting model balances accuracy and real-time performance, suitable for edge deployment.

Dataset
Dataset consists of real orchard mango fruit images grouped into five disease classes, including Anthracnose, Bacterial Canker, Scab, Stem End Rot, and Healthy.

Images were annotated with YOLO-format bounding box labels.

Data was split into 80% training and 20% validation sets.

Canny edge maps were computed for each image to provide structural features complementary to RGB.

Methodology and Architecture
The proposed approach fuses RGB images and edge maps into a 4-channel input tensor.

The first convolutional layer of pretrained YOLOv8 was adapted to accept 4-channel inputs, initializing the new edge channel weights as the mean of RGB weights.

This integration improves boundary detection of subtle disease lesions often missed by standard RGB-only models.

Training utilizes transfer learning with pretrained weights, combined with evolutionary optimization of key hyperparameters.

The architecture enables efficient disease detection with enhanced sensitivity to disease boundaries and lesion structures.

Results and Discussion
Model evaluation using precision, recall, and mAP metrics showed improved detection performance compared to baseline YOLOv8.

Edge-guided input contributed significantly to better disease boundary localization, especially for Stem End Rot and Healthy classes.

Some subtle diseases like Anthracnose and Scab showed relatively lower detection accuracy due to challenging visual symptoms.

The optimized model exhibits a balanced trade-off between detection accuracy and inference speed, making it practical for real-time use on resource-constrained devices.

Project Structure
text
MANGO_DEPLOY/
├── app.py                  # FastAPI backend and inference code
├── best.pt                 # Trained YOLOv8 model file
├── requirements.txt        # Python dependencies
├── static/                 # Frontend static files
│   ├── index.html
│   ├── style.css
│   └── script.js
├── Dockerfile              # Optional containerization
└── README.md               # This file
How to Use
Run the FastAPI backend which serves the frontend and API endpoints.

Upload mango fruit images via the web interface.

The system shows the original image (with edge enhancement), detected disease bounding boxes, and disease information including cause and precautions.
