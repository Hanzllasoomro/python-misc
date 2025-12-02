# Import required libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_csv("house_prices.csv")

# Split features and target
X = data[["Size (sqft)", "Rooms"]]
y = data["Price (in $1000)"]

# Initialize regression model
regressor = LinearRegression()

# Define 5-Fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Evaluate using cross_val_score
scores = cross_val_score(regressor, X, y, cv=kf, scoring='r2')

print("R² Scores for each fold:", scores)
print("Mean R² Score:", np.mean(scores))
print("Standard Deviation:", np.std(scores))
