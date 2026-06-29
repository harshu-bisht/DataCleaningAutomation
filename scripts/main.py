from cleaning import load_data, clean_data, save_data
from report import generate_report
from visualization import sales_chart
import pandas as pd

df = load_data("data/raw_data.xlsx")

df = clean_data(df)

save_data(df, "data/cleaned_data.xlsx")

report = generate_report(df)

pd.DataFrame([report]).to_excel("reports/report.xlsx", index=False)

sales_chart(df)

print("Project Completed Successfully!")