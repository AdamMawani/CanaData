import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with specified encoding
data = pd.read_csv('census.csv')

# Utility function for creating bar plots
def plot_bar(data, x, y, title, xlabel, ylabel, rotation=45, ha='right', figsize=(10, 6)):
    plt.figure(figsize=figsize)
    sns.barplot(x=x, y=y, data=data)
    plt.xticks(rotation=rotation, ha=ha)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.show()

# Age Group Distribution
plot_bar(data=data[data["CHARACTERISTIC_ID"].between(9, 24)],
         x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL",
         title="Age Group Distribution",
         xlabel="Age Group", ylabel="Population Count")

# Marital Status Distribution
plot_bar(data=data[data["CHARACTERISTIC_ID"].isin([59, 60, 61])],
         x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL",
         title="Marital Status Distribution",
         xlabel="Marital Status", ylabel="Population Count", figsize=(8, 6))

# Dwelling Type Distribution
plot_bar(data=data[data["CHARACTERISTIC_ID"].between(42, 49)],
         x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL",
         title="Dwelling Type Distribution",
         xlabel="Dwelling Type", ylabel="Count")

# Pairplot of Canada Census Data
sns.pairplot(data)
plt.suptitle('Pairplot of Canada Census Data', y=1.02)
plt.show()

# Correlation Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
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
plot_bar(data=data[data["CHARACTERISTIC_ID"].isin([1, 2])],
         x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL",
         title="Gender Distribution",
         xlabel="Gender", ylabel="Population Count", rotation=0)

# Employment Status Distribution
plot_bar(data=data[data["CHARACTERISTIC_ID"].between(25, 30)],
         x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL",
         title="Employment Status Distribution",
         xlabel="Employment Status", ylabel="Population Count")

# Education Level Distribution
plot_bar(data=data[data["CHARACTERISTIC_ID"].between(31, 36)],
         x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL",
         title="Education Level Distribution",
         xlabel="Education Level", ylabel="Population Count")

# Scatter Plot of Age vs Income
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='income', data=data)
plt.title('Age vs Income')
plt.xlabel('Age')
plt.ylabel('Income')
plt.show()

# Line Plot of Population Growth Over Years
if 'year' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='year', y='C1_COUNT_TOTAL', data=data)
    plt.title('Population Growth Over Years')
    plt.xlabel('Year')
    plt.ylabel('Total Population Count')
    plt.show()

# Box Plot of Age Distribution by Gender
if 'gender' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='gender', y='age', data=data)
    plt.title('Age Distribution by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Age')
    plt.show()

# Heatmap of Categorical Features
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