import os
import pandas as pd

def generate_report(df):
    report = {
        "Total Rows": len(df),
        "Total Columns": len(df.columns),
        "Missing Values": df.isnull().sum().sum(),
        "Duplicate Rows": df.duplicated().sum()
    }

    report_df = pd.DataFrame(report.items(), columns=["Metric", "Value"])

    os.makedirs("../reports", exist_ok=True)

    report_df.to_excel("../reports/report.xlsx", index=False)

    print("Report Generated Successfully!")