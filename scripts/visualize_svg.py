import math

import pandas as pd
import matplotlib.pyplot as pl

# Dark-fleet adjustment: AIS undercounts real traffic (ghost ships, transponders
# switched off). Research-backed flat addition, see data/SOURCES.md > Limitations.
DARK_FLEET_ADJUSTMENT = 5

# Rolling window (days) used to smooth the daily counts before drawing the
# coastline. Keeps the profile a bit jagged, but blunts single-day noise.
SMOOTHING_WINDOW_DAYS = 7

# Horizontal stretch to get a more realistic strait
X_STRETCH = 2

df = pd.read_csv("./data/transits.csv")
df["date"] = pd.to_datetime(df["date"])

x = df.index * X_STRETCH

df["outbound"] = df["outbound"] + DARK_FLEET_ADJUSTMENT
df["inbound"] = df["inbound"] + DARK_FLEET_ADJUSTMENT

# North coast = outbound traffic, south coast = inbound (mirrored, hence the
# minus sign) so the two profiles sit on either side of the y=0 channel axis.
df["north"] = df["outbound"]
df["south"] = -df["inbound"]

# .rolling(window, center=True) averages each day with the days around it
# (not just the days before), so the curve stays aligned with the real dates.
df["north_smooth"] = df["north"].rolling(SMOOTHING_WINDOW_DAYS, center=True).mean()
df["south_smooth"] = df["south"].rolling(SMOOTHING_WINDOW_DAYS, center=True).mean()

# --- Coastline silhouette ---
pl.plot(x, df["north_smooth"], color="black")
pl.plot(x, df["south_smooth"], color="black")

# fill_between(x, curve, 0) fills the water side of each curve down to the
# central channel axis, giving the solid land shape.
pl.fill_between(x, df["north_smooth"], 0, color="black")
pl.fill_between(x, df["south_smooth"], 0, color="black")

# --- Weekly reference markers (Mondays), for alignment once imported in Blender ---
# .dt.dayofweek == 0 selects Mondays (0 = Monday in pandas).
mondays = df[df["date"].dt.dayofweek == 0]
marker_label_y = df["north_smooth"].max() + 5

for idx, row in mondays.iterrows():
    pl.axvline(x=idx * X_STRETCH, color="red", linewidth=0.5)
    pl.text(
        idx * X_STRETCH,
        marker_label_y,
        row["date"].strftime("%Y-%m-%d"),
        rotation=90,
        fontsize=6,
        color="red",
    )

# --- Style: horizontal grid every 10 units, aligned on 0 ---
y_min = math.floor(df["south_smooth"].min() / 10) * 10
y_max = math.ceil(df["north_smooth"].max() / 10) * 10
pl.yticks(range(y_min, y_max + 1, 10))
pl.grid(axis="y", color="red", linewidth=0.5)

pl.gca().set_aspect("equal")

pl.savefig("output/geometry.svg")
pl.show()
