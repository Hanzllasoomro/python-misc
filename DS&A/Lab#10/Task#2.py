# Task 2: Linear Regression on Custom Dataset (Car Price Prediction)

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load your dataset (e.g., cars.csv)
# Example columns: 'EngineSize', 'Price'
dataset = pd.read_csv('cars.csv')

# Prepare variables
X = dataset[['EngineSize']].values
y = dataset['Price'].values

# Split dataset
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.25, random_state=42)

# Train model
model = LinearRegression()
model.fit(xTrain, yTrain)

# Predict on test set
yPred = model.predict(xTest)

# Show comparison
results = pd.DataFrame({'EngineSize': xTest.flatten(), 'Actual Price': yTest, 'Predicted Price': yPred})
print(results)

# Visualize
plt.scatter(xTrain, yTrain, color='red')
plt.plot(xTrain, model.predict(xTrain), color='blue')
plt.title('Engine Size vs Car Price (Training Set)')
plt.xlabel('Engine Size')
plt.ylabel('Price')
plt.show()

plt.scatter(xTest, yTest, color='green')
plt.plot(xTrain, model.predict(xTrain), color='blue')
plt.title('Engine Size vs Car Price (Test Set)')
plt.xlabel('Engine Size')
plt.ylabel('Price')
plt.show()

# Evaluate performance
print("Mean Absolute Error:", mean_absolute_error(yTest, yPred))
print("Mean Squared Error:", mean_squared_error(yTest, yPred))
print("R² Score:", r2_score(yTest, yPred))
