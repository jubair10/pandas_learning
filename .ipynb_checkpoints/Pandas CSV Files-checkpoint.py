""" Pandas CSV Files (Write and Read) """

import pandas as pd

# lst = ["Geeks", "For", "Geeks", "is", "portal", "for", "Geeks"]

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

df = pd.DataFrame(data)
# print(df)

# Writing
# df.to_csv("Resources/data.csv",index=False)
import time

# time.sleep(3)

# df.to_csv("Resources/data.csv")


# Reading

col_names = [
    "Company",
    "Name",
    "Price",
    "Quantity",
    "Demand",
    "Interest",
    "Ratings",
    "Niche",
    "Stock",
]
# nrows
# nrows=2 ---> read first 2 rows
# nrows=None ---> read all rows

csv = pd.read_csv("Resources\\big_data.csv", names=col_names, nrows=2)

# print(csv)


# usecols
# usecols=["Company", "Name"] ---> by column name
# usecols=[0,8] ---> by column indexing
csv_1 = pd.read_csv("Resources\\big_data.csv", usecols=[0,8])
# print(csv_1.head())

# skiprows

csv_2 = pd.read_csv("Resources\\big_data.csv", skiprows=[2,3], usecols=[1,2])
# print(csv_2.head(5))

# index_col

csv_3 = pd.read_csv("Resources\\big_data.csv", index_col="Price")
print(csv_3.columns)
print(csv_3.head(5))

# header and prefixes

csv_4 = pd.read_csv("Resources\\big_data.csv", header=None,)
print(csv_4.columns)
print(csv_4.head(5))