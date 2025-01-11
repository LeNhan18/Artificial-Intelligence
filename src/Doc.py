import os
import glob
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Đọc dữ liệu từ các thư mục
spam_folders = ["C:\\Users\\Admin\\Downloads\\spam_2\\spam_2"]
ham_folders = ["C:\\Users\\Admin\\Downloads\\easy_ham\\easy_ham"]

mail_data = []
for folder_path in spam_folders:
    spam_files = glob.glob(os.path.join(folder_path, "*"))
    for fname in spam_files:
        try:
            with open(fname, "r", encoding="latin-1") as f:
                content = f.read()
            mail_data.append((content, 1))
        except Exception as e:
            print(f"Lỗi khi đọc file {fname}: {e}")

for folder_path in ham_folders:
    ham_files = glob.glob(os.path.join(folder_path, "*"))
    for fname in ham_files:
        try:
            with open(fname, "r", encoding="latin-1") as f:
                content = f.read()
            mail_data.append((content, 0))
        except Exception as e:
            print(f"Lỗi khi đọc file {fname}: {e}")

# Tạo DataFrame
df = pd.DataFrame(mail_data, columns=["text", "label"])
print(df['label'].value_counts())

# Chuyển đổi văn bản thành vector số
vectorizer = TfidfVectorizer(
    max_features=5000, stop_words='english', lowercase=True, ngram_range=(1, 2)
)
X = vectorizer.fit_transform(df['text']).toarray()
y = df['label'].values

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Xử lý dữ liệu không cân bằng bằng SMOTE
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
print("Dữ liệu sau SMOTE:", X_train_res.shape, y_train_res.shape)
print("Phân phối sau SMOTE:")
print(pd.Series(y_train_res).value_counts())

# Xây dựng mô hình mạng nơ-ron
model = Sequential([
    Dense(512, input_shape=(X_train_res.shape[1],), activation='relu'),
    Dropout(0.5),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Biên dịch mô hình
model.compile(
    loss='binary_crossentropy',
    optimizer=Adam(learning_rate=0.0001),
    metrics=['accuracy']
)

# Huấn luyện mô hình
history = model.fit(
    X_train_res, y_train_res,
    epochs=10,
    batch_size=64,
    validation_data=(X_test, y_test)
)

# Dự đoán và đánh giá
y_pred = (model.predict(X_test) > 0.5).astype("int32")
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
from tensorflow.keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = model.fit(
    X_train_res, y_train_res,
    epochs=50,
    batch_size=64,
    validation_data=(X_test, y_test),
    callbacks=[early_stopping]
)
import matplotlib.pyplot as plt

# Accuracy
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.title('Accuracy Over Epochs')
plt.show()

# Loss
plt.plot(history.history['loss'], label='')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.title('Loss Over Epochs')
plt.show()
from keras.saving import save_model
save_model(model, "PhanLoaiEmail.keras")