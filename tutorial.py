import pandas as pd

# 1. Create
df = pd.read_csv('telco_churn.csv')
tempdict = {'coll':[1, 2, 3], 'col2':[4, 5, 6], 'col3':[7, 8, 9]}
dictdf = pd.DataFrame.from_dict(tempdict)

# 2. Read
print(df.head(10))
print(dictdf.head())