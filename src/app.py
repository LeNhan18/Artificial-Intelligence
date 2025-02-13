from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from src.Doc import vectorizer
from flask_cors import CORS
import pickle
import logging

# Tải mô hình đã lưu
model = load_model("PhanLoaiEmail.keras")

# Tải vectorizer đã được huấn luyện

# Sau khi huấn luyện vectorizer, thêm đoạn mã này để lưu
with open("tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Đã lưu tfidf_vectorizer.pkl thành công!")
# Tạo Flask app
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
@app.route("/nhanle", methods=["POST"])
def predict():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Request received.")

    try:
        data = request.get_json()
        logging.debug(f"Dữ liệu đã nhận: {data}")

        if not data:
            logging.error("Không nhận được dữ liệu")
            return jsonify({"error": "Không nhận được dữ liệu"}), 400

        if "email" not in data:
            logging.error("Không cung cấp email.")
            return jsonify({"error": "Không cung cấp email"}), 400

        email_text = data["email"]
        logging.debug(f"Nội dung email: {email_text}")

        # Vectorize email text
        email_vector = vectorizer.transform([email_text]).toarray()
        prediction = model.predict(email_vector)
        label = "spam" if prediction[0] > 0.5 else "ham"

        logging.debug(f"Kết Qua dự đoán: {label}")
        return jsonify({"Ket Qua dự đoán": label})

    except Exception as e:
        logging.error(f"Lỗi: {e}")
        return jsonify({"error": "Lỗi server"}), 500

if __name__ == "__main__":
    app.run(debug=True)

