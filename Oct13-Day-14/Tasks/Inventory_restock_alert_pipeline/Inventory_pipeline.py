import pandas as pd
from datetime import datetime
def b_pipeline():
    df=pd.read_csv("inventory.csv")
    df["RestockNeeded"]= df.apply(lambda x: "Yes" if x["Quantity"] < x["ReorderLevel"] else "No", axis=1)
    df["Total_price"]= df["Quantity"] * df["PricePerUnit"]
    df.to_csv("restock_report.csv", index=False)
    print(f"Inventory pipeline completed at {datetime.now()}")

if __name__ == "__main__":
    b_pipeline()