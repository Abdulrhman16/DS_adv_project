from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle

app = Flask(__name__)

# إعدادات
MODEL_PATH = "sentiment_model.h5"
TOKENIZER_PATH = "tokenizer.pickle"
MAX_LEN = 400  # نفس max_length اللي دربت عليه

# تحميل النموذج
model = load_model(MODEL_PATH)

# تحميل الـ tokenizer
with open(TOKENIZER_PATH, "rb") as handle:
    tokenizer = pickle.load(handle)

# المعالجة المسبقة
def preprocess(text):
    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=MAX_LEN)
    return padded

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None

    if request.method == "POST":
        text = request.form["text"]
        processed = preprocess(text)
        pred = model.predict(processed)[0][0]  # قيمة واحدة فقط

        label = "P" if pred >= 0.5 else "N"
        confidence = pred if label == "P" else 1 - pred

        prediction = f"Predicted Label: {label}"
        confidence = f"Confidence: {confidence:.2%}"

    return render_template("index.html", prediction=prediction, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
