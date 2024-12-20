from flask import Flask, request, jsonify
import pandas as pd
import pickle

from keras.src.saving import load_model
from sklearn.feature_extraction.text import TfidfVectorizer


# 1. Load các thành phần mô hình đã huấn luyện
app = Flask(__name__)

# Load vectorizer (TF-IDF) và mô hình ANN đã lưu
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

model = load_model('email_classification_model.h5')


def classify_email(email_text):
    email_vector = vectorizer.transform([email_text]).toarray()

    prediction = model.predict(email_vector)

    label = 'Spam' if prediction[0][0] > 0.5 else 'Binh Thuong'

    return {'email': email_text, 'label': label, 'probability': float(prediction[0][0])}


# 3. Định nghĩa route API
@app.route('/classify', methods=['POST'])
def classify():
    try:
        # Nhận dữ liệu từ request
        data = request.json
        email_text = data.get('email', '')

        if not email_text:
            return jsonify({'error': 'Email text is required'}), 400

        # Gọi hàm phân loại
        result = classify_email(email_text)

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# 4. Chạy ứng dụng Flask
if __name__ == '__main__':
    app.run(debug=True)
