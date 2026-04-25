import pandas as pd

# 1. Load CSV dataset
df = pd.read_csv('data.csv')

# 2. Inspect the dataset
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

# 3. Data Cleaning

# Handle missing values
df_cleaned = df.dropna()

# Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()

print("\nAfter Cleaning:")
print(df_cleaned.info())

# 4. Filtering (Example: filter rows where a column value > some value)
# Replace 'column_name' with actual column
if 'column_name' in df_cleaned.columns:
    filtered_data = df_cleaned[df_cleaned['column_name'] > df_cleaned['column_name'].mean()]
    print("\nFiltered Data:")
    print(filtered_data.head())
else:
    print("\nSkipping filtering (column not found)")

# 5. Grouping and Aggregation
# Replace 'category_column' and 'value_column' with actual names
if 'category_column' in df_cleaned.columns and 'value_column' in df_cleaned.columns:
    grouped = df_cleaned.groupby('category_column')['value_column'].mean()
    print("\nGrouped Data (Average values):")
    print(grouped)
else:
    print("\nSkipping grouping (columns not found)")

# 6. Save cleaned dataset
df_cleaned.to_csv('cleaned_data.csv', index=False)

print("\nCleaned data saved as 'cleaned_data.csv'")