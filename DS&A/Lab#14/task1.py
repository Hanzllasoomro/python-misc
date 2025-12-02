# ---- Import Libraries ----
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler

# ---- Load Dataset ----
data = pd.read_csv("student_dataset.csv")

# ---- Split Features and Target ----
X = data[['Hours_Studied', 'Attendance']]
y = data['Pass_Fail']

# ---- Standardize Data ----
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ---- Define SVM Model ----
svm_model = SVC(kernel='linear', random_state=42)

# ---- Perform Cross Validation ----
scores = cross_val_score(svm_model, X_scaled, y, cv=5)

print("Cross Validation Scores:", scores)
print("Mean Accuracy:", np.mean(scores))
