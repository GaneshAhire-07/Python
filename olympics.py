import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
plt.ion()

# Load the dataset into a Pandas DataFrame
df = pd.read_csv('olympics.csv')

# Display the first few rows to understand the structure
print(df.head())
print(df.columns)
df = pd.read_csv('olympics.csv', header=0)
print(df.head())

# Calculate the number of unique countries
total_countries = df['team'].nunique()
print(f'Total number of countries: {total_countries}')

# Filter the dataset for India and count the number of each type of medal
india_medals = df[df['team'] == 'India'].groupby('medal').size()
print('India medal count:')
print(india_medals)

# Plot boxplot for ages of all athletes
plt.figure(figsize=(10, 5))
sns.boxplot(x=df['age'])
plt.title('Boxplot of Ages of All Athletes')
plt.xlabel('age')
plt.show()
plt.savefig('plot.png')

# Plot boxplot for ages of Indian athletes
plt.figure(figsize=(10, 5))
sns.boxplot(x=df[df['team'] == 'India']['age'])
plt.title('Boxplot of Ages of Indian Athletes')
plt.xlabel('age')
plt.show()
plt.savefig('plot1.png')

# Median and mean ages of male athletes
median_age_male = df[df['sex'] == 'M']['age'].median()
mean_age_male = df[df['sex'] == 'M']['age'].mean()
print(f'Median age of male athletes: {median_age_male}')
print(f'Mean age of male athletes: {mean_age_male}')

# Median and mean ages of female athletes
median_age_female = df[df['sex'] == 'M']['age'].median()
mean_age_female = df[df['sex'] == 'F']['age'].mean()
print(f'Median age of female athletes: {median_age_female}')
print(f'Mean age of female athletes: {mean_age_female}')

# Group by 'Year' and 'Gender' and calculate the number of athletes in each group
olympic_gender_counts = df.groupby(['year', 'sex']).size().unstack(fill_value=0)

# Calculate the male to female ratio
olympic_gender_counts['Male_to_Female_Ratio'] = olympic_gender_counts['M'] / olympic_gender_counts['F']

# Plot the male to female ratio for each Olympic
plt.figure(figsize=(12, 6))
olympic_gender_counts['Male_to_Female_Ratio'].plot(kind='bar')
plt.title('Male to Female Athlete Ratio by Olympics Year')
plt.xlabel('Olympics Year')
plt.ylabel('Male:Female Ratio')
plt.show()
plt.savefig('plot2.png')
