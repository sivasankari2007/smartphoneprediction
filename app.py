import streamlit as st
import pickle
import numpy as np

with open("l", "rb") as f:
    model = pickle.load(f)

st.title("📱 Mobile Price Prediction")

f1 = st.number_input("Feature 1")
f2 = st.number_input("Feature 2")
f3 = st.number_input("Feature 3")
f4 = st.number_input("Feature 4")

if st.button("Predict"):
    result = model.predict([[f1, f2, f3, f4]])
    st.success(f"Predicted Price: ₹ {result[0]:.2f}")
