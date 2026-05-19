import streamlit as st
import pickle
import numpy as np

# Load Model
model = pickle.load(open("model.pkl","rb"))

# Page Title
st.title("🏠 House Price Predictor")
st.write("Predict house price using Machine Learning")

# Inputs
area = st.number_input("Enter Area (sq ft)")
bedrooms = st.number_input("Number of Bedrooms")

# Prediction Button
if st.button("Predict Price"):

    input_data = np.array([[area, bedrooms]])
    prediction = model.predict(input_data)

    st.success(f"Estimated Price: ₹ {prediction[0]:.2f} Lakhs")