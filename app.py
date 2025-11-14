from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
import cv2, numpy as np
from ultralytics import YOLO
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load model
model = YOLO("best.pt")  # trained model

# Disease precautions dictionary
DISEASE_INFO =  {
    "Anthracnose": {
        "description": "Fungal disease causing black spots on mango.",
        "cause": "Caused by the Colletotrichum gloeosporioides fungus under humid conditions.",
        "precautions": "Use fungicides, prune infected areas, avoid overhead irrigation."
    },
    "Healthy": {
        "description": "No disease detected.",
        "cause": "N/A",
        "precautions": "Maintain regular care and monitoring."
    },
    "Bacterial Canker": {
        "description": "Bacterial infection causing lesions on fruit and leaves.",
        "cause": "Caused by Xanthomonas campestris bacteria spreading via water splashes.",
        "precautions": "Use copper-based bactericides, remove infected fruits/leaves."
    },
    "Scab": {
        "description": "Fungal disease causing corky lesions on skin.",
        "cause": "Caused by Elsinoë mangiferae fungus, thrives in wet weather.",
        "precautions": "Apply fungicides, remove fallen infected leaves and fruits."
    },
    "StemEndRot": {
        "description": "Fungal rot at stem end after harvest.",
        "cause": "Caused by fungi like Alternaria alternata during storage.",
        "precautions": "Harvest carefully, store properly, apply post-harvest fungicides."
    }
}

# Helper functions
def generate_edge_map(img_bgr):
    gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5),0)
    edges = cv2.Canny(blur, 30, 100)
    return edges

def create_4channel_image(img_bgr, edge_map):
    b, g, r = cv2.split(img_bgr)
    fused = cv2.merge([b, g, r, edge_map])
    return fused

def overlay_edge_for_display(img_bgr, edge_map, alpha=0.2):
    b, g, r = cv2.split(img_bgr)
    g = cv2.addWeighted(g, 1.0, edge_map, alpha, 0)
    return cv2.merge([b, g, r])

def process_image(file_bytes):
    arr = np.frombuffer(file_bytes, np.uint8)
    img_bgr = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    if img_bgr is None:
        raise ValueError("Failed to read uploaded image!")

    edge = generate_edge_map(img_bgr)

    # Fused image for display (without bounding boxes)
    overlay_img = overlay_edge_for_display(img_bgr, edge, alpha=0.2)
    overlay_path = "static/temp_overlay.png"
    cv2.imwrite(overlay_path, overlay_img)

    # 4-channel fused image for YOLO
    fused_4ch = create_4channel_image(img_bgr, edge)
    fused_path = "static/temp_fused.png"
    cv2.imwrite(fused_path, fused_4ch)

    # YOLO inference
    results = model.predict(
        source=fused_path,
        imgsz=640,
        conf=0.25,
        save=True,
        project="static",
        name="out",
        exist_ok=True
    )

    # Annotated image with bounding boxes
    boxed_img = results[0].plot()
    boxed_img_path = "static/temp_boxed.png"
    cv2.imwrite(boxed_img_path, boxed_img)

    # Get detected class name (first detection for simplicity)
    if len(results[0].boxes) > 0:
        disease_class = results[0].boxes.cls[0].item()
        disease_name = model.names[int(disease_class)]
    else:
        disease_name = "Healthy"

    info = DISEASE_INFO.get(disease_name, DISEASE_INFO["Healthy"])
    description = info.get("description", "")
    cause = info.get("cause", "")
    precautions = info.get("precautions", "No info available")

    return {
        "original_image": overlay_path,
        "annotated_image": boxed_img_path,
        "disease_name": disease_name,
        "description": description,
        "cause": cause,
        "precautions": precautions
    }


# Routes
@app.get("/")
def home():
    html = open("static/index.html").read()
    return HTMLResponse(html)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    result = process_image(content)
    return JSONResponse(result)
