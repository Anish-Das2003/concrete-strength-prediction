import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("🏗️ Concrete Strength Prediction App")

st.write("Enter the mix design parameters to predict compressive strength (MPa).")
col1,col2= st.columns(2)
# Input fields
with col1:
    cement = st.number_input("Cement (kg/m³)", min_value=0.0)
    blast_furnace = st.number_input("Blast Furnace Slag (kg/m³)", min_value=0.0)
    fly_ash = st.number_input("Fly Ash (kg/m³)", min_value=0.0)
    water = st.number_input("Water (kg/m³)", min_value=0.0)

with col2:
    superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0)
    coarse_aggregate = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0)
    fine_aggregate = st.number_input("Fine Aggregate (kg/m³)", min_value=0.0)
    age = st.number_input("Age (days)", min_value=1)

# Predict button
if st.button("Predict Strength"):
    features = np.array([
        cement,
        blast_furnace,
        fly_ash,
        water,
        superplasticizer,
        coarse_aggregate,
        fine_aggregate,
        age
    ]).reshape(1, -1)

    prediction = model.predict(features)

    st.success(f"Predicted Concrete Strength: **{prediction[0]:.2f} MPa**")