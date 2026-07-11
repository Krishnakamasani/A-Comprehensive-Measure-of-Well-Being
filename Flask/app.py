# ============================
# Import Required Libraries
# ============================

# NumPy is used for numerical operations
import numpy as np

# Pandas is used to create a DataFrame for prediction
import pandas as pd

# Flask libraries
from flask import Flask, render_template, request
# Pickle is used to load the saved machine learning model
import pickle


# ============================
# Initialize Flask Application
# ============================
app = Flask(__name__)
# ============================
# Load the Trained Model
# ============================

# Load the saved Linear Regression model
model = pickle.load(open("HDI.pkl", "rb"))


# ============================
# Home Page Route
# ============================

@app.route("/")
def home():
    """
    Displays the Home Page.
    """
    return render_template("index.html")


# ============================
# Prediction Page Route
# ============================

@app.route("/Prediction", methods=["GET", "POST"])
def prediction():
    """
    Opens the prediction page.
    """
    return render_template("index.html")


# Optional route (same as home page)

@app.route("/Home", methods=["GET", "POST"])
def my_home():
    return render_template("index.html")


# ============================
# Prediction Route
# ============================

@app.route("/predict", methods=["POST"])
def predict():

    # Read user inputs from the HTML form
    input_features = [float(x) for x in request.form.values()]

    # Convert input into NumPy array
    feature_array = np.array(input_features)

    # Feature names (must match training data)
    feature_names = [
        "Life expectancy at birth",
        "Expected years of schooling",
        "Mean years of schooling",
        "Gross national income (GNI) per capita"
    ]

    # Convert array into DataFrame
    df = pd.DataFrame([feature_array], columns=feature_names)

    # Predict HDI
    prediction = model.predict(df)

    # Round prediction to 2 decimal places
    hdi = round(float(prediction[0]), 2)

    # Categorize the HDI value
    if 0.30 <= hdi < 0.40:
        result = f"Low HDI : {hdi}"

    elif 0.40 <= hdi < 0.70:
        result = f"Medium HDI : {hdi}"

    elif 0.70 <= hdi < 0.80:
        result = f"High HDI : {hdi}"

    elif hdi >= 0.80:
        result = f"Very High HDI : {hdi}"

    else:
        result = f"The given values do not match the expected range. HDI = {hdi}"

    return render_template(
        "result.html",
        prediction_text=result
    )


# ============================
# Run the Flask Application
# ============================

if __name__ == "__main__":
    app.run(debug=True, port=5000)