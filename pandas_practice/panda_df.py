import pandas as pd

match= pd.read_csv("ipl-matches.csv")
# print(df.describe())
# print(match.keys())
# print(match['Date'].min(), match['Date'].max())
# print(match.iloc[1])
# print(match['ID'][0:12])
print(match['ID'][0:12].mean())
