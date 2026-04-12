import pandas as pd

# -----------------------------
# LOAD DATA (FIXED VERSION)
# -----------------------------
df = pd.read_csv("bank.csv")   # ❗ removed sep=";"

# -----------------------------
# CHECK DATA
# -----------------------------
print("First 5 rows:")
print(df.head())

print("\nData info:")
print(df.info())

print("\nColumn names:")
print(df.columns)

# -----------------------------
# CHECK MISSING VALUES
# -----------------------------
print("\nMissing values per column:")
print(df.isnull().sum())

# -----------------------------
# CHECK DUPLICATES
# -----------------------------
duplicates = df.duplicated().sum()
print("\nNumber of duplicate rows:", duplicates)

# remove duplicates
df = df.drop_duplicates()

# -----------------------------
# CLEAN COLUMN NAMES
# -----------------------------
df.columns = df.columns.str.lower().str.strip()

# -----------------------------
# CLEAN TEXT VALUES
# -----------------------------
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# -----------------------------
# CHECK UNIQUE VALUES
# -----------------------------
for col in df.select_dtypes(include="object").columns:
    print(f"\nUnique values in {col}:")
    print(df[col].unique())

# -----------------------------
# CREATE AGE GROUP COLUMN
# -----------------------------
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 29, 49, 100],
    labels=["18-29", "30-49", "50+"]
)

# -----------------------------
# CREATE NUMERIC TARGET COLUMN
# -----------------------------
df["subscribed"] = df["deposit"].map({"yes": 1, "no": 0})

# -----------------------------
# FINAL CHECK
# -----------------------------
print("\nCleaned data preview:")
print(df.head())

# -----------------------------
# SAVE CLEAN DATA
# -----------------------------
df.to_csv("clean_bank_data.csv", index=False)

print("\n✅ Clean data saved as clean_bank_data.csv")