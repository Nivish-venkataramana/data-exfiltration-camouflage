import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(path):
    return pd.read_csv(path)

def preprocess(df):

    df = df.dropna()

    df = df.select_dtypes(include=['float64', 'int64'])

    features = [
        'Flow Duration',
        'Total Fwd Packets',
        'Total Backward Packets',
        'Flow Bytes/s',
        'Flow Packets/s'
    ]

    df = df[features]

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)

    return df_scaled, scaler