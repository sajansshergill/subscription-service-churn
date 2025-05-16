import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib


def train_model(input_path, model_output_path):
    # Load preprocessed data
    df = pd.read_csv(input_path)

    # Select features and target
    features = ['account_age', 'monthly_spend', 'plan_type', 'support_tickets',
                'PaymentMethod', 'PaperlessBilling', 'ContentType', 'MultiDeviceAccess',
                'DeviceRegistered', 'ViewingHoursPerWeek', 'AverageViewingDuration',
                'ContentDownloadsPerMonth', 'GenrePreference', 'UserRating',
                'Gender', 'WatchlistSize', 'ParentalControl', 'SubtitlesEnabled']

    X = df[features]
    y = df['churn_label']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save model
    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)
    joblib.dump(model, model_output_path)
    print(f"Model saved to: {model_output_path}")

if __name__ == "__main__":
    train_model(
        input_path="data/processed/preprocessed_churn_data.csv",
        model_output_path="scripts/churn_model.pkl"
    )
