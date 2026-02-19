# 💳 Online Payment Fraud Detection System

## 📌 Project Title
Online Payment Fraud Detection using Machine Learning

## 👨‍💻 Team Details
*Team ID:* LTVIP2026TMIDS90110  
*Team Size:* 4  
### 👥 Team Members

* Rishitha Akula – Team Leader  
* Deekshitha Akepati – Team Member  
* Chamarthi Kavya Sree – Team Member  
* Gummalla Nandini – Team Member  

---
🛡️ Online Payments Fraud Detection using Machine Learning

A complete Machine Learning + Flask web application that detects fraudulent online payment transactions using multiple ML algorithms and deploys the selected model for real-time prediction.

## 📖 Project Overview

With the rapid growth of digital transactions, online payment fraud has become a serious issue for financial institutions. Detecting fraudulent transactions in real time is a challenging task due to highly imbalanced datasets.

This project builds a Machine Learning-based web application that predicts whether a transaction is:

- ✅ Safe Transaction  
- ⚠️ Fraudulent Transaction  

The system uses a Random Forest Classifier along with SMOTE to handle class imbalance.

---

## 🎯 Problem Statement

Online payment systems process thousands of transactions daily. Among these, only a small percentage are fraudulent, making fraud detection difficult.

Traditional rule-based systems fail to detect new fraud patterns. Therefore, we developed an intelligent ML-based system to analyze transaction patterns and identify fraudulent behavior effectively.

---

## 📊 Dataset Description

The dataset contains the following features:

1. *Step* – Time of transaction  
2. *Type* – Transaction type (TRANSFER, CASH_OUT, PAYMENT, etc.)  
3. *Amount* – Transaction amount  
4. *Old Balance Origin*  
5. *New Balance Origin*  
6. *Old Balance Destination*  
7. *New Balance Destination*  
8. *isFraud* – Target variable (0 = Safe, 1 = Fraud)

### Dataset Distribution:
- Safe Transactions: 465  
- Fraud Transactions: 35  

The dataset is imbalanced, which is handled using SMOTE (Synthetic Minority Oversampling Technique).

---

## 🧠 Machine Learning Model

### 🔹 Algorithm Used:
- Random Forest Classifier

### 🔹 Techniques Applied:
- Label Encoding (for transaction type)
- SMOTE (to balance dataset)
- Class Weight Balancing
- Fraud Probability Prediction

### 🔹 Model Accuracy:
Approximately *94% accuracy*

---

## 🌐 Web Application Features

The system is developed using Flask and includes:

- 🏠 Home Page  
- 📝 Fraud Detection Input Form  
- 📊 Prediction Result Page  
- 📈 Fraud Probability Percentage Output  

Users enter 7 transaction details, and the system predicts whether the transaction is safe or fraudulent.

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Joblib
- HTML & CSS

---

## 📂 Project Structure
fraud_project/
│
├── app.py
├── train_model.py
├── fraud_model.pkl
├── label_encoder.pkl
├── online_payment_fraud_dataset_sample.csv
├── requirements.txt
├── README.md
│
├── templates/
│   ├── home.html
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
git clone https://github.com/your-username/online-payment-fraud-detection.git� cd online-payment-fraud-detection
### 2️⃣ Install Dependencies
pip install -r requirements.txt
### 3️⃣ Train the Model
python train_model.py
### 4️⃣ Run the Application
python app.py
Open in browser:
 http://127.0.0.1:5000/
 ## 🔎 Fraud Pattern Observations

From analysis, fraud transactions mostly occur in:

- TRANSFER
- CASH_OUT

Fraud patterns include:
- Large transaction amounts
- Sudden balance drops to zero
- Suspicious transfer behavior

---

## 🔐 Real-World Applications

This system can help:

- Banks
- Financial Institutions
- Payment Gateways
- FinTech Companies

to reduce financial loss and improve transaction security.

---

## 📌 Conclusion

This project demonstrates how Machine Learning can be effectively used to detect fraudulent transactions in online payment systems. By balancing the dataset and optimizing the model, we built a practical fraud detection system with high accuracy and improved fraud detection capability.

---

## 📜 License

This project is developed for educational and internship purposes under SmartInternz.