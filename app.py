import streamlit as st
import numpy as np
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

# ----------------------------
# Load and prepare data
# ----------------------------
calories = pd.read_csv('calories.csv')
exercise_data = pd.read_csv('exercise.csv')

calories_data = pd.concat([exercise_data, calories['Calories']], axis=1)
calories_data.replace({"Gender": {'male': 0, 'female': 1}}, inplace=True)

X = calories_data.drop(columns=['User_ID', 'Calories'], axis=1)
Y = calories_data['Calories']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

model = XGBRegressor()
model.fit(X_train, Y_train)

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Calories Burnt Prediction", page_icon="🔥", layout="centered")

st.title("🔥 Calories Burnt Prediction App")
st.write("Enter your exercise details to estimate calories burnt using **XGBoost**.")

# Sidebar for inputs
st.sidebar.header("Input Features")

gender = st.sidebar.radio("Gender", ("Male", "Female"))
gender_val = 0 if gender == "Male" else 1

age = st.sidebar.slider("Age", 18, 80, 25)
height = st.sidebar.number_input("Height (cm)", min_value=100.0, max_value=250.0, value=170.0)
weight = st.sidebar.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
duration = st.sidebar.slider("Exercise Duration (mins)", 1, 60, 20)
heart_rate = st.sidebar.slider("Heart Rate (bpm)", 60, 200, 100)
body_temp = st.sidebar.number_input("Body Temperature (°C)", min_value=36.0, max_value=42.0, value=38.5)

# Predict button
if st.button("🔮 Predict Calories Burnt"):
    input_data = np.array([[gender_val, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)
    st.success(f"🔥 Estimated Calories Burnt: **{prediction[0]:.2f} kcal**")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & XGBoost")
