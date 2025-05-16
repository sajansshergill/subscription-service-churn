import pandas as pd
import joblib
import os
from sklearn.metrics import classification_report, roc_auc_score
import matplotlib.pyplot as plt


def evaluate_model(data_path, model_path, report_path, chart_path):
    # Load data and model
    df = pd.read_csv(data_path)
    model = joblib.load(model_path)

    # Features and target
    features = ['account_age', 'monthly_spend', 'plan_type', 'support_tickets',
                'PaymentMethod', 'PaperlessBilling', 'ContentType', 'MultiDeviceAccess',
                'DeviceRegistered', 'ViewingHoursPerWeek', 'AverageViewingDuration',
                'ContentDownloadsPerMonth', 'GenrePreference', 'UserRating',
                'Gender', 'WatchlistSize', 'ParentalControl', 'SubtitlesEnabled']
    X = df[features]
    y = df['churn_label']

    # Predict
    y_pred = model.predict(X)
    y_proba = model.predict_proba(X)[:, 1]

    # Classification report and AUC
    report = classification_report(y, y_pred, output_dict=True)
    roc_auc = roc_auc_score(y, y_proba)

    # Save textual report
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, 'w') as f:
        f.write("Classification Report\n")
        f.write(classification_report(y, y_pred))
        f.write(f"\nROC AUC Score: {roc_auc:.4f}\n")

    # Feature importance
    importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=True)
    plt.figure(figsize=(8, 10))
    importances.plot(kind='barh')
    plt.title("Feature Importance")
    plt.tight_layout()
    plt.savefig(chart_path)
    print(f"Evaluation report saved to: {report_path}")
    print(f"Feature importance chart saved to: {chart_path}")


if __name__ == "__main__":
    evaluate_model(
        data_path="data/processed/preprocessed_churn_data.csv",
        model_path="scripts/churn_model.pkl",
        report_path="reports/churn_model_report.txt",
        chart_path="reports/feature_importance_chart.png"
    )
