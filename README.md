# Project EcoSort: AI-Powered Waste Intelligence
**Team:** --Binary Coders | **Track:** Sustainability 
**Status:**  Prototype Development 
##  The Vision
In many urban areas, waste segregation at the source is the biggest bottleneck to recycling. **EcoSort AI** is a real-time vision system that identifies waste (Plastic, Paper, Metal) and provides instant binning instructions to ensure a circular economy

##  Implementation Strategy 
We are building a bridge between high-level AI and real-time execution:
* **The Intelligence:** A custom image classification model trained via **Transfer Learning** on the MobileNetV2 architecture.
* **The Dataset:** 100 curated images of Plastic, Paper, and Metal, including "Environmental Noise" (backgrounds) to ensure real-world accuracy.
* **The Pipeline:** Using **OpenCV** to capture live frames and **TensorFlow** to run predictions locally on the edge.
##  Setup & Prerequisites
To run this project locally, you need Python 3.x installed along with the following libraries:
###  Required Libraries
* **TensorFlow:** To load and execute the Keras (.h5) AI model.
* **OpenCV (opencv-python):** To handle live webcam feed and image processing.
* **NumPy:** To perform numerical operations on image data.
###  Installation Command(setting of environment)
Run the following command in your terminal to set up the environment:
```bash
pip install tensorflow opencv-python numpy
```
## further Progress: The `main.py` Integration
We have successfully transitioned from model training to full system integration. The `main.py` serves as the central orchestrator, handling the following complex tasks:
### 1. High-Performance Inference Engine
The script utilizes a **Compatibility Layer** to load our MobileNetV2 model. 
### 2. Real-Time Vision Pipeline
Using **OpenCV**, we've implemented a frame-capture loop that:
* **Normalizes Input:** Converts raw pixel data into the floating-point format required by the AI.
* **Resizing & Cropping:** Automatically adjusts the camera aspect ratio to a 224x224 input tensor without distorting the image.
### 3. Smart Logic & UX
The `main.py` doesn't just show labels; it makes decisions:
* **Threshold Filtering:** Only triggers a "Bin Instruction" if the AI confidence is above 80%, reducing false positives.
* **Interactive Metrics:** Uses Streamlit's state management to track how many items have been processed in a single session, providing immediate "Impact Feedback."
## Roadmap for hacathon(Checklist)
[x] **09:00 AM:** Problem desicussion
[x] **11:00 AM:** Dataset curation and Model Training via Teachable Machine.
[x] **06:00 PM:** Integration of AI model with Python/OpenCV logic.
[] **11:00 PM:** Adding "Bin Logic" and User Interface feedback.
[ ] **Final Stage:** Optimization for low-latency performance.
*Developed for the Genesys 2.0  Hackathon.*
