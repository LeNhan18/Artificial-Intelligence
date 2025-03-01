import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Load MNIST dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Build ANN model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Chuyển ma trận 28x28 thành vector 1D
    keras.layers.Dense(128, activation='relu'),  # Hidden layer với 128 neuron
    keras.layers.Dropout(0.2),  # Giảm overfitting
    keras.layers.Dense(10, activation='softmax')  # Output layer với 10 lớp (0-9)
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
# Train model
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Evaluate model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc}')

# Save model
model.save("handwriting_model.h5")
