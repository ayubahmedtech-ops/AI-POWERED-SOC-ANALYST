import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\haris\UEBA_Project\data\ueba_synthetic_dataset.csv")

# Basic info
print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)

print("\nFirst 5 Rows:\n", df.head())