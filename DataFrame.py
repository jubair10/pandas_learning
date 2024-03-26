"""
Difference between Dataframe and Series
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

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
