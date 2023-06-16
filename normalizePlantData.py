import pandas as pd

# データフレームの作成
df = pd.read_csv('sumCountryCode.csv')#植物名は列名になる

print(df)

# 最小値0、最大値1に正規化する関数
def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

# データフレームの2列目以降の列に関数を適用、0,1行目にはCountryCodeが入っているため
df.iloc[:, 2:] = df.iloc[:, 2:].apply(normalize)

print(df[110:120])#アシタバのJPで正規化を確認
df.to_csv("normalizedCountryPlantDada.csv",index = False)
