# 🎭 VisionGuard — Deepfake Detection System

### *AI-powered truth verification for images & videos*

VisionGuard is an advanced deepfake detection system built using **TensorFlow**, **Keras**, and **Streamlit**, designed to classify media as **Real** or **Fake** with high accuracy.

Built for the *MumbaiHacks Hackathon*, this project focuses on **ethical AI**, real-time detection, and a clean, interactive frontend.

---

## 🚀 Features

### 🔍 **Deepfake Classifier (CNN Model)**

* Custom-trained Convolutional Neural Network
* Evaluates real vs fake media
* Supports `.jpg`, `.png`, `.mp4*` (optional based on your project)

### 🧪 **Accuracy Evaluation**

* Built-in accuracy checker (`accuracy.py`)
* Validation dataset loader
* Displays evaluation metrics instantly

### 🎨 **Interactive UI (Streamlit)**

* Minimal, modern interface
* Drag-and-drop media upload
* Real-time prediction with confidence score
* Gradient-styled headers and animations

### 📂 **Clean Dataset Pipeline**

* Uses `ImageDataGenerator`
* Supports train/val folder structures
* Auto-preprocessing & augmentation

---

## 🧠 Model Architecture

The deepfake detector is powered by a lightweight CNN:

* Convolution layers (feature extraction)
* Batch normalization
* MaxPooling layers
* Dense classifier with sigmoid activation
* Trained on a curated mini deepfake dataset

## ✨ Future Roadmap

* 🔗 Add video-based frame extraction
* 🌐 Deploy the app on Cloud (Render / HuggingFace / AWS)
* 📶 Live camera detection
* 🧩 Add Xception-based advanced architectures
* 🔒 Add explainability: Grad-CAM heatmaps

---

## 🏆 Why This Project?

Deepfakes are rapidly increasing—DetectoAI aims to:

* Promote **media integrity**
* Make detection **accessible**
* Help users verify content confidently
* Demonstrate **AI for social good**


![WhatsApp Image 2025-11-29 at 5 43 45 AM](https://github.com/user-attachments/assets/2eec20f1-7bce-4f49-98fc-cf4c5631cfb8)
![WhatsApp Image 2025-11-29 at 5 45 32 AM](https://github.com/user-attachments/assets/e11492a9-70e7-48fd-805e-5adc1f3fc65a)
![WhatsApp Image 2025-11-29 at 5 45 33 AM](https://github.com/user-attachments/assets/c88e1a5f-7262-49a4-81b1-c99cb3381f40)
![WhatsApp Image 2025-11-29 at 5 48 34 AM](https://github.com/user-attachments/assets/8d6dcda0-8612-42b3-9522-60cf5ff5f631)
