
import pandas as pd
import numpy as np
csv = pd.read_csv("Resources\\big_data_num.csv")
csv.head(10)


csv.replace(to_replace=np.nan,value=22,inplace=True)
print(csv)
