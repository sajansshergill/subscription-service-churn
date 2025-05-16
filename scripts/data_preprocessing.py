import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import os

import os

base_dir = os.path.dirname(os.path.dirname(__file__))  # go up from /scripts
input_path = os.path.join(base_dir, "data/raw/Subscription_Service_Churn_Dataset.csv")
output_path = os.path.join(base_dir, "data/processed/preprocessed_churn_data.csv")

def preprocess_data(input_path, output_path):
    # Load dataset
    df = pd.read_csv(input_path)

    # Rename columns to align with project schema
    df.rename(columns={
        'CustomerID': 'customer_id',
        'AccountAge': 'account_age',
        'MonthlyCharges': 'monthly_spend',
        'SubscriptionType': 'plan_type',
        'SupportTicketsPerMonth': 'support_tickets',
        'Churn': 'churn_label'
    }, inplace=True)

    # Handle missing numeric values with median
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].median())

    # Handle missing categorical values with mode
    cat_cols = df.select_dtypes(include=['object']).columns
    df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

    # Encode categorical columns
    label_encoders = {}
    for col in ['plan_type', 'PaymentMethod', 'PaperlessBilling', 'ContentType',
                'MultiDeviceAccess', 'DeviceRegistered', 'GenrePreference', 'Gender',
                'ParentalControl', 'SubtitlesEnabled']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Save preprocessed data
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to: {output_path}")

if __name__ == "__main__":
    preprocess_data(
        input_path="data/raw/Subscription_Service_Churn_Dataset.csv",
        output_path="data/processed/preprocessed_churn_data.csv"
    )
