import pandas as pd

data = {
    "PM2.5": [35, 59, 90, 110, 100, 150],
    "PM10": [50, 120, 150, 160, 170, 200],
    "NO2": [22, 46, 65, 70, 73, 90],
    "SO2": [12, 23, 30, 35, 51, 40],
    "CO": [6, 9, 11, 16, 6, 29],
    "O3": [42, 37, 35, 33, 33, 37],
    "Temp": [27, 29, 31, 34, 32, 35],
    "Humidity": [75, 60, 72, 68, 70, 75],
    "AQI": [100, 130, 150, 180, 220, 250]
}

df = pd.DataFrame(data)
df.to_csv("dataset.csv", index=False)
print("✅ Clean dataset.csv recreated successfully!")
