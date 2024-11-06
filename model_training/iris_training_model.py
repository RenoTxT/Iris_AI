import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Input
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import time
from tqdm import tqdm

data_url = 'https://raw.githubusercontent.com/RenoTxT/Iris_AI/main/model_training/iris.csv'
data = pd.read_csv(data_url, sep=';')

features = data.iloc[1:, :4].values.astype(float)
labels = data.iloc[1:, 4].values

label_encoder = LabelEncoder()
labels_encoded = label_encoder.fit_transform(labels)
labels_categorical = to_categorical(labels_encoded, num_classes=3)

X_train, X_test, y_train, y_test = train_test_split(features, labels_categorical, test_size=0.2, random_state=42)

model = Sequential()
model.add(Input(shape=(4,)))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.3))

for _ in range(3):
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.3))

model.add(Dense(3, activation='softmax'))
model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=100, batch_size=16, validation_data=(X_test, y_test))

y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_test_classes = np.argmax(y_test, axis=1)
accuracy = accuracy_score(y_test_classes, y_pred_classes)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.show()

def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    print("Mendeteksi dan memproses data...")
    for _ in tqdm(range(10), desc="Loading"):
        time.sleep(0.1)

    prediction = model.predict(input_data)
    predicted_class = np.argmax(prediction)

    predicted_species = label_encoder.inverse_transform([predicted_class])[0]

    print(f"Prediksi jenis bunga Iris: {predicted_species}")

predict_iris(7, 3, 4, 2)
model.save('iris_predict_model.h5')
