import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array

MODEL_PATH = "./out/model.keras"

CLASS_NAMES = ["Schere", "Stein", "Papier"]

IMG_WIDTH, IMG_HEIGHT = 180, 180

MIN_CONFIDENCE = 0.7

print(f"[INFO] Lade Modell von {MODEL_PATH}...")
try:
    model = load_model(MODEL_PATH)
    print("[INFO] Modell erfolgreich geladen.")
except Exception as e:
    print(f"[FEHLER] Modell konnte nicht geladen werden: {e}")
    exit()

print("[INFO] Starte Webcam...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("[FEHLER] Webcam konnte nicht geöffnet werden.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("[INFO] Frame konnte nicht gelesen werden, stoppe...")
        break

    image_for_model = cv2.resize(frame, (IMG_WIDTH, IMG_HEIGHT))

    image_array = img_to_array(image_for_model)
    image_array = image_array / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    probabilities = model.predict(image_array)[
        0
    ]  

    predicted_class_index = np.argmax(probabilities)
    confidence = probabilities[predicted_class_index]

    if confidence >= MIN_CONFIDENCE:
        predicted_class_name = CLASS_NAMES[predicted_class_index]

        print(
            f"Erkannt: {predicted_class_name} (Wahrscheinlichkeit: {confidence*100:.2f}%)"
        )

        text = f"{predicted_class_name}: {confidence*100:.2f}%"
        cv2.putText(
            frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2
        )
    else:
        print("Nichts erkannt (Sicherheit zu gering)")

        cv2.putText(
            frame,
            "Nichts erkannt",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 0, 255),
            2,
        )

    cv2.imshow("Live-Erkennung (Zum Beenden 'q' druecken)", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print("[INFO] Beende Programm...")
cap.release()
cv2.destroyAllWindows()
