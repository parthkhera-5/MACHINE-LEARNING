from flask import Flask, render_template, request, redirect, session
import numpy as np
import joblib
import os

app = Flask(__name__)
app.secret_key = "12a"  # Needed for session storage

# Load models with joblib
model_path = os.path.join("models", "voting_model.joblib")  # or voting_model.joblib if you saved as .joblib
threshold_path = os.path.join("models", "threshold.joblib")  # optional, if you have a custom threshold

voting_model = joblib.load(model_path)
threshold = joblib.load(threshold_path)  # if needed for custom threshold

# ------------------- Routes -------------------

# Dashboard
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

# Step 1: Personal Details
@app.route("/personal_detail", methods=["GET", "POST"])
def personal_detail():
    if request.method == "POST":
        session['name'] = request.form['name']
        session['age'] = int(request.form['age'])
        session['sex'] = int(request.form['sex'])
        session['edu'] = int(request.form['edu'])
        return redirect("/smoking_detail")
    return render_template("personal_details.html")

# Step 2: Smoking Details
@app.route("/smoking_detail", methods=["GET", "POST"])
def smoking_detail():
    if request.method == "POST":
        session['isSmoking'] = int(request.form['isSmoking'])
        session['cigsPerDay'] = float(request.form['cigsPerDay'])
        return redirect("/medical_detail")
    return render_template("smoking_detail.html")

# Step 3: Medical History
@app.route("/medical_detail", methods=["GET", "POST"])
def medical_detail():
    if request.method == "POST":
        session['BPMeds'] = int(request.form['BPMeds'])
        session['prevalentStroke'] = int(request.form['prevalentStroke'])
        session['prevalentHyp'] = int(request.form['prevalentHyp'])
        session['diabetes'] = int(request.form['diabetes'])
        return redirect("/medical_checkup")
    return render_template("medical_detail.html")

# Step 4: Medical Checkup
@app.route("/medical_checkup", methods=["GET", "POST"])
def medical_checkup():
    if request.method == "POST":
        session['total_cholesterol'] = float(request.form['total_cholesterol'])
        session['sysBP'] = float(request.form['sysBP'])
        session['diaBP'] = float(request.form['diaBP'])
        session['bmi'] = float(request.form['bmi'])
        session['heart_rate'] = float(request.form['heart_rate'])
        session['glucose'] = float(request.form['glucose'])
        return redirect("/submit")
    return render_template("medical_checkup.html")

# Step 5: Submit & Predict
@app.route("/submit")
def submit():
    # Derived Features
    age_group = 0
    age = session['age']
    if age < 30:
        age_group = 0
    elif age <= 45:
        age_group = 1
    elif age <= 60:
        age_group = 2
    else:
        age_group = 3

    totChol = session['total_cholesterol']
    if totChol < 200:
        chol_category = 0
    elif totChol < 240:
        chol_category = 1
    else:
        chol_category = 2

    bmi = session['bmi']
    if bmi < 18.5:
        bmi_category = 0
    elif bmi < 25:
        bmi_category = 1
    elif bmi < 30:
        bmi_category = 2
    else:
        bmi_category = 3

    smoking_intensity = session['isSmoking'] * session['cigsPerDay']
    pulse_rate = session['heart_rate']

    # Feature array for model
    features = np.array([[
        session['age'],
        session['sex'],
        session['isSmoking'],
        session['cigsPerDay'],
        session['BPMeds'],
        session['prevalentStroke'],
        session['prevalentHyp'],
        session['diabetes'],
        totChol,
        session['sysBP'],
        session['diaBP'],
        session['bmi'],
        session['heart_rate'],
        session['glucose'],
        smoking_intensity,
        pulse_rate,
        age_group,
        chol_category,
        bmi_category
    ]])

    # Prediction
    prob = voting_model.predict_proba(features)[0][1]

    # Optional: apply threshold if you saved a custom one
    if threshold:
        pred = (prob >= threshold).astype(int)
    else:
        pred = (prob >= 0.5).astype(int)

    risk_message = f"Your estimated cardiovascular risk is {prob*100:.2f}%"

    return render_template("submit.html", risk_message=risk_message)


# ------------------- Run App -------------------
if __name__ == "__main__":
    app.run(debug=True)
