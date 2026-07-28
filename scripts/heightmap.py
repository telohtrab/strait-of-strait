import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

DARK_FLEET_ADJUSTMENT = 5
SMOOTHING_WINDOW_DAYS = 7
X_STRETCH = 2 

df = pd.read_csv("./data/transits.csv")

df["outbound"] = df["outbound"] + DARK_FLEET_ADJUSTMENT
df["inbound"] = df["inbound"] + DARK_FLEET_ADJUSTMENT

df["north"] = df["outbound"].rolling(SMOOTHING_WINDOW_DAYS, center=True, min_periods= 1).mean()
df["south"] = -df["inbound"].rolling(SMOOTHING_WINDOW_DAYS, center=True, min_periods= 1).mean()

print(df["north"].head())
print(df["south"].head())

x = df.index.to_numpy() * X_STRETCH

n_cols = 3000 # Horizontal resolution
n_rows = 1500 # Vertical resolution

x_days = df.index.to_numpy() * X_STRETCH
x_fine = np.linspace(x_days.min(), x_days.max(), n_cols)

north_fine = np.interp(x_fine, x_days, df["north"].to_numpy())
south_fine = np.interp(x_fine, x_days, df["south"].to_numpy())

# North/south margin computed so the heightmap is roughly square (same span
# in Y as in X), instead of a fixed +/-20 margin.
x_span = x_fine.max() - x_fine.min()
data_y_span = df["north"].max() - df["south"].min()
margin = (x_span - data_y_span) / 2

y_min = df["south"].min() - margin
y_max = df["north"].max() + margin
y = np.linspace(y_min, y_max, n_rows)

X, Y = np.meshgrid(x_fine, y)

distance_to_land_north = Y - north_fine
distance_to_land_south = south_fine -Y

d = np.maximum(distance_to_land_north, distance_to_land_south)

# Noise smoothed along the coastline: locally controls gentle (beach) vs abrupt (cliff) slope
np.random.seed(0)
noise_1d = np.random.normal(0, 1, n_cols)
noise_1d = pd.Series(noise_1d).rolling(250, center=True, min_periods=1).mean().to_numpy()
slope_scale = np.interp(noise_1d, (noise_1d.min(), noise_1d.max()), (4, 20))  # small = cliff, large = beach

# Organic 2D noise (dunes/relief) in several octaves: one large, gentle layer
# (big dunes) plus finer, weaker layers on top, same idea as the Depth setting
# of the A.N.T. Landscape terrain used earlier in Blender.
noise_2d = np.zeros((n_rows, n_cols))
amplitude = 1.0
sigma = 60
for _ in range(5):
    layer = np.random.normal(0, 1, (n_rows, n_cols))
    layer = gaussian_filter(layer, sigma=sigma)
    noise_2d += layer * amplitude
    amplitude *= 0.5
    sigma /= 2
noise_2d = noise_2d / np.abs(noise_2d).max()

NOISE_AMPLITUDE = 20  # organic relief amplitude, far from the shore

# noise_fade is 0 exactly at the shore (d=0) and rises toward 1 further away, so
# the noise never shifts the data's exact zero-crossing while still giving
# organic relief everywhere else.
noise_fade = np.tanh(np.abs(d) / 10)
d_noisy = d + noise_2d * NOISE_AMPLITUDE * noise_fade

# tanh saturates smoothly toward -1/+1 without ever hitting a hard "wall", and d=0 always lands on 0
shaped = np.tanh(d_noisy / slope_scale)

normalized = 0.5 + 0.5 * shaped
plt.imsave("output/heightmap.png", normalized, cmap="gray", origin="lower")

row_at_shore = np.argmin(np.abs(y[:, None] - north_fine[None, :]), axis=0)
values_at_shore = normalized[row_at_shore, np.arange(n_cols)]
print(values_at_shore.min(), values_at_shore.max(), values_at_shore.mean())