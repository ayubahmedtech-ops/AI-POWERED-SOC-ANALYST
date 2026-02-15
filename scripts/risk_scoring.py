import pandas as pd

# Load predicted dataset
df = pd.read_csv(r"C:\Users\haris\UEBA_Project\data\ueba_exact_attributes_low_anomaly.csv")

# Risk scoring function
def calculate_risk(row):

    score = 0

    # Failed logins risk
    if row["failed_logins"] > 3:
        score += 20

    # High data download
    if row["data_download_mb"] > 1000:
        score += 25

    # Many files accessed
    if row["files_accessed"] > 200:
        score += 20

    # USB usage
    if row["usb_usage"] == 1:
        score += 15

    # Risky login location
    if row["login_location_risk"] == 1:
        score += 20

    return score


# Apply risk scoring
df["risk_score"] = df.apply(calculate_risk, axis=1)

# Risk level classification
def risk_level(score):

    if score >= 70:
        return "High"

    elif score >= 40:
        return "Medium"

    else:
        return "Low"


df["risk_level"] = df["risk_score"].apply(risk_level)

# Save output
df.to_csv(r"C:\Users\haris\UEBA_Project\data\ueba_risk_scored_output.csv", index=False)

# Show sample
print(df[[
    "user_id",
    "predicted_anomaly",
    "risk_score",
    "risk_level"
]].head())