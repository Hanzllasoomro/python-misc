# Task 5: Regression Analysis
# --------------------------------------
# 5a) Apply Linear Regression to predict the writing score based on the reading score.
# 5b) Plot the regression line using Matplotlib.
# 5c) Calculate R² Score to evaluate performance.
# 5d) Interpret the R² value.
# --------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# 5a) Linear Regression model
X = df[['reading score']].values     # independent variable
y = df['writing score'].values       # dependent variable

model = LinearRegression()
model.fit(X, y)

# 5c) Calculate R² Score
r2 = model.score(X, y)
print(f"R² Score (Writing ~ Reading): {r2:.4f}")

# 5b) Plot regression line
x_line = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
y_line = model.predict(x_line)

plt.figure()
plt.scatter(X, y, alpha=0.6, label="Actual data")
plt.plot(x_line, y_line, color='red', label="Regression line")
plt.title("Linear Regression: Writing vs Reading")
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.legend()
plt.tight_layout()
plt.savefig("task5_regression.png")  # Save the plot
plt.show()

# 5d) Interpretation
if r2 >= 0.9:
    interpretation = "Very strong linear relationship."
elif r2 >= 0.7:
    interpretation = "Strong linear relationship."
elif r2 >= 0.5:
    interpretation = "Moderate linear relationship."
else:
    interpretation = "Weak linear relationship."

print(f"Interpretation: The R² value of {r2:.4f} indicates a {interpretation}")
