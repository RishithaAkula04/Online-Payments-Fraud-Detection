from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("fraud_model.pkl")
le = joblib.load("label_encoder.pkl")

# HOME PAGE
@app.route("/")
def home():
    return render_template("home.html")

# FRAUD DETECTION PAGE
@app.route("/fraud")
def fraud():
    return render_template("index.html", types=le.classes_)

# PREDICTION
@app.route("/predict", methods=["POST"])
def predict():

    step = float(request.form["step"])
    trans_type = request.form["type"]
    amount = float(request.form["amount"])
    oldbalanceOrg = float(request.form["oldbalanceOrg"])
    newbalanceOrig = float(request.form["newbalanceOrig"])
    oldbalanceDest = float(request.form["oldbalanceDest"])
    newbalanceDest = float(request.form["newbalanceDest"])

    type_encoded = le.transform([trans_type])[0]

    features = np.array([[step,
                          type_encoded,
                          amount,
                          oldbalanceOrg,
                          newbalanceOrig,
                          oldbalanceDest,
                          newbalanceDest]])

    prediction = model.predict(features)[0]

    result = "Fraud Transaction" if prediction == 1 else "Safe Transaction"

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
