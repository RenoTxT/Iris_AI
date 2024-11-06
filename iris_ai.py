from google.colab import files
uploaded = files.upload()

import numpy as np
from sklearn.preprocessing import LabelEncoder

model = load_model('iris_predict_model.h5')

# Inisialisasi encoder untuk konversi prediksi numerik ke label string
label_encoder = LabelEncoder()
label_encoder.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])  # Sesuaikan dengan label asli

# Fungsi prediksi
def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    predicted_class = np.argmax(prediction)
    predicted_species = label_encoder.inverse_transform([predicted_class])[0]
    print(f"Prediksi jenis bunga Iris: {predicted_species}")

# Contoh prediksi
predict_iris(7, 6, 1, 3)