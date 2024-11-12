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

# 3. Update
# 3.1
print(df.isnull().sum())
df.dropna(inplace=True)
print(df.isnull().sum())
# 3.2
print(df.drop('Area code', axis=1))
# 3.3
df['New Column'] = df['Total night minutes'] + df['Total intl minutes']
print(df.head())
# 3.4
df['New Column'] = 100
print(df.head())
# 3.5
df.iloc[0, -1] = 10
print(df.head())
# 3.6
df['Churn Binary'] = df['Churn'].apply(lambda x: 1 if x== True else 0)
print(df[df['Churn']==True].head())

# 4. Delete/Output
df.to_csv('output.csv')
df.to_json()
df.to_html()
del df