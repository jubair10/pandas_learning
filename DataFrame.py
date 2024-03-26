"""
Difference between Dataframe and Series

A Series is a one-dimensional labeled array of data.

A DataFrame is a two-dimensional labeled array of data.

A Panel is a three-dimensional labeled array of data.


            DataFrame
    Name  Age         City
0   John   30     New York
1  Alice   25  Los Angeles
2    Bob   35      Chicago

            Series
Name                  [John, Alice, Bob]
Age                         [30, 25, 35]
City    [New York, Los Angeles, Chicago]


"""
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [30, 25, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}
# all value's length must be same


# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
