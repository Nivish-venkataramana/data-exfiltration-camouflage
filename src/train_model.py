import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv(r"C:\Users\nivis\OneDrive\Desktop\2nd sem IDT\data-exfiltration-camouflage\data\raw data\Monday-WorkingHours.pcap_ISCX.csv.zip")
df = pd.read_csv(r"C:\Users\nivis\OneDrive\Desktop\2nd sem IDT\data-exfiltration-camouflage\data\raw data\Tuesday-WorkingHours.pcap_ISCX.csv.zip")


# Clean column names
df.columns = df.columns.str.strip()

# Replace infinite values
df = df.replace([np.inf, -np.inf], np.nan)

# Remove missing values
df = df.dropna()

# Keep only numeric columns
df = df.select_dtypes(include=['float64', 'int64'])

# Feature selection
features = [
    'Flow Duration',
    'Total Fwd Packets',
    'Total Backward Packets',
    'Flow Bytes/s',
    'Flow Packets/s'
]

# Keep only available features
features = [f for f in features if f in df.columns]

df = df[features]

# Final cleaning
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()

# Scaling
scaler = StandardScaler()
X = scaler.fit_transform(df)

# Train Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

model.fit(X)

# Save model + scaler
joblib.dump(model, r"C:\Users\nivis\OneDrive\Desktop\2nd sem IDT\data-exfiltration-camouflage\models\isolation_forest.pkl")
joblib.dump(scaler, r"C:\Users\nivis\OneDrive\Desktop\2nd sem IDT\data-exfiltration-camouflage\models\scaler.pkl")

print("Model training completed successfully!")