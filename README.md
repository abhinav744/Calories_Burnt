# 🔥 Calories Burnt Prediction

A machine learning project that estimates the number of calories burned during physical activity based on personal biometric inputs and workout parameters.

👉 Live Demo: [Calories Burnt App](https://caloriesburnt-gwwqnmz9tikh3ks5xdrdn2.streamlit.app/)

## 📌 Project Overview

This application predicts calories burned using key inputs such as gender, age, height, weight, exercise duration, heart rate, and body temperature. Built using Python's ML ecosystem, it includes data processing, model training, evaluation, and an interactive interface via Streamlit for real-time predictions.

## 📂 Repository Structure

/Calories_Burnt

│── data/

│    └── calories.csv

│    └── exercise.csv

│── models/

│    └── model.pkl             # Trained model

│    └── scaler.pkl            # Preprocessor

│── app.py                     # Streamlit app

│── train.py                   # Model training script

│── requirements.txt           # Python dependencies

│── README.md                  # Project documentation

## 🚀 Getting Started

### 1. Clone the repository

git clone https://github.com/abhinav744/Calories_Burnt.git

cd Calories_Burnt

### 2. (Optional) Set up a virtual environment

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Train the model

python train.py

### 5. Run the Streamlit app

streamlit run app.py

## 🔮 Future Enhancements

Compare multiple models (Random Forest, XGBoost, etc.)

Add visual insights in the Streamlit app (feature importance, prediction plots)

Hyperparameter tuning for accuracy
