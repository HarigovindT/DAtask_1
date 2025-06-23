import pandas as pd
df = pd.read_csv(r"C:\Users\harig\Desktop\Mall_Customers.csv")
print("Before Cleaning:\n", df.info())
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicate Rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
for col in df.select_dtypes(include='number'):
    df[col].fillna(df[col].mean(), inplace=True)
for col in df.select_dtypes(include='object'):
    df[col].fillna(df[col].mode()[0], inplace=True)
for col in df.select_dtypes(include='object'):
    df[col] = df[col].str.lower().str.strip()
if 'gender' in df.columns:
    df['gender'] = df['gender'].replace({
        'female': 'f', 'f': 'f',
        'male': 'm', 'm': 'm',
        'other': 'o'
    })
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')
for col in df.columns:
    if 'date' in col or 'dob' in col:
        try:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        except:
            pass
if 'age' in df.columns:
    df['age'] = df['age'].fillna(df['age'].mean())
    df['age'] = df['age'].astype(int)
df.to_csv("cleaned_dataset.csv", index=False)
print("\nCleaned dataset saved as cleaned_dataset.csv")
summary = f"""
Summary of Cleaning Steps:
1. Removed duplicate rows.
2. Filled missing numeric values with column mean.
3. Filled missing string values with column mode.
4. Standardized text columns (lowercase, stripped spaces).
5. Normalized 'gender' column values to 'f', 'm', 'o' (if present).
6. Renamed column headers (lowercase + underscores).
7. Converted date-related columns to datetime format.
8. Converted 'age' column to integer (if present).
"""
with open("summary.txt", "w") as f:
    f.write(summary)
print("Summary written to summary.txt")


