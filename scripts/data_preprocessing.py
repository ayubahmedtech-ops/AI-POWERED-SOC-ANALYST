import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\haris\UEBA_Project\data\ueba_synthetic_dataset.csv")

print("Original Shape:", df.shape)


# 1️⃣ Check Missing Values
print("\nMissing Values:\n", df.isnull().sum())


# 2️⃣ Check Data Types
print("\nData Types:\n", df.dtypes)


# 3️⃣ Remove Duplicates
df = df.drop_duplicates()

print("\nShape After Removing Duplicates:", df.shape)


# 4️⃣ Separate Features & Target

X = df.drop("anomaly_label", axis=1)  # Features
y = df["anomaly_label"]               # Target

print("\nFeature Shape:", X.shape)
print("Target Shape:", y.shape)