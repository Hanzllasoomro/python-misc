import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.datasets import load_iris, load_breast_cancer


iris = load_iris()
X_iris = iris.data
y_iris = iris.target


X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.2, random_state=0)


nb_model_iris = GaussianNB()
nb_model_iris.fit(X_train_iris, y_train_iris)
nb_pred_iris = nb_model_iris.predict(X_test_iris)


svm_model_iris = SVC(kernel='linear')
svm_model_iris.fit(X_train_iris, y_train_iris)
svm_pred_iris = svm_model_iris.predict(X_test_iris)

print("========== IRIS DATASET ==========\n")
print("Naïve Bayes Classification Report:\n", metrics.classification_report(y_test_iris, nb_pred_iris))
print("Naïve Bayes Confusion Matrix:\n", metrics.confusion_matrix(y_test_iris, nb_pred_iris))
print("SVM Classification Report:\n", metrics.classification_report(y_test_iris, svm_pred_iris))
print("SVM Confusion Matrix:\n", metrics.confusion_matrix(y_test_iris, svm_pred_iris))

cancer = load_breast_cancer()
X_cancer = cancer.data
y_cancer = cancer.target

X_train_cancer, X_test_cancer, y_train_cancer, y_test_cancer = train_test_split(X_cancer, y_cancer, test_size=0.2, random_state=0)

nb_model_cancer = GaussianNB()
nb_model_cancer.fit(X_train_cancer, y_train_cancer)
nb_pred_cancer = nb_model_cancer.predict(X_test_cancer)

svm_model_cancer = SVC(kernel='linear')
svm_model_cancer.fit(X_train_cancer, y_train_cancer)
svm_pred_cancer = svm_model_cancer.predict(X_test_cancer)

print("\n========== BREAST CANCER DATASET ==========\n")
print("Naïve Bayes Classification Report:\n", metrics.classification_report(y_test_cancer, nb_pred_cancer))
print("Naïve Bayes Confusion Matrix:\n", metrics.confusion_matrix(y_test_cancer, nb_pred_cancer))
print("SVM Classification Report:\n", metrics.classification_report(y_test_cancer, svm_pred_cancer))
print("SVM Confusion Matrix:\n", metrics.confusion_matrix(y_test_cancer, svm_pred_cancer))

results = pd.DataFrame({
    'Dataset': ['Iris', 'Iris', 'Breast Cancer', 'Breast Cancer'],
    'Model': ['Naïve Bayes', 'SVM', 'Naïve Bayes', 'SVM'],
    'Accuracy': [
        metrics.accuracy_score(y_test_iris, nb_pred_iris),
        metrics.accuracy_score(y_test_iris, svm_pred_iris),
        metrics.accuracy_score(y_test_cancer, nb_pred_cancer),
        metrics.accuracy_score(y_test_cancer, svm_pred_cancer)
    ]
})

print("\n========== COMPARISON SUMMARY ==========\n")
print(results)
