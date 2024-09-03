import pandas as pd

# Load the dataset
data = pd.read_csv('coffee_survey.csv')

# Display the first 10 rows of the dataset
print("10 rows of the dataset:")
print(data.head(10))

# Get the total number of rows and columns
num_rows, num_columns = data.shape
print(f"\nTotal number of rows: {num_rows}")
print(f"Total number of columns: {num_columns}")

# Display data types of each column
print("\nData types of each column:")
print(data.dtypes)

# Find and display missing values for each column
print("\nMissing values for each column:")
null_values = data.isnull().sum()
null_values = null_values[null_values > 0]
print(null_values)

# Calculate percentage of missing values and identify columns to drop
null_percent = (null_values / num_rows) * 100
drop_columns = null_percent[null_percent > 20].index

print("\nColumns with more than 20% missing values:")
print(drop_columns.tolist())

# Drop columns with more than 20% missing values
data_cleaned = data.drop(columns=drop_columns)

# Display statistics for numerical columns
print("\nStatistics for numerical columns:")
numerical_stats = data_cleaned.describe(include=[float, int])
print(numerical_stats)

# Display mode for numerical columns
print("\nMode for numerical columns:")
numerical_mode = data_cleaned.mode().iloc[0]
print(numerical_mode)

# Convert 'age' to categorical and numeric codes
data_cleaned['age_category'] = data_cleaned['age'].astype('category').cat.codes

# Convert 'coffee_a_bitterness' to numeric, handling errors
data_cleaned['coffee_bitterness'] = pd.to_numeric(data_cleaned['coffee_a_bitterness'], errors='coerce')

# Calculate and display average coffee bitterness preference by age group
average_bitterness_by_age = data_cleaned.groupby('age_category')['coffee_bitterness'].mean()
print("\nAverage coffee bitterness preference by age group:")
print(average_bitterness_by_age)
