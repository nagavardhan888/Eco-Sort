import cv2
import numpy as np
import tensorflow as tf
import pyttsx3

# ---------- Voice setup ----------
engine = pyttsx3.init()
engine.setProperty('rate', 165)

def speak(text):
    engine.say(text)
    engine.runAndWait()

# ---------- Load AI Model ----------
model = tf.keras.models.load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

print("AI Smart Bin Ready")

# ---------- Start Camera ----------
cap = cv2.VideoCapture(0)

already_spoken = False
last_label = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize image for model
    img = cv2.resize(frame, (224, 224))
    img = np.asarray(img)
    img = (img.astype(np.float32) / 127.5) - 1
    img = np.expand_dims(img, axis=0)

    # Prediction
    prediction = model.predict(img, verbose=0)
    index = np.argmax(prediction)
    label = class_names[index].strip()
    confidence = prediction[0][index]

    # Display on screen
    text = f"{label} ({confidence*100:.1f}%)"
    cv2.putText(frame, text, (20,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # Speak ONLY when new object detected
    if label != last_label and confidence > 0.80:
        print("Detected:", label)
        speak(label + " waste detected")
        last_label = label

    cv2.imshow("Eco Smart Bin", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
