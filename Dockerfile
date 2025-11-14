# Dockerfile (CPU)
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential ffmpeg libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps (ultralytics, torch - CPU)
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
