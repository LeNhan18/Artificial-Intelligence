from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

from src.Doc import vectorizer

# Tải mô hình đã lưu
model = load_model("PhanLoaiEmail.keras")

# Tải vectorizer đã được huấn luyện
# Bạn cần lưu vectorizer sau khi huấn luyện và tải lại
import pickle

# Sau khi huấn luyện vectorizer, thêm đoạn mã này để lưu
with open("tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Đã lưu tfidf_vectorizer.pkl thành công!")
# Tạo Flask app
from flask_cors import CORS
from flask import Flask, request, jsonify
app = Flask(__name__)
CORS(app)
@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     logging.basicConfig(level=logging.DEBUG)
#     logging.debug("Request received.")
#
#     data = request.get_json()
#     logging.debug(f"Data received: {data}")
#
#     if not data:
#         logging.error("No data provided.")
#         return jsonify({"error": "No data provided"}), 400
#
#     if "email" not in data:
#         logging.error("No email field provided.")
#         return jsonify({"error": "No email field provided"}), 400
#
#     email_text = data["email"]
#     email_vector = vectorizer.transform([email_text]).toarray()
#     prediction = model.predict(email_vector)
#     label = "spam" if prediction[0] > 0.5 else "ham"
#
#     logging.debug(f"Ket Qua: {label}")
#     return jsonify({"Ket Qua": label})

import logging

@app.route("/predict", methods=["POST"])
def predict():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Request received.")

    try:
        data = request.get_json()
        logging.debug(f"Data received: {data}")

        if not data:
            logging.error("No data provided.")
            return jsonify({"error": "No data provided"}), 400

        if "email" not in data:
            logging.error("No email field provided.")
            return jsonify({"error": "No email field provided"}), 400

        email_text = data["email"]
        logging.debug(f"Email content: {email_text}")

        # Vectorize email text
        email_vector = vectorizer.transform([email_text]).toarray()
        prediction = model.predict(email_vector)
        label = "spam" if prediction[0] > 0.5 else "ham"

        logging.debug(f"Prediction result: {label}")
        return jsonify({"KetQua": label})

    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
