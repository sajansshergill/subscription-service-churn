import pandas as pd
import joblib
import os


def export_for_dashboard(data_path, model_path, output_path):
    # Load data and model
    df = pd.read_csv(data_path)
    model = joblib.load(model_path)

    # Define features used in the model
    features = ['account_age', 'monthly_spend', 'plan_type', 'support_tickets',
                'PaymentMethod', 'PaperlessBilling', 'ContentType', 'MultiDeviceAccess',
                'DeviceRegistered', 'ViewingHoursPerWeek', 'AverageViewingDuration',
                'ContentDownloadsPerMonth', 'GenrePreference', 'UserRating',
                'Gender', 'WatchlistSize', 'ParentalControl', 'SubtitlesEnabled']

    # Predict probabilities
    df['churn_probability'] = model.predict_proba(df[features])[:, 1]

    # Select relevant fields for dashboard
    export_cols = ['customer_id', 'account_age', 'monthly_spend', 'plan_type', 'support_tickets',
                   'churn_label', 'churn_probability']

    df_dashboard = df[export_cols]

    # Save for dashboard
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df_dashboard.to_csv(output_path, index=False)
    print(f"Dashboard-ready data saved to: {output_path}")


if __name__ == "__main__":
    export_for_dashboard(
        data_path="data/processed/preprocessed_churn_data.csv",
        model_path="scripts/churn_model.pkl",
        output_path="data/processed/churn_predictions.csv"
    )
