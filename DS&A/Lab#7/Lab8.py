import numpy as np
import pandas as pd
from scipy import linalg
import matplotlib.pyplot as plt

# ---------- Step 1: Generate a synthetic dataset ----------
# Let's simulate a dataset of 100 students with marks in 4 subjects and a categorical grade
np.random.seed(42)
student_ids = np.arange(1, 101)
math = np.random.randint(40, 100, size=100)
science = np.random.randint(35, 95, size=100)
english = np.random.randint(30, 90, size=100)
computer = np.random.randint(45, 100, size=100)
grades = pd.cut((math + science + english + computer)/4,
                bins=[0,50,65,80,100],
                labels=["D","C","B","A"])

df = pd.DataFrame({
    "student_id": student_ids,
    "math": math,
    "science": science,
    "english": english,
    "computer": computer,
    "grade": grades
})


print(df.head(10))

print("Dataset shape:", df.shape)
print("First 5 rows:\n", df.head())

# ---------- Step 2: NumPy array creation ----------
arr = df[["math", "science", "english"]].to_numpy()
print("\nArray shape:", arr.shape)
print("Size:", arr.size)
print("Dtype:", arr.dtype)
print("First row as list:", arr[0].tolist())

# astype conversion
arr_float = arr.astype(float)
print("Converted dtype:", arr_float.dtype)

# ---------- Step 3: Copy, sort, reshape ----------
arr_copy = arr.copy()
arr_sorted = arr_copy[arr_copy[:,0].argsort()] # sort by math score
print("First 5 rows sorted by math:\n", arr_sorted[:5])

reshaped = arr_copy[:2,:3].reshape(1,6)
print("Reshaped (1x6):", reshaped)

# ---------- Step 4: Add/remove columns ----------
df["total"] = df[["math","science","english","computer"]].sum(axis=1)
print("\nAdded total column. Sample:\n", df[["student_id","total"]].head())

df_removed = df.drop(columns=["total"])
print("Removed total column. Columns now:", df_removed.columns.tolist())

# ---------- Step 5: Combine / split ----------
a = df["math"].to_numpy()
b = df["science"].to_numpy()
combined = np.vstack((a,b)).T
print("Combined shape:", combined.shape)
split1, split2 = np.hsplit(combined,2)
print("Split shapes:", split1.shape, split2.shape)

# ---------- Step 6: Indexing / slicing ----------
high_math = df[df["math"] > 80]
print("\nStudents with math > 80:", high_math.shape[0])
print("Grade distribution:\n", high_math["grade"].value_counts())

slice_10_19 = df.iloc[10:20, 1:3]
print("Rows 10-19, math & science:\n", slice_10_19)

# ---------- Step 7: Scalar & vector math ----------
math_plus_5 = df["math"].to_numpy() + 5
print("First 5 math+5:", math_plus_5[:5])

nums = df[["math","science","english","computer"]].to_numpy()
nums_norm = (nums - nums.min(axis=0)) / (nums.max(axis=0)-nums.min(axis=0))
print("Normalized first row:", nums_norm[0])

# ---------- Step 8: Statistics ----------
means = nums.mean(axis=0)
medians = np.median(nums, axis=0)
stds = nums.std(axis=0)
print("Means:", means)
print("Medians:", medians)
print("Stds:", stds)

# ---------- Step 9: SciPy Linear Algebra ----------
A = np.array([[4,2,1],[2,3,1],[1,1,2]], float)
b = np.array([5,6,7], float)
inv_A = linalg.inv(A)
det_A = linalg.det(A)
sol = linalg.solve(A,b)
print("\nMatrix A:\n", A)
print("Inverse:\n", inv_A)
print("Determinant:", det_A)
print("Solution x for A x = b:", sol)

# ---------- Step 10: Matplotlib Visualizations ----------
# Histogram: math scores
plt.figure()
plt.hist(df["math"], bins=10)
plt.title("Histogram: Math scores")
plt.xlabel("Math")
plt.ylabel("Frequency")
plt.show()

# Pie: grade distribution
plt.figure()
grade_counts = df["grade"].value_counts()
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%')
plt.title("Grade distribution")
plt.show()

# Histogram: total marks
plt.figure()
plt.hist(df["total"], bins=10)
plt.title("Histogram: Total marks")
plt.xlabel("Total")
plt.ylabel("Frequency")
plt.show()

# Pie: grade distribution of high_math subset
plt.figure()
high_math_counts = high_math["grade"].value_counts()
plt.pie(high_math_counts, labels=high_math_counts.index, autopct='%1.1f%%')
plt.title("Grades of students with math>80")
plt.show()

print("\nDone — applied all tasks on self-generated dataset with 100 students.")
