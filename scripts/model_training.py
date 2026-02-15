import pandas as pd
from sklearn.ensemble import IsolationForest


# Load dataset
df = pd.read_csv(r"C:\Users\haris\UEBA_Project\data\ueba_exact_attributes_low_anomaly.csv")


# Separate features & target
X = df.drop("anomaly_label", axis=1)
y = df["anomaly_label"]


# Train Isolation Forest Model
model = IsolationForest(
    n_estimators=100,     # Number of trees
    contamination=0.05,    # Expected anomaly % (05%)
    random_state=42
)

model.fit(X)


# Predict anomalies
predictions = model.predict(X)


# Convert predictions
# (-1 = anomaly, 1 = normal) → convert to (1 = anomaly, 0 = normal)

predictions = [1 if p == -1 else 0 for p in predictions]


# Add predictions to dataset
df["predicted_anomaly"] = predictions


# Show results
print(df[["anomaly_label", "predicted_anomaly"]].head()) 

print(df["anomaly_label"].value_counts())

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Confusion Matrix
cm = confusion_matrix(
    df["anomaly_label"],
    df["predicted_anomaly"]
)

print("Confusion Matrix:\n", cm)

# Accuracy
acc = accuracy_score(
    df["anomaly_label"],
    df["predicted_anomaly"]
)

print("\nAccuracy:", acc)

# Classification Report
print("\nReport:\n",
      classification_report(
          df["anomaly_label"],
          df["predicted_anomaly"]
      ))
df.to_csv(r"C:\Users\haris\UEBA_Project\data\ueba_exact_attributes_low_anomaly.csv", index=False)