# 🌸 Iris_AI 🌸  
**Your Personal Iris Flower Detector**

Iris_AI is a deep learning-based model that classifies the species of Iris flowers based on four key measurements. The project uses a Multi-Layer Perceptron (MLP) model, trained on a custom Iris dataset available in this repository, to provide accurate species predictions.

[![Open in Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mi40HNfjmxckxSHrd9Zk7oBacwdxW65v)

---

## 🌟 Features
- **Interactive AI Model**: Iris_AI uses a neural network to classify Iris flowers with high accuracy.
- **Multi-Layer Perceptron (MLP) Architecture**: The model uses a dense neural network for effective feature recognition.
- **Real-Time Prediction**: Provides predictions on Iris species based on four simple inputs: **sepal length**, **sepal width**, **petal length**, and **petal width**.

---

## 🚀 Getting Started

### Running the Project Locally
1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/RenoTxT/Iris_AI.git
   cd Iris_AI
   
2. **Install Dependency**:  
   ```bash
   pip install -r requirements.txt

3. **Running on VS Code (Recommended)**:  
   To avoid certain warnings and errors that may appear when running the project from the Command Prompt, it is recommended to run the project in VS Code. You can follow the same steps as above, but instead of using the Command Prompt, use VS Code’s integrated terminal.    This way, you can run the project smoothly without encountering issues related to warnings that may interfere with your experience.

### Running on Google Colab
To run the project directly in Google Colab, click the badge above or this link. This link opens the Colab notebook where you can explore and train the model step-by-step.
<hr/>
<h2>🌼 Example Usage</h2>
After training, you can use the function predict_iris to make predictions. Simply input values to predict the Iris species:
   
   <pre>
   python
   # Example: Predicting Iris species based on measurements
   predict_iris(5.8, 2.7, 4.1, 1.0)
   # Output: Predicted species, e.g., "Iris-versicolor"
   </pre>
<hr/>
<h2>📈 Training the Model</h2>
The model is trained using the following settings:

Model Architecture: Multi-Layer Perceptron with dense layers.
<br/>Epochs: 100 (can be adjusted as desired)
<br/>Batch Size: 16
<br/>Optimizer: Adam with a learning rate of 0.001
<br/>Training metrics (accuracy and loss) are visualized to help assess model performance over time.
<hr/>
<h2>📊 Visualizing Results</h2>
After training, the model's accuracy and loss are plotted for both training and validation data to show progress and convergence.
<hr/>
<h2>🌸 Contributing</h2>
Feel free to fork this repository, make enhancements, and submit pull requests. We welcome contributions that improve accuracy, enhance usability, or add new features.
<hr/>
<h2>License</h2>
Feel free to use this project however if you want to use at your program I hope you give me a credit by tag this github
<hr/>
Enjoy exploring the world of Iris flowers with Iris_AI!
