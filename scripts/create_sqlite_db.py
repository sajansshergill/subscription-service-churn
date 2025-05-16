import pandas as pd
import sqlite3
import os

def create_sqlite_database(csv_path, db_path):
    # Load the flat CSV data
    df = pd.read_csv(csv_path)

    # Simulate table splits
    customers = df[['CustomerID', 'AccountAge', 'SubscriptionType', 'PaymentMethod']].copy()
    customers.rename(columns={
        'CustomerID': 'customer_id',
        'AccountAge': 'account_age',
        'SubscriptionType': 'plan_type',
        'PaymentMethod': 'payment_method'
    }, inplace=True)

    usage_logs = df[['CustomerID', 'ViewingHoursPerWeek', 'AverageViewingDuration',
                     'ContentDownloadsPerMonth', 'GenrePreference', 'UserRating']].copy()
    usage_logs.rename(columns={'CustomerID': 'customer_id'}, inplace=True)

    support_tickets = df[['CustomerID', 'SupportTicketsPerMonth']].copy()
    support_tickets.rename(columns={'CustomerID': 'customer_id'}, inplace=True)

    churn_data = df[['CustomerID', 'MonthlyCharges', 'Churn']].copy()
    churn_data.rename(columns={
        'CustomerID': 'customer_id',
        'MonthlyCharges': 'monthly_spend',
        'Churn': 'churn_label'
    }, inplace=True)

    # Create database
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)

    # Write tables to database
    customers.to_sql('customers', conn, if_exists='replace', index=False)
    usage_logs.to_sql('usage_logs', conn, if_exists='replace', index=False)
    support_tickets.to_sql('support_tickets', conn, if_exists='replace', index=False)
    churn_data.to_sql('churn_info', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()
    print(f"SQLite database created at: {db_path}")


if __name__ == "__main__":
    create_sqlite_database(
        csv_path="data/raw/Subscription_Service_Churn_Dataset.csv",
        db_path="data/subscription_churn.db"
    )
