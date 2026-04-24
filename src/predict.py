import joblib
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(".."))
from src.feature_extractor import extract_features

MODEL_PATH = "models/phishing_model.pkl"
FEATURE_PATH = "models/feature_columns.pkl"

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURE_PATH)



def prepare_features(features_dict):
    df = pd.DataFrame([features_dict])
    
    # Align columns
    df = df.reindex(columns=feature_columns, fill_value=0)
    
    return df



def predict_url(url):
    try:
        features = extract_features(url)
        X = prepare_features(features)

        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0][1]

        return {
            "prediction": int(prediction),
            "probability": float(probability),
            "features": features
        }

    except Exception as e:
        return {
            "error": str(e)
        }



def interpret_result(features):
    reasons = []

    if features["url_length"] > 75:
        reasons.append("Unusually long URL")

    if features["entropy"] > 4:
        reasons.append("High randomness in URL")

    if features["num_dots"] > 3:
        reasons.append("Excessive subdomains")

    if features["num_digits"] > 5:
        reasons.append("High number of digits")

    if features["ip_in_url"] == 1:
        reasons.append("IP address used instead of domain")

    return reasons



def analyze_url(url):
    result = predict_url(url)

    if "error" in result:
        return result

    reasons = interpret_result(result["features"])

    return {
        "prediction": result["prediction"],
        "probability": result["probability"],
        "reasons": reasons
    }



