
spam_folders = [
    "C:\\Users\\Admin\\Downloads\\spam_2",

]

# Danh sách thư mục chứa email thường (ham)
ham_folders = [
    "C:\\Users\\Admin\\Downloads\\easy_ham",

]
import os
import glob
import pandas as pd

mail_data = []  # list để lưu (nội_dung, nhãn)

# Đọc thư mục SPAM
for folder_path in spam_folders:
    # Lấy danh sách file .txt/.eml trong thư mục
    spam_files = glob.glob(os.path.join(folder_path, "*"))
    for fname in spam_files:
        try:
            with open(fname, "r", encoding="latin-1") as f:
                content = f.read()
            # Thêm vào list mail_data, label=1 (spam)
            mail_data.append((content, 1))
        except Exception as e:
            print(f"Lỗi khi đọc file {fname}: {e}")

# Đọc thư mục HAM
for folder_path in ham_folders:
    ham_files = glob.glob(os.path.join(folder_path, "*"))
    for fname in ham_files:
        try:
            with open(fname, "r", encoding="latin-1") as f:
                content = f.read()
            # Thêm vào list mail_data, label=0 (ham)
            mail_data.append((content, 0))
        except Exception as e:
            print(f"Lỗi khi đọc file {fname}: {e}")

# Tạo DataFrame
df = pd.DataFrame(mail_data, columns=["text", "label"])
print(df.head())
print(df['label'].value_counts())

# Lưu vào CSV
df.to_csv("spamassassin_data.csv", index=False)
from sklearn.feature_extraction.text import TfidfVectorizer

# Khởi tạo TfidfVectorizer với các tham số phù hợp
vectorizer = TfidfVectorizer(
    max_features=5000,          # Giới hạn số lượng đặc trưng
    stop_words='english',       # Loại bỏ các stop words
    lowercase=True,             # Chuyển đổi văn bản thành chữ thường
    ngram_range=(1, 2)          # Sử dụng unigram và bigram
)

# Chuyển đổi văn bản thành vector số
X = vectorizer.fit_transform(df['text']).toarray()
y = df['label'].values

print("Kích thước ma trận đặc trưng:", X.shape)
from sklearn.model_selection import train_test_split

# Chia dữ liệu thành tập huấn luyện và kiểm tra (70% - 30%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print("Số lượng email trong tập huấn luyện:", X_train.shape[0])
print("Số lượng email trong tập kiểm tra:", X_test.shape[0])
import tensorflow as tf
from tensorflow
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import classification_report, confusion_matrix

# Xây dựng mô hình mạng nơ-ron
model = Sequential()
model.add(Dense(512, input_dim=X_train_res.shape[1], activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# Biên dịch mô hình
model.compile(
    loss='binary_crossentropy',
    optimizer=Adam(learning_rate=0.001),
    metrics=['accuracy']
)

# Huấn luyện mô hình
history = model.fit(
    X_train_res, y_train_res,
    epochs=10,
    batch_size=64,
    validation_data=(X_test, y_test)
)
