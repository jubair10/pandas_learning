# Delete and Insert

import pandas as pd


data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

df = pd.DataFrame(data)
print(df)

df = df.drop("Age", axis=1)
df = df.drop(1, axis=0)
print(df)

#  insert or add with another vaiable with dataframe


data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

df = pd.DataFrame(data)
print(df)

df.insert(1, "Country", ("USA", "Canada", "UK"))
print(df)


df["New Column"] = df["Age"] + 3

print(df)

df["New Column 2"] = df["Age"][:2] + 3
print(df)


# To delete , we can use del keyword, pop function


# dlted= df.pop("Age")

# # 0    30
# # 1    25
# # 2    35
# # Name: Age, dtype: int64

# print(dlted)
# print(df)


del df["Age"], df["City"]

print(df)
df.drop