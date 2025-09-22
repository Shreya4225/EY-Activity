import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Priya", "Arjun", "Neha", "Vikram"],
    "Age": [21, 22, 20, 23, 21],
    "Course": ["AI", "ML", "Data Science", "AI", "ML"],
    "Marks": [85, 90, 78, 88, 95]
}

df=pd.DataFrame(data)
#print(df)

# print(df["Name"]) #Single col
# print(df[["Name","Age"]]) #print multiple col
# print(df.iloc[0]) #print first row
# print(df.loc[2,"Marks"]) #print marks as 2nd position
#
# high_scores=df[df["Marks"]>85] #filtering records
# print(high_scores)

df["results"]=np.where(df["Marks"]>80,"Pass", "Fail")

df.loc[df["Name"]=="Neha", "Marks"]=90
print(df)