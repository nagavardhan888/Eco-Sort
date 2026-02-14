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
## Roadmap for hacathon(Checklist)
[x] **09:00 AM:** Problem desicussion
[x] **11:00 AM:** Dataset curation and Model Training via Teachable Machine.
[ ] **06:00 PM:** Integration of AI model with Python/OpenCV logic.
[ ] **11:00 PM:** Adding "Bin Logic" and User Interface feedback.
[ ] **Final Stage:** Optimization for low-latency performance.
*Developed for the Genesys 2.0  Hackathon.*
