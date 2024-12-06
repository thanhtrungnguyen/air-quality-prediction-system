import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
# from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from src.config import MODEL_PATH, DATASET_PATH, BATCH_SIZE, EPOCHS, LEARNING_RATE

print("Training model...")

# Example usage
print(f"Model path: {MODEL_PATH}")
print(f"Dataset path: {DATASET_PATH}")
print(f"Batch size: {BATCH_SIZE}, Epochs: {EPOCHS}, Learning rate: {LEARNING_RATE}")

# Limit GPU memory growth
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print(f"Using {len(gpus)} GPU(s)")
    except RuntimeError as e:
        print(f"Error configuring GPUs: {e}")

# Load and preprocess data
df = pd.read_csv("../../data/processed/combined_data.csv")

data = pd.get_dummies(df)

X = data.drop(columns=['Unnamed: 0', 'timestamp', 'CO', 'NO', 'NO2', 'O3', 'SO2', 'PM2_5', 'PM10', 'NH3', 'AQI'],
              axis=1)

y = data.loc[:, ['CO', 'NO', 'NO2', 'O3', 'SO2', 'PM2_5', 'PM10', 'NH3', 'AQI']]

scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

X_train, X_val, y_train, y_val = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(y_train.shape[1], activation='linear')  # Output layer for multiple targets
])

# Compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss='mean_squared_error',
              metrics=['mean_absolute_error'])

# Train the model
callbacks = [
    tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True),
    tf.keras.callbacks.ModelCheckpoint('../models/best_model.keras', save_best_only=True, monitor='val_loss')
]

history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=100, batch_size=32, callbacks=callbacks)

print("Model trained and saved.")
