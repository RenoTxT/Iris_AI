# Importing necessary libraries
import requests
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import LabelEncoder
import os

# if you want to use offline file remove the comment and make sure the model is on the same path by check the current directory
# Print the current directory to confirm file location
# print("Current Directory:", os.getcwd())
# Load the model (make sure the file is in the same directory)
# model = load_model('iris_predict_model.h5')

# import model online from github
model_url = 'https://github.com/RenoTxT/Iris_AI/raw/main/iris_predict_model.h5'
model_filename = 'iris_predict_model.h5'

response = requests.get(model_url)
with open(model_filename, 'wb') as file:
    file.write(response.content)

model = load_model(model_filename)

# Initialize label encoder to convert numeric predictions to species labels
label_encoder = LabelEncoder()
label_encoder.fit(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])  # Adjust to match original labels

# Define the prediction function
def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data, verbose=0)  # Set verbose=0 to avoid unnecessary logs
    predicted_class = np.argmax(prediction)
    predicted_species = label_encoder.inverse_transform([predicted_class])[0]
    print(f"Prediksi jenis bunga Iris: {predicted_species}")

# Input data from user
try:
    sepal_length = float(input("Masukkan panjang sepal (cm): "))
    sepal_width = float(input("Masukkan lebar sepal (cm): "))
    petal_length = float(input("Masukkan panjang petal (cm): "))
    petal_width = float(input("Masukkan lebar petal (cm): "))
    
    # Call the prediction function with the user input
    predict_iris(sepal_length, sepal_width, petal_length, petal_width)

except ValueError:
    print("Input invalid")
