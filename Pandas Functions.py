# Pandas Functions

import pandas as pd

csv_1 = pd.read_csv("Resources\\big_data.csv")
print(csv_1.head(5))
print(
    csv_1.index,
    csv_1.columns,
    csv_1.describe(),
     )






