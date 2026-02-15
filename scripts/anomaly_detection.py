import pandas as pd
import matplotlib.pyplot as plt

# Load predicted dataset
df = pd.read_csv(r"C:\Users\haris\UEBA_Project\data\ueba_exact_attributes_low_anomaly.csv")

# Count anomalies vs normal
counts = df["predicted_anomaly"].value_counts()

# Bar graph
plt.figure(figsize=(8,5))

plt.bar(
    counts.index.astype(str),
    counts.values
)

plt.title("UEBA Anomaly Detection Summary")
plt.xlabel("User Behaviour Type")
plt.ylabel("Number of Users")

plt.show()