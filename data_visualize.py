import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('coffee_survey.csv')

# Display the first few rows to understand the structure of the data
print(data.head())

# Data Cleaning

# Drop columns with more than 20% missing values
null_values = data.isnull().sum()
null_percent = (null_values / data.shape[0]) * 100
drop_columns = null_percent[null_percent > 20].index
data_cleaned = data.drop(columns=drop_columns)

# Convert relevant columns to numeric or categorical as needed
data_cleaned['age_category'] = data_cleaned['age'].astype('category').cat.codes
data_cleaned['coffee_bitterness'] = pd.to_numeric(data_cleaned['coffee_a_bitterness'], errors='coerce')

# Visualization 1: Age vs. Coffee Bitterness Preference
plt.figure(figsize=(10, 6))
sns.barplot(x='age_category', y='coffee_bitterness', data=data_cleaned, ci=None)
plt.title('Average Coffee Bitterness Preference by Age Group')
plt.xlabel('Age Category')
plt.ylabel('Average Bitterness')
plt.show()

# Visualization 2: Coffee Brewing Methods
plt.figure(figsize=(10, 6))
brewing_methods = ['brew_pourover', 'brew_espresso', 'brew_frenchpress']
for method in brewing_methods:
    sns.histplot(data_cleaned[method], label=method, kde=False)
plt.title('Coffee Brewing Methods Preferences')
plt.xlabel('Brewing Method')
plt.ylabel('Count')
plt.legend(title='Brewing Methods')
plt.show()

# Visualization 3: Relationship Status vs. Roast Preference
plt.figure(figsize=(10, 6))
sns.countplot(x='relationship_status', hue='preferred_roast', data=data_cleaned)
plt.title('Roast Preference by Relationship Status')
plt.xlabel('Relationship Status')
plt.ylabel('Count')
plt.show()

# Visualization 4: Income vs. Preferred Roast
plt.figure(figsize=(10, 6))
sns.boxplot(x='annual_income', y='preferred_roast', data=data_cleaned)
plt.title('Income vs. Preferred Roast Level')
plt.xlabel('Annual Income')
plt.ylabel('Preferred Roast')
plt.show()

# Visualization 5: Political Affiliation vs. Roast Preference
plt.figure(figsize=(10, 6))
sns.countplot(x='political_affiliation', hue='preferred_roast', data=data_cleaned)
plt.title('Political Affiliation vs. Roast Preference')
plt.xlabel('Political Affiliation')
plt.ylabel('Count')
plt.show()

# Visualization 6: Ethnicity vs. Coffee Preferences
plt.figure(figsize=(10, 6))
sns.countplot(x='ethnicity', hue='preferred_roast', data=data_cleaned)
plt.title('Ethnicity vs. Coffee Preferences')
plt.xlabel('Ethnicity')
plt.ylabel('Count')
plt.show()

# Visualization 7: Relationship Status vs. Roast Preference by Age
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age_category', y='preferred_roast', hue='relationship_status', data=data_cleaned)
plt.title('Relationship Status vs. Roast Preference by Age')
plt.xlabel('Age Category')
plt.ylabel('Preferred Roast')
plt.show()

