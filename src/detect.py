import joblib
import numpy as np

model = joblib.load(r"C:\Users\nivis\OneDrive\Desktop\2nd sem IDT\data-exfiltration-camouflage\models\isolation_forest.pkl")
scaler = joblib.load(r"C:\Users\nivis\OneDrive\Desktop\2nd sem IDT\data-exfiltration-camouflage\models\scaler.pkl")

def detect(features):

    features = np.array(features).reshape(1, -1)
    features_scaled = scaler.transform(features)

    prediction = model.predict(features_scaled)
    score = model.decision_function(features_scaled)[0]

    return {
        "label": "ANOMALY" if prediction[0] == -1 else "NORMAL",
        "score": float(score)
    }