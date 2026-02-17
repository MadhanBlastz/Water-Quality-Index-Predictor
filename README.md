# 💧 Water Quality Index (WQI) Predictor

---

## 📌 Project Overview
This project is a Machine Learning-based web application that predicts the **Water Quality Index (WQI)** using important physicochemical water parameters.  
It helps determine whether water is safe or unsafe based on scientific measurements.

The application is built using:
- Python
- Streamlit
- Scikit-learn
- NumPy
- Joblib

🚀 **Live App:**  
👉 https://water-quality-index-predictor.streamlit.app/

---

## ⚙️ Features
- ✅ User-friendly Streamlit interface  
- ✅ Real-time WQI prediction
- ✅ Color-coded water quality classification  
- ✅ Automatic preprocessing (Imputer + Scaler)  
- ✅ ML model integration (.pkl files)  
- ✅ Lightweight and easy to deploy  

---

## 📊 Input Parameters
The model accepts the following water quality parameters:

- pH  
- TDS (Total Dissolved Solids)  
- Chloride (Cl)  
- Sulphate (SO4)  
- Sodium (Na)  
- Potassium (K)  
- Calcium (Ca)  
- Magnesium (Mg)  
- Total Hardness  

---

## 🧠 Machine Learning Model
- Trained using water quality dataset  
- Model file: `hybrid_wqi_model.pkl`  
- Preprocessing files:
  - `imputer.pkl`
  - `scaler.pkl`
- Used Scikit-learn for training and prediction  

---

## 🏷 Water Quality Classification

| WQI Range | Category      |
|-----------|--------------|
| 0 – 50    | Excellent    |
| 51 – 100  | Good         |
| 101 – 200 | Poor         |
| > 200     | Very Poor    |

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/MadhanBlastz/water-quality-index-predictor.git
cd water-quality-index-predictor
```

### 2️⃣ Install dependencies
```bash
pip install numpy pandas
pip install streamlit joblib xgboost
pip install scikit-learn==1.7.2
```

### 3️⃣ Run the application
```bash
streamlit run app.py
```

---

## 🌐 Deployment
You can deploy this project for free on:

- Streamlit Community Cloud (Recommended)
- Render
- Railway

---

## 📂 Project Structure
```
Water-Quality-Index-Predictor/
│
├──.ipynb_checkpoints
├──Water_Final.ipynb
├── app.py
├──data.docx
├──requirements.txt
├── hybrid_wqi_model.pkl
├── scaler.pkl
├── imputer.pkl
└── README.md
```

---

## 🎯 Future Improvements
- 📊 Add graphical visualizations  
- 📁 Add CSV file upload option  
- 📱 Improve mobile responsiveness  
- 📈 Improve model accuracy with larger dataset  
- 🔐 Add authentication system  

---

## 👨‍💻 Author
**Madhankumar**

- LinkedIn: 
- GitHub:  

---

⭐ If you like this project, consider giving it a star!
