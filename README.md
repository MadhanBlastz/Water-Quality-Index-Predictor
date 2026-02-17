💧 Water Quality Index (WQI) Predictor

A Machine Learning based web application that predicts the Water Quality Index (WQI) and classifies water quality as Excellent, Good, Poor, or Very Poor using physicochemical parameters.

Built using Streamlit, Scikit-learn, and Python.

📌 Project Overview

Water Quality Index (WQI) is an important indicator used to evaluate the overall quality of water for drinking and other purposes.

This project:

Accepts water parameters as input

Uses a trained ML model

Predicts WQI value

Classifies water quality level

⚙️ Features

✅ User-friendly Streamlit interface
✅ Real-time WQI prediction
✅ Automatic data preprocessing (Imputer + Scaler)
✅ Color-coded water quality classification
✅ Machine Learning model integration

📊 Input Parameters

The model takes the following inputs:

pH

TDS (Total Dissolved Solids)

Chloride (Cl)

Sulphate (SO4)

Sodium (Na)

Potassium (K)

Calcium (Ca)

Magnesium (Mg)

Total Hardness

🧠 Machine Learning Model

Model file: hybrid_wqi_model.pkl

Preprocessing:

imputer.pkl

scaler.pkl

Libraries used:

NumPy

Scikit-learn

Joblib

🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/your-username/wqi-predictor.git
cd wqi-predictor

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
streamlit run app.py

🌐 Deployment

This project can be deployed for free on:

Streamlit Community Cloud (Recommended)

Render

Railway

📂 Project Structure
WQI-Predictor/
│
├── app.py
├── hybrid_wqi_model.pkl
├── scaler.pkl
├── imputer.pkl
├── requirements.txt
└── README.md

🏷 Water Quality Classification
WQI Range	Category
0 – 50	Excellent
51 – 100	Good
101 – 200	Poor
> 200	Very Poor
🎯 Future Improvements

Add data visualization charts

Add CSV upload option

Deploy as mobile-friendly app

Improve model accuracy with more data
