import pandas as pd
from datetime import datetime

def a_pipeline():
    df = pd.read_csv("customers.csv")
    df = df[df["Age"]>=20]

    df["Age_group"]=df["Age"].apply(lambda x: "Young" if x < 30 else "Adult" if x < 50 else "Senior")
    df.to_csv("filtered_customers.csv", index= False)
    print("pipeline completed")

if __name__ == "__main__":
    a_pipeline()