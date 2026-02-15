import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model


model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()


st.title("AI Eco Smart Bin")
st.write("Real Time Waste Detection System")

start = st.button("Start Camera")
stop = st.button("Stop Camera")

frame_window = st.empty()


if start:

    cap = cv2.VideoCapture(0)

    last_label = ""

    while cap.isOpened():

        ret, frame = cap.read()
        if not ret:
            st.error("Camera not found")
            break

    
        img = cv2.resize(frame, (224, 224))
        img = np.asarray(img)
        img = (img.astype(np.float32) / 127.5) - 1
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img, verbose=0)
        index = np.argmax(prediction)
        label = class_names[index].strip()
        confidence = prediction[0][index]

        text = f"{label} ({confidence*100:.1f}%)"

        cv2.putText(frame, text, (20,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)


        if label != last_label and confidence > 0.80:
            last_label = label

    
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame)

  
        if stop:
            break

    cap.release()
