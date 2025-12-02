import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Step 1: Load and clean the dataset
df = pd.read_csv("StudentsPerformance.csv")

# Normalize column names: replace spaces with underscores
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# Step 2: Create average score and result columns
df["avg_score"] = df[["math_score", "reading_score", "writing_score"]].mean(axis=1)
df["result"] = (df["avg_score"] >= 50).map({True: "Pass", False: "Fail"})

# Step 3: Prepare data
X = df[["math_score", "reading_score", "writing_score"]].values
y = df["result"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Step 4: Scale features and train SVM
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s  = scaler.transform(X_test)

svm = SVC(kernel="rbf", random_state=42)
svm.fit(X_train_s, y_train)

# Step 5: Evaluate model
y_pred = svm.predict(X_test_s)
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred, labels=["Pass", "Fail"])

print(f"Accuracy: {acc:.4f}")
print("\nConfusion Matrix (labels: Pass, Fail):\n", cm)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 6: Visualization 1 — Confusion Matrix Heatmap
plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Pass", "Fail"],
            yticklabels=["Pass", "Fail"])
plt.title("SVM Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("svm_confusion_matrix.png", dpi=150)
plt.show()

# Step 7: Visualization 2 — Scatter plot of predicted results
plt.figure(figsize=(6,5))
plt.scatter(df["math_score"], df["avg_score"],
            c=(df["result"] == "Pass"), cmap="coolwarm", s=30)
plt.title("Pass/Fail Distribution by Math & Average Scores")
plt.xlabel("Math Score")
plt.ylabel("Average Score")
plt.axhline(50, color="black", linestyle="--", linewidth=1)
plt.colorbar(label="Pass (1) / Fail (0)")
plt.tight_layout()
plt.savefig("svm_result_scatter.png", dpi=150)
plt.show()
