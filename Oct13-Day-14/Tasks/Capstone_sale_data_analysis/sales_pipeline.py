import pandas as pd
from datetime import datetime

def sales_pipeline():
    products = pd.read_csv("products.csv")
    orders = pd.read_csv("orders.csv")
    customers = pd.read_csv("customersss.csv")

    new=pd.merge(orders, customers,how="inner", on="CustomerID")
    processed_orders= pd.merge(new,products,how="inner", on="ProductID")

    processed_orders["TotalAmount"] = processed_orders["Quantity"] * processed_orders["Price"]

    processed_orders["Month"]= pd.to_datetime(processed_orders["OrderDate"]).dt.month

    filtered = processed_orders[
        (processed_orders["Quantity"] >= 2) &
        (processed_orders["Country"].isin(["India", "UAE"]))
        ]
    category_summary = filtered.groupby("Category")["TotalAmount"].sum().reset_index()
    segment_summary = filtered.groupby("Segment")["TotalAmount"].sum().reset_index()

    # Step 5: Sorting & Ranking
    customer_revenue = filtered.groupby("CustomerID")["TotalAmount"].sum().reset_index()
    customer_revenue = customer_revenue.sort_values(by="TotalAmount", ascending=False)

    # Merge sorted revenue back into filtered data for enriched output
    enriched_orders = filtered.merge(customer_revenue, on="CustomerID", suffixes=("", "_CustomerTotal"))

    # 3. Load
    enriched_orders.to_csv("processed_orders.csv", index=False)
    category_summary.to_csv("category_summary.csv", index=False)
    segment_summary.to_csv("segment_summary.csv", index=False)


# Run the pipeline
if __name__ == "__main__":
    sales_pipeline()
