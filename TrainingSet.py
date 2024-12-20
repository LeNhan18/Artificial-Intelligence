import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, GlobalAveragePooling1D, Dense
from tensorflow.keras.optimizers import Adam

# 4.1. Khởi tạo mô hình
model = Sequential()

# 4.2. Tầng Embedding
embedding_dim = 50
model.add(
    Embedding(input_dim=num_words,  # phải khớp với tokenizer
              output_dim=embedding_dim,
              input_length=max_length)
)

# 4.3. Tầng Pooling
model.add(GlobalAveragePooling1D())

# 4.4. Tầng ẩn (Dense) với hàm kích hoạt ReLU
model.add(Dense(16, activation='relu'))

# 4.5. Tầng đầu ra (Dense) cho phân loại nhị phân (sigmoid)
model.add(Dense(1, activation='sigmoid'))

# 4.6. Compile mô hình
model.compile(
    loss='binary_crossentropy',
    optimizer=Adam(learning_rate=0.001),
    metrics=['accuracy']
)

model.summary()  # xem cấu trúc mô hình
# 5.1. Huấn luyện mô hình
history = model.fit(
    train_padded,
    y_train,
    epochs=5,          # số lần lặp (có thể tăng)
    batch_size=32,     # kích thước batch
    validation_split=0.2,  # trích 20% train làm validation
    verbose=1
)
# 6.1. Đánh giá
loss, accuracy = model.evaluate(test_padded, y_test, verbose=0)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")
from sklearn.metrics import classification_report

y_pred = (model.predict(test_padded) >= 0.5).astype(int)
print(classification_report(y_test, y_pred, target_names=["Ham", "Spam"]))
def predict_email(model, tokenizer, email_text):
    # 7.1. Chuyển sang chữ thường + xử lý cơ bản
    email_text = email_text.lower()

    # 7.2. Convert to sequence + pad
    seq = tokenizer.texts_to_sequences([email_text])
    pad = pad_sequences(seq, maxlen=max_length, padding='post', truncating='post')

    # 7.3. Dự đoán
    prob = model.predict(pad)[0][0]  # xác suất spam
    label = "Spam" if prob >= 0.5 else "Ham"
    return label, prob

sample_email = "Bạn đã trúng thưởng 1 tỷ đồng! Bấm link để nhận giải..."
label, prob = predict_email(model, tokenizer, sample_email)
print(f"Email: {sample_email}\nDự đoán: {label} (xác suất={prob:.4f})")
model.save("spam_ham_model.h5")
from tensorflow.keras.models import load_model

loaded_model = load_model("spam_ham_model.h5")
