# 📊 Data Cleaning & Reporting Automation

## Overview

This project automates the process of cleaning, preprocessing, and reporting data using Python. It removes duplicate records, handles missing values, standardizes text formatting, generates summary reports, and visualizes cleaned data using Power BI.

This project demonstrates an end-to-end data cleaning workflow suitable for data analysis and business reporting.

---

## Features

* Read raw Excel datasets
* Remove duplicate records
* Handle missing values
* Standardize text formatting
* Generate cleaned Excel dataset
* Create automated summary reports
* Visualize data using Power BI
* Generate sales charts

---

## Technologies Used

* Python
* Pandas
* OpenPyXL
* Matplotlib
* Excel
* Power BI
* Git & GitHub

---

## Project Structure

```text
DataCleaningAutomation/
│
├── data/
│   ├── raw_data.xlsx
│   └── cleaned_data.xlsx
│
├── reports/
│   └── report.xlsx
│
├── scripts/
│   ├── cleaning.py
│   ├── report.py
│   ├── visualization.py
│   └── main.py
│
├── dashboard/
│   └── DataCleaningDashboard.pbix
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Workflow

1. Load raw Excel data.
2. Remove duplicate records.
3. Handle missing values.
4. Standardize text formatting.
5. Save cleaned data.
6. Generate summary report.
7. Create Power BI dashboard.

---

## Power BI Dashboard

The dashboard includes:

* KPI Cards
* Total Sales
* Average Sales
* Total Records
* Sales by City
* Sales Distribution
* Interactive Filters

---

## How to Run

### Clone the repository

```bash
git clone https://github.com/harshu-bisht/DataCleaningAutomation.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python scripts/main.py
```

---

## Future Improvements

* Database integration (MySQL)
* Automatic outlier detection
* Interactive dashboard filtering
* Scheduled data cleaning
* Cloud deployment

---

## Author

**Harshit Bisht**

GitHub: https://github.com/harshu-bisht

LinkedIn: https://www.linkedin.com/in/harshit-bisht-832401309/
