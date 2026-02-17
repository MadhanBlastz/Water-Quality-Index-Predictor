import streamlit as st
import numpy as np
import joblib

# Load trained objects
model = joblib.load("hybrid_wqi_model.pkl")
scaler = joblib.load("scaler.pkl")
imputer = joblib.load("imputer.pkl")

st.set_page_config(page_title="WQI Predictor", layout="centered")

st.title("💧 Water Quality Index Predictor")
st.write("Enter water parameters to predict WQI and Water Quality")

# -------- INPUT FIELDS (10 FEATURES) --------
pH = st.number_input("pH", 0.0, 14.0, 7.0)
TDS = st.number_input("TDS", 0.0, 5000.0, 500.0)
Cl = st.number_input("Chloride", 0.0, 2000.0, 100.0)
SO4 = st.number_input("Sulphate", 0.0, 2000.0, 100.0)
Na = st.number_input("Sodium", 0.0, 2000.0, 50.0)
K = st.number_input("Potassium", 0.0, 500.0, 10.0)
Ca = st.number_input("Calcium", 0.0, 500.0, 50.0)
Mg = st.number_input("Magnesium", 0.0, 500.0, 30.0)
Hardness = st.number_input("Total Hardness", 0.0, 2000.0, 200.0)

# ⚠️ IMPORTANT
# Your model was trained with 10 features
# If you used 10 inputs in training, ADD the missing one here.
# Example: if you trained with "Sample ID" removed,
# then your 9 features are correct.
# If you trained with 10 numeric features, add the missing feature.

# For safety, we add a dummy 10th feature = 0
extra_feature = 0.0

if st.button("Predict WQI"):

    features = np.array([[extra_feature, pH, TDS, Cl, SO4, Na, K, Ca, Mg, Hardness]])

    # Preprocess
    features = imputer.transform(features)
    features = scaler.transform(features)

    # Predict
    wqi = model.predict(features)[0]

    # Classify
    if wqi <= 50:
        label = "Excellent"
        color = "green"
    elif wqi <= 100:
        label = "Good"
        color = "lightgreen"
    elif wqi <= 200:
        label = "Poor"
        color = "orange"
    else:
        label = "Very Poor"
        color = "red"

    st.markdown(f"## 🔢 Predicted WQI: **{wqi:.2f}**")
    st.markdown( f"<h2>🏷 Water Quality: <span style='color:{color}'>{label}</span></h2>", unsafe_allow_html=True )
