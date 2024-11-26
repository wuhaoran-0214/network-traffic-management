import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import numpy as np

# Prepare data (time series format)
X_train = np.random.rand(1000, 30, 1)  # Example data
y_train = np.random.rand(1000, 1)

# Build LSTM model
model = Sequential([
    LSTM(128, input_shape=(30, 1), return_sequences=True),
    Dropout(0.2),
    LSTM(64, return_sequences=False),
    Dense(1, activation="linear")
])

# Compile and train
model.compile(optimizer="adam", loss="mse")
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Save model
model.save("lstm_model.h5")
