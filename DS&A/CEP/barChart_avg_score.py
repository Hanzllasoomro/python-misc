import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
# Optional: normalize column names for convenience
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

avg_by_gender = (
    df.groupby("gender")[["math_score", "reading_score", "writing_score"]]
      .mean()
      .round(2)
)
avg_by_gender.plot(kind="bar")     # 1 chart, no explicit colors per your rubric
plt.title("Average Scores by Gender")
plt.ylabel("Average Score")
plt.xlabel("Gender")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("avg_scores_by_gender_bar.png", dpi=150)
plt.show()
