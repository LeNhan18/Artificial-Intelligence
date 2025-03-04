import os
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split

# 1. Thu thập dữ liệu
faces_dataset_path = os.path.abspath("C:\\Users\\Admin\\PycharmProjects\\ANN\\src\\faces_dataset")
data = []
labels = []
people = os.listdir(faces_dataset_path)
label_dict = {name: idx for idx, name in enumerate(people)}

for person in people:
    person_path = os.path.join(faces_dataset_path, person)
    if not os.path.isdir(person_path):  # Kiểm tra nếu không phải thư mục thì bỏ qua
        continue
    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue  # Bỏ qua ảnh bị lỗi
        img = cv2.resize(img, (100, 100))
        data.append(img)
        labels.append(label_dict[person])

# Chuyển dữ liệu thành mảng numpy
data = np.array(data).reshape(-1, 100, 100, 1) / 255.0
labels = to_categorical(np.array(labels), len(people))

# 2. Chia tập dữ liệu thành train/test
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# 3. Xây dựng mô hình CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 1)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(len(people), activation='softmax')
])

# 4. Compile và train mô hình
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
model.fit(X_train, y_train, epochs=30, validation_data=(X_test, y_test), callbacks=[early_stopping])

# 5. Lưu mô hình
model.save("face_recognition_model.h5")
# 6. Triển khai nhận diện khuôn mặt
def recognize_face(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File '{image_path}' không tồn tại.")

    model = tf.keras.models.load_model("face_recognition_model.h5")
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Không thể đọc ảnh.")
    img = cv2.resize(img, (100, 100)).reshape(1, 100, 100, 1) / 255.0
    prediction = model.predict(img)
    predicted_label = np.argmax(prediction)
    confidence = np.max(prediction)
    return list(label_dict.keys())[predicted_label], confidence


# Test nhận diện
label, confidence = recognize_face("test_face.jpg")
print(f"Dự đoán: {label} ({confidence:.2f})")
