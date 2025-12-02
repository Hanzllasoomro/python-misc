# Task 1: Linear Regression on Student Dataset

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset (e.g., student_scores.csv)
# The dataset should contain columns like: "Hours" and "Scores"
dataset = pd.read_csv('student_scores.csv')

# Split the data into features (X) and target (y)
X = dataset.iloc[:, :-1].values  # Independent variable (Hours)
y = dataset.iloc[:, -1].values   # Dependent variable (Scores)

# Split dataset into training and testing sets (80/20)
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the model
model = LinearRegression()
model.fit(xTrain, yTrain)

# Make predictions
yPred = model.predict(xTest)

# Compare actual vs predicted
results = pd.DataFrame({'Hours': xTest.flatten(), 'Actual Scores': yTest, 'Predicted Scores': yPred})
print(results)

# Visualize training results
plt.scatter(xTrain, yTrain, color='red')
plt.plot(xTrain, model.predict(xTrain), color='blue')
plt.title('Hours vs Scores (Training set)')
plt.xlabel('Hours Studied')
plt.ylabel('Scores Obtained')
plt.show()

# Visualize test results
plt.scatter(xTest, yTest, color='red')
plt.plot(xTrain, model.predict(xTrain), color='blue')
plt.title('Hours vs Scores (Test set)')
plt.xlabel('Hours Studied')
plt.ylabel('Scores Obtained')
plt.show()

# Model performance
print("Mean Absolute Error:", mean_absolute_error(yTest, yPred))
print("Mean Squared Error:", mean_squared_error(yTest, yPred))
print("R² Score:", r2_score(yTest, yPred))
