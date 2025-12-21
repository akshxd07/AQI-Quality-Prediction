import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Step 1: Load the dataset
data = pd.read_csv("dataset.csv")

# Step 2: Clean the data (force numeric and drop bad values)
data = data.apply(pd.to_numeric, errors='coerce')
data = data.dropna()

# Step 3: Check if dataset is clean
print("\n✅ Clean dataset:")
print(data)

# Step 4: Separate features and target
X = data[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'O3', 'Temp', 'Humidity']]
y = data['AQI']

# Step 5: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("\n✅ Model trained successfully!")
print("Mean Squared Error:", mse)
print("R² Score:", r2)

# Step 8: Save the model
joblib.dump(model, "aqi_model.pkl")
print("\n💾 Model saved successfully as 'aqi_model.pkl'")

