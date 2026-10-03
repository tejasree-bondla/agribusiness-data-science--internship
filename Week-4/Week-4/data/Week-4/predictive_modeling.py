import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 1. Load dataset
df = pd.read_csv("data/agribusiness_yield_data.csv")

print("Dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())


# 2. Prepare data
# Convert categorical columns into numerical columns
df_encoded = pd.get_dummies(
    df,
    columns=["State", "District", "Crop", "Season"],
    drop_first=True
)

# Remove rows with missing values
df_encoded = df_encoded.dropna()


# 3. Separate features and target
X = df_encoded.drop("Yield", axis=1)
y = df_encoded["Yield"]


# 4. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# 5. Train Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# 6. Make predictions
y_pred = model.predict(X_test)


# 7. Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("R2 Score:", r2)


# 8. Actual vs Predicted Yield
plt.figure(figsize=(8, 5))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Actual vs Predicted Crop Yield")

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)

plt.tight_layout()
plt.show()


# 9. Feature importance
importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nTop Important Features:")
print(importance.head(10))

plt.figure(figsize=(10, 6))

importance.head(10).sort_values().plot(kind="barh")

plt.xlabel("Importance")
plt.ylabel("Features")
plt.title("Top 10 Feature Importances")

plt.tight_layout()
plt.show()
