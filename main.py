import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.utils import resample #help us do downsampling
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.ensemble import RandomForestClassifier #ml model we will use to train our data
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

with open("rainfall_prediction_model.pkl", "rb") as file:
  model_data = pickle.load(file)

@app.route("/")
def home():
  return "Rainfall prediction app is running"

@app.route("/predict", methods=["POST"])
def predict():
  try:
    # get json data from api request
    data = request.get_json()

    input_data = pd.DataFrame([data])

    # check if input is provided
    if not data:
      return jsonify({"error": "input data not found"}), 400
    
    required_cols = ["pressure","maxtemp", "dewpoint", "humidity", "cloud", "sunshine", "winddirection", "windspeed"]
    if not all(col in input_data.columns for col in required_cols):
      return jsonify({"error": f"all input data not found, Required columns :{required_cols}"}), 400
    
    model = model_data["model"]
    feature_names = model_data["feature_names"]
    input_data = pd.DataFrame([data], columns=feature_names)

    prediction = model.predict(input_data)
    res = {
      "prediction result":"rainfall" if prediction[0] == 1 else "no rainfall"
    }
    return jsonify(res)


  except Exception as e:
    return jsonify({"error": str(e)}), 500
  
if __name__ == "__main__":
  app.run(debug=True)
