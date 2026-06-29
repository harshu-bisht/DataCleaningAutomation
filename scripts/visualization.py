import matplotlib.pyplot as plt

def sales_chart(df):
    if "Sales" in df.columns:
        plt.figure(figsize=(8,5))
        plt.hist(df["Sales"])
        plt.title("Sales Distribution")
        plt.xlabel("Sales")
        plt.ylabel("Frequency")
        plt.savefig("../reports/sales_distribution.png")
        plt.close()