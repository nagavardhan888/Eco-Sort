import cv2
import numpy as np
import tensorflow as tf
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 165)

def speak(text):
    engine.say(text)
    engine.runAndWait()
model = tf.keras.models.load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

print("AI Smart Bin Ready")

cap = cv2.VideoCapture(0)

already_spoken = False
last_label = ""

while True:
    ret, frame = cap.read()
    if not ret:
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
        print("Detected:", label)
        speak(label + " waste detected")
        last_label = label

    cv2.imshow("Eco Smart Bin", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
