import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load(r"C:\Users\nivis\OneDrive\Desktop\2nd sem IDT\data-exfiltration-camouflage\models\isolation_forest.pkl")
scaler = joblib.load(r"C:\Users\nivis\OneDrive\Desktop\2nd sem IDT\data-exfiltration-camouflage\models\scaler.pkl")

def detect(features):
    """
    Takes input features of a network packet
    Returns: True = Attack, False = Normal
    """

    # Convert to numpy array
    features = np.array(features).reshape(1, -1)

    # Scale input
    features_scaled = scaler.transform(features)

    # Predict using Isolation Forest
    prediction = model.predict(features_scaled)

    # -1 = anomaly (attack), 1 = normal
    if prediction[0] == -1:
        return True
    else:
        return False