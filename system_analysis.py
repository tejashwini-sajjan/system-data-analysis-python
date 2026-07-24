import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("anomaly_label.csv")

print(df.head())

print("\nTotal Records:", len(df))

print("\nLabel Count:")
print(df["Label"].value_counts())

anomaly_count = (df["Label"] == "Anomaly").sum()

total_records = len(df)

anomaly_rate = (anomaly_count / total_records) * 100

print("\nAnomaly Count:", anomaly_count)

print("Anomaly Rate:", round(anomaly_rate, 2), "%")

# Bar Chart
df["Label"].value_counts().plot(
    kind="bar",
    color=["green", "red"]
)

plt.title("Normal vs Anomaly Events")
plt.xlabel("Event Type")
plt.ylabel("Count")

plt.savefig("anomaly_bar_chart.png")

plt.show()

# Pie Chart
df["Label"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Anomaly Distribution")
plt.ylabel("")

plt.savefig("anomaly_pie_chart.png")

plt.show()