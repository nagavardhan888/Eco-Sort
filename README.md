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
**Features
Real-Time Detection: Processes live video feed from your webcam.
High Precision: Uses a TensorFlow/Keras model (.h5) for image classification.
Interactive UI: Simple "Start" and "Stop" controls powered by Streamlit.
Confidence Filtering: Only triggers labels when the model is >80% confident.
**Prerequisites
Before running the app, ensure you have the following installed:
Python 3.9+
A working Webcam
```bash
pip install streamlit opencv-python numpy tensorflow
```
How to Use
Run the Streamlit application:
```bash
streamlit run app.py
```
*The browser will open automatically at http://localhost:8501.
*Click the "Start Camera" button.
*Hold an object (e.g., a plastic bottle or paper) in front of the camera to see the classification.
**Technical FlowCapture:
*OpenCV captures frames from the webcam.
*Pre-process: Frames are resized to $224 X 224$ and normalized to a range of $[-1, 1]$.
*Inference: The Keras model predicts the category.
*Display: The label and confidence score are overlaid on the live video feed.
## Roadmap for hacathon(Checklist)
[x] **09:00 AM:** Problem desicussion
[x] **11:00 AM:** Dataset curation and Model Training via Teachable Machine.
[x] **06:00 PM:** Integration of AI model with Python/OpenCV logic.
[x] **11:00 PM:** Adding "Bin Logic" and User Interface feedback.
[X] **Final Stage:** Optimization for low-latency performance.
*Developed for the Genesys 2.0  Hackathon.*
