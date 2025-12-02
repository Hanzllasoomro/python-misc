# ===============================================================
# CLASS TASK: CONFUSION MATRIX for LAB 10 & LAB 11
# ===============================================================

# -------------------------------
# Import required libraries
# -------------------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, classification_report, mean_absolute_error, mean_squared_error, r2_score, accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.datasets import load_iris, load_breast_cancer

# ===============================================================
# LAB 10 - TASK 1: Linear Regression on Student Dataset
# ===============================================================

print("\n========== LAB 10 - TASK 1 (Student Dataset) ==========\n")

# Load dataset
# Example dataset should have columns "Hours" and "Scores"
dataset = pd.read_csv('student_scores.csv')

# Split features and target
X = dataset.iloc[:, :-1].values  # Hours
y = dataset.iloc[:, -1].values   # Scores

# Train/test split
xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=0)

# Train Linear Regression model
model = LinearRegression()
model.fit(xTrain, yTrain)

# Predict
yPred = model.predict(xTest)

# Evaluate Regression performance
print("Mean Absolute Error:", mean_absolute_error(yTest, yPred))
print("Mean Squared Error:", mean_squared_error(yTest, yPred))
print("R² Score:", r2_score(yTest, yPred))

# -------------------------------
# Convert Regression Output to Classification (Pass/Fail)
# -------------------------------
# Define threshold (50 marks as passing)
yTest_class = np.where(yTest >= 50, 1, 0)
yPred_class = np.where(yPred >= 50, 1, 0)

# Compute Confusion Matrix
cm_lab10_task1 = confusion_matrix(yTest_class, yPred_class)
print("\nConfusion Matrix (Lab 10 - Task 1):\n", cm_lab10_task1)
print("\nClassification Report (Lab 10 - Task 1):\n", classification_report(yTest_class, yPred_class))

# ===============================================================
# LAB 10 - TASK 2: Linear Regression on Custom Dataset (Car Prices)
# ===============================================================

print("\n========== LAB 10 - TASK 2 (Car Price Dataset) ==========\n")

# Load custom dataset (e.g., 'cars.csv' with columns 'EngineSize' and 'Price')
dataset2 = pd.read_csv('cars.csv')

X2 = dataset2[['EngineSize']].values
y2 = dataset2['Price'].values

xTrain2, xTest2, yTrain2, yTest2 = train_test_split(X2, y2, test_size=0.25, random_state=42)

model2 = LinearRegression()
model2.fit(xTrain2, yTrain2)
yPred2 = model2.predict(xTest2)

# Regression evaluation
print("Mean Absolute Error:", mean_absolute_error(yTest2, yPred2))
print("Mean Squared Error:", mean_squared_error(yTest2, yPred2))
print("R² Score:", r2_score(yTest2, yPred2))

# -------------------------------
# Convert Regression Output to Classification (Expensive/Affordable)
# -------------------------------
threshold_price = np.mean(y2)  # mean price as threshold
yTest2_class = np.where(yTest2 >= threshold_price, 1, 0)
yPred2_class = np.where(yPred2 >= threshold_price, 1, 0)

# Confusion Matrix
cm_lab10_task2 = confusion_matrix(yTest2_class, yPred2_class)
print("\nConfusion Matrix (Lab 10 - Task 2):\n", cm_lab10_task2)
print("\nClassification Report (Lab 10 - Task 2):\n", classification_report(yTest2_class, yPred2_class))

# ===============================================================
# LAB 11: Naïve Bayes and SVM on Two Datasets (Iris & Breast Cancer)
# ===============================================================

print("\n========== LAB 11 (Classification Tasks) ==========\n")

# -------------------------------
# Dataset 1: IRIS
# -------------------------------
iris = load_iris()
X_iris = iris.data
y_iris = iris.target
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.2, random_state=0)

# Naive Bayes
nb_model_iris = GaussianNB()
nb_model_iris.fit(X_train_iris, y_train_iris)
nb_pred_iris = nb_model_iris.predict(X_test_iris)

# SVM
svm_model_iris = SVC(kernel='linear')
svm_model_iris.fit(X_train_iris, y_train_iris)
svm_pred_iris = svm_model_iris.predict(X_test_iris)

# Confusion Matrices
cm_nb_iris = confusion_matrix(y_test_iris, nb_pred_iris)
cm_svm_iris = confusion_matrix(y_test_iris, svm_pred_iris)

print("Iris Dataset - Naïve Bayes Confusion Matrix:\n", cm_nb_iris)
print("Iris Dataset - SVM Confusion Matrix:\n", cm_svm_iris)

# -------------------------------
# Dataset 2: BREAST CANCER
# -------------------------------
cancer = load_breast_cancer()
X_cancer = cancer.data
y_cancer = cancer.target
X_train_cancer, X_test_cancer, y_train_cancer, y_test_cancer = train_test_split(X_cancer, y_cancer, test_size=0.2, random_state=0)

# Naive Bayes
nb_model_cancer = GaussianNB()
nb_model_cancer.fit(X_train_cancer, y_train_cancer)
nb_pred_cancer = nb_model_cancer.predict(X_test_cancer)

# SVM
svm_model_cancer = SVC(kernel='linear')
svm_model_cancer.fit(X_train_cancer, y_train_cancer)
svm_pred_cancer = svm_model_cancer.predict(X_test_cancer)

# Confusion Matrices
cm_nb_cancer = confusion_matrix(y_test_cancer, nb_pred_cancer)
cm_svm_cancer = confusion_matrix(y_test_cancer, svm_pred_cancer)

print("\nBreast Cancer Dataset - Naïve Bayes Confusion Matrix:\n", cm_nb_cancer)
print("Breast Cancer Dataset - SVM Confusion Matrix:\n", cm_svm_cancer)

# -------------------------------
# Comparison Summary Table
# -------------------------------
results = pd.DataFrame({
    'Dataset': ['Student Scores', 'Car Prices', 'Iris (NB)', 'Iris (SVM)', 'Breast Cancer (NB)', 'Breast Cancer (SVM)'],
    'Model': ['LinearReg (classed)', 'LinearReg (classed)', 'Naïve Bayes', 'SVM', 'Naïve Bayes', 'SVM'],
    'Accuracy': [
        accuracy_score(yTest_class, yPred_class),
        accuracy_score(yTest2_class, yPred2_class),
        accuracy_score(y_test_iris, nb_pred_iris),
        accuracy_score(y_test_iris, svm_pred_iris),
        accuracy_score(y_test_cancer, nb_pred_cancer),
        accuracy_score(y_test_cancer, svm_pred_cancer)
    ]
})

print("\n========== COMPARISON SUMMARY ==========\n")
print(results)
