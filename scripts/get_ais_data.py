import requests
import pandas as pd

response = requests.get(
    "https://hormuz.data-tracking.net/api/crossings/daily",
    params={"days": 250}
)
data = response.json()

df = pd.DataFrame(data)

df = df.pivot(index="day", columns="direction", values="count")
df = df.drop(columns=["in_strait"]).fillna(0).reset_index()
df[["inbound", "outbound"]] = df[["inbound", "outbound"]].astype(int) 

df.to_csv("data/raw/ais_raw.csv", index=False)
print(df.head(10))