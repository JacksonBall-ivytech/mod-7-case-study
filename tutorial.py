import pandas as pd

# 1. Create
df = pd.read_csv('telco_churn.csv')
tempdict = {'coll':[1, 2, 3], 'col2':[4, 5, 6], 'col3':[7, 8, 9]}
dictdf = pd.DataFrame.from_dict(tempdict)

# 2. Read
# 2.1
print(df.head(10))
print(dictdf.head())
print(df.tail())
# 2.2
print(df.columns)
print(df.dtypes)
# 2.3
print(df.describe())
print(df.describe(include=object))
# 2.4
print(df.State)
print(df['International plan'])
print(df[['State', 'International plan']])
print(df.State.unique())
# 2.5
print(df.head())
print(df[df['International plan']=='No'])
print(df[(df['International plan']=='No') & (df['Churn']==True)] )
# 2.6
print(df.iloc[14])
print(df.iloc[14, 0])
print(df.iloc[22:23])
# 2.7
state = df.copy()
state.set_index('State', inplace=True)
print(state.head())
print(state.loc['OH'])