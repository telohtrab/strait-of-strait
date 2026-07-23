import pandas as pd

janmar = pd.read_csv("./data/raw/ukmto_raw.csv")
marjul = pd.read_csv("./data/raw/ais_raw.csv")

janmar = janmar.drop(columns=['total'])
janmar = janmar.dropna()

janmar = janmar.rename(columns={'day': 'date'})
marjul = marjul.rename(columns={'day': 'date'})

janmar["inbound"] = janmar['inbound'].astype(int)
janmar["outbound"] = janmar['outbound'].astype(int)

merged = pd.concat([janmar, marjul])
merged = merged.sort_values(by='date').reset_index(drop=True)

merged["date"] = pd.to_datetime(merged['date'])
expected = pd.date_range(start=merged["date"].min(), end=merged["date"].max(), freq="D")
missing = expected.difference(merged['date'])
print(missing)

if len(missing) == 0:
    print(merged.head())
    print(merged.tail())

merged.to_csv("data/transits.csv", index=False)