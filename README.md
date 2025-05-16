# Customer Churn Prediction & Insights Dashboard for a Subscription Service

## 📌 Problem Statement:
Subscription-based services (e.g., SaaS platforms or streaming apps) lose significant revenue due to customer churn. Early detection and interpretation of churn signals can help businesses take preventive actions. This project aims to build a predictive churn model, generate insights from customer behavior, and present them in a business-friendly dashboard.

---

## 🧱 Project Components:
1. Data Collection

Simulated data from Kaggle or mock-generated datasets with fields like:

- customer_id, signup_date, last_login, monthly_spend, plan_type, support_tickets, churn_label

2. Database (SQL)
Use PostgreSQL or MySQL

Tables:

- customers: basic info
- usage_logs: login frequency, content usage
- billing: monthly payments
- support_tickets: customer issues

---

## Project Structure
customer_churn_dashboard_project/
│
├── data/
│   ├── raw/
│   │   └── Subscription_Service_Churn_Dataset.csv
│   └── processed/
│       └── churn_predictions.csv
│
├── notebooks/
│   └── churn_model_dev.ipynb
│
├── scripts/
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── evaluate_model.py
│   └── export_dashboard_data.py
│
├── reports/
│   ├── churn_model_report.pdf
│   └── feature_importance_chart.png
│
├── dashboard/
│   └── churn_dashboard.pbix  # or .twbx for Tableau
│
├── utils/
│   └── helpers.py
│
├── README.md
└── requirements.txt

---

## Storytelling & Delivery
Deliverables:

- PowerPoint slide deck summarizing the problem, insights, key drivers, and recommendations

- A live dashboard walkthrough

- A brief document highlighting:

  - Hypotheses tested

  - Model performance

  - Suggested actions to reduce churn (e.g., improve support response times)

---

## 🧠 Tools & Skills Practiced
- SQL: PostgreSQL for querying relational datasets

- Python: pandas, sklearn, seaborn, numpy

- Stats: t-tests, logistic regression

- ML: Random Forest Classifier

- BI: Power BI or Tableau dashboarding

- Soft Skills: Insight communication, stakeholder storytelling

