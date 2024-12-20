from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import pickle

# Load dữ liệu
data = pd.read_csv('spam.csv', encoding='latin-1')
data = data[['v1', 'v2']].rename(columns={'v1': 'label', 'v2': 'text'})
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Tiền xử lý văn bản
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X = vectorizer.fit_transform(data['text']).toarray()
y = data['label']

# Lưu vectorizer
with open('vectorizer.pkl', 'wb') as file:\n       pickle.dump(vectorizer, file)

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Xây dựng mô hình ANN
model = Sequential([\n       Dense(128, activation='relu', input_dim=X.shape[1]),\n       Dropout(0.5),\n       Dense(64, activation='relu'),\n       Dropout(0.3),\n       Dense(1, activation='sigmoid')\n   ])\n\n   # Compile và train\n   model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])\n   model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)\n\n   # Lưu mô hình\n   model.save('email_classification_model.h5')\n   ```
