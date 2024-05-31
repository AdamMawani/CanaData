import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with specified encoding
data = pd.read_csv('census.csv')

# Age Group Distribution
plt.figure(figsize=(10, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].between(9, 24)])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Age Group")
plt.ylabel("Population Count")
plt.title("Age Group Distribution")
plt.show()

# Marital Status Distribution
plt.figure(figsize=(8, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].isin([59, 60, 61])])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Marital Status")
plt.ylabel("Population Count")
plt.title("Marital Status Distribution")
plt.show()

# Dwelling Type Distribution
plt.figure(figsize=(10, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].between(42, 49)])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Dwelling Type")
plt.ylabel("Count")
plt.title("Dwelling Type Distribution")
plt.show()

# Pairplot of Canada Census Data
sns.pairplot(data)
plt.suptitle('Pairplot of Canada Census Data', y=1.02)
plt.show()

# Correlation Matrix
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Canada Census Data')
plt.show()

# Age Distribution
plt.figure(figsize=(8, 6))
sns.histplot(data['age'], kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Income Distribution Across Canadian Provinces
plt.figure(figsize=(10, 6))
sns.boxplot(x='province', y='income', data=data)
plt.title('Income Distribution Across Canadian Provinces')
plt.xlabel('Province')
plt.ylabel('Income')
plt.xticks(rotation=45)
plt.show()

# Gender Distribution
plt.figure(figsize=(8, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].isin([1, 2])])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Gender")
plt.ylabel("Population Count")
plt.title("Gender Distribution")
plt.show()

# Employment Status Distribution
plt.figure(figsize=(10, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].between(25, 30)])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Employment Status")
plt.ylabel("Population Count")
plt.title("Employment Status Distribution")
plt.show()

# Education Level Distribution
plt.figure(figsize=(10, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].between(31, 36)])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Education Level")
plt.ylabel("Population Count")
plt.title("Education Level Distribution")
plt.show()

# Scatter Plot of Age vs Income
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='income', data=data)
plt.title('Age vs Income')
plt.xlabel('Age')
plt.ylabel('Income')
plt.show()

# Line Plot of Population Growth Over Years
# Ensure that 'year' is a column in your dataset
if 'year' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='year', y='C1_COUNT_TOTAL', data=data)
    plt.title('Population Growth Over Years')
    plt.xlabel('Year')
    plt.ylabel('Total Population Count')
    plt.show()

# Box Plot of Age Distribution by Gender
# Ensure that 'gender' is a column in your dataset
if 'gender' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='gender', y='age', data=data)
    plt.title('Age Distribution by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Age')
    plt.show()

# Heatmap of Categorical Features
# Replace 'another_categorical_column' with actual column name
if 'another_categorical_column' in data.columns:
    categorical_columns = ['CHARACTERISTIC_NAME', 'another_categorical_column']
    pivot_table = data.pivot_table(index=categorical_columns[0], columns=categorical_columns[1], values='C1_COUNT_TOTAL', aggfunc='sum', fill_value=0)
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt='d')
    plt.title('Heatmap of Categorical Features')
    plt.xlabel(categorical_columns[1])
    plt.ylabel(categorical_columns[0])
    plt.show()

# Violin Plot of Income Distribution by Province
plt.figure(figsize=(10, 6))
sns.violinplot(x='province', y='income', data=data)
plt.title('Income Distribution by Province')
plt.xlabel('Province')
plt.ylabel('Income')
plt.xticks(rotation=45)
plt.show()