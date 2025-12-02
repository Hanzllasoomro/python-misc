import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
# Optional: normalize column names for convenience
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

avg_by_gender = (
    df.groupby("gender")[["math_score", "reading_score", "writing_score"]]
      .mean()
      .round(2)
)
print(avg_by_gender)
avg_by_gender.to_csv("avg_scores_by_gender.csv", index=True)
