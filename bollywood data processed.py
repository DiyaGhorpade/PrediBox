import pandas as pd
df=pd.read_csv(r"c:\Users\aksha\Downloads\bollywood1to950.csv",skipinitialspace=True)
df.info()
print(df.isnull().sum()/len(df)*100)
df=df.apply(lambda X:X.str.strip() if X.dtype=='object' else X)
df.columns=df.columns.str.strip()
pd.read_table("bollywood1to950.csv",sep=r',',names=["Year","Rating","Runtime","Votes"])
df_cleaned = df.loc[:, ~df.isin(['']).any()]
print(df_cleaned)
from tabulate import tabulate
print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))
df_clean=df.dropna(axis=0)
print(tabulate(df_clean, headers='keys', tablefmt='pretty', showindex=False))
df_clean.to_csv('cleaned_data.csv', index=False)
print("Cleaned data saved to 'cleaned_data.csv'.")
