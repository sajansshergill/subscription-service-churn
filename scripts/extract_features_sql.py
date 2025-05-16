import sqlite3
import pandas as pd
import os

def extract_features_from_sql(db_path, output_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Define SQL query to join tables and create a flat view
    query = """
        SELECT 
            c.customer_id,
            c.account_age,
            c.plan_type,
            c.payment_method,
            u.ViewingHoursPerWeek,
            u.AverageViewingDuration,
            u.ContentDownloadsPerMonth,
            u.GenrePreference,
            u.UserRating,
            s.SupportTicketsPerMonth AS support_tickets,
            ch.monthly_spend,
            ch.churn_label
        FROM customers c
        LEFT JOIN usage_logs u ON c.customer_id = u.customer_id
        LEFT JOIN support_tickets s ON c.customer_id = s.customer_id
        LEFT JOIN churn_info ch ON c.customer_id = ch.customer_id
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    # Save extracted features to CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Feature dataset saved to: {output_path}")


if __name__ == "__main__":
    extract_features_from_sql(
        db_path="data/subscription_churn.db",
        output_path="data/processed/sql_flattened_features.csv"
    )
