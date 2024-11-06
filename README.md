<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iris_AI - Personal Iris Flower Detector</title>
</head>
<body>
    <h1>🌸 Iris_AI 🌸</h1>
    <p><strong>Your Personal Iris Flower Detector</strong></p>
    <p>
        Iris_AI is a deep learning-based model that classifies the species of Iris flowers based on four key measurements. The project uses a Multi-Layer Perceptron (MLP) model, trained on a custom Iris dataset available in this repository, to provide accurate species predictions.
    </p>

    <p>
        <a href="https://colab.research.google.com/drive/1mi40HNfjmxckxSHrd9Zk7oBacwdxW65v">
            <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Google Colab">
        </a>
    </p>

    <h2>🌟 Features</h2>
    <ul>
        <li><strong>Interactive AI Model</strong>: Iris_AI uses a neural network to classify Iris flowers with high accuracy.</li>
        <li><strong>Multi-Layer Perceptron (MLP) Architecture</strong>: The model uses a dense neural network for effective feature recognition.</li>
        <li><strong>Real-Time Prediction</strong>: Provides predictions on Iris species based on four simple inputs: <strong>sepal length</strong>, <strong>sepal width</strong>, <strong>petal length</strong>, and <strong>petal width</strong>.</li>
    </ul>

    <h2>🚀 Getting Started</h2>
    <h3>Running the Project Locally</h3>
    <p>Follow these steps to run the project on your local machine:</p>
    <ol>
        <li><strong>Clone the Repository</strong>: 
            <pre>
                git clone https://github.com/RenoTxT/Iris_AI.git
                cd Iris_AI
            </pre>
        </li>
        <li><strong>Install Dependency</strong>: 
            <pre>
                pip install -r requirements.txt
            </pre>
        </li>
        <li><strong>Run The Notebook</strong>: Open the <code>Iris_AI.ipynb</code> notebook in Jupyter Notebook or Google Colab to start training and using the model.</li>
    </ol>

    <h3>Running on VS Code (Recommended)</h3>
    <p>To avoid certain warnings and errors that may appear when running the project from the Command Prompt, it is <strong>recommended to run the project in VS Code</strong>. You can follow the same steps as above, but instead of using the Command Prompt, use VS Code’s integrated terminal. This way, you can run the project smoothly without encountering issues related to warnings that may interfere with your experience.</p>

    <h3>Running on Google Colab</h3>
    <p>To run the project directly in Google Colab, click the badge above or <a href="https://colab.research.google.com/drive/1mi40HNfjmxckxSHrd9Zk7oBacwdxW65v">this link</a>. This link opens the Colab notebook where you can explore and train the model step-by-step.</p>

    <h2>🌼 Example Usage</h2>
    <p>After training, you can use the function <code>predict_iris</code> to make predictions. Simply input values to predict the Iris species:</p>
    <pre>
# Example: Predicting Iris species based on measurements
predict_iris(5.8, 2.7, 4.1, 1.0)
# Output: Predicted species, e.g., "Iris-versicolor"
    </pre>

    <h2>📈 Training the Model</h2>
    <p>The model is trained using the following settings:</p>
    <ul>
        <li><strong>Model Architecture</strong>: Multi-Layer Perceptron with dense layers.</li>
        <li><strong>Epochs</strong>: 100 (can be adjusted as desired)</li>
        <li><strong>Batch Size</strong>: 16</li>
        <li><strong>Optimizer</strong>: Adam with a learning rate of 0.001</li>
    </ul>
    <p>Training metrics (accuracy and loss) are visualized to help assess model performance over time.</p>

    <h2>📊 Visualizing Results</h2>
    <p>After training, the model's accuracy and loss are plotted for both training and validation data to show progress and convergence.</p>

    <h2>🌸 Contributing</h2>
    <p>Feel free to fork this repository, make enhancements, and submit pull requests. We welcome contributions that improve accuracy, enhance usability, or add new features.</p>

    <h2>License</h2>
    <p>Feel free to use this project however you want, but if you integrate it into your program, we ask that you give credit by tagging this GitHub.</p>

    <p>Enjoy exploring the world of Iris flowers with Iris_AI!</p>
</body>
</html>
