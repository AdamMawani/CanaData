import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
data = pd.read_csv("census.csv")

# Plot population distribution by age group
plt.figure(figsize=(10, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].between(9, 24)])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Age Group")
plt.ylabel("Population Count")
plt.title("Population Distribution by Age Group")
plt.show()

# Plot marital status distribution
plt.figure(figsize=(8, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].isin([59, 60, 61])])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Marital Status")
plt.ylabel("Population Count")
plt.title("Marital Status Distribution")
plt.show()

# Plot dwelling types distribution
plt.figure(figsize=(10, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].between(42, 49)])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Dwelling Type")
plt.ylabel("Count")
plt.title("Distribution of Dwelling Types")
plt.show()

# Create a pairplot to visualize relationships between numerical variables
sns.pairplot(data)
plt.title('Pairplot of Canada Census Data')
plt.show()

# Example 1: Heatmap to visualize correlations between numerical variables
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Canada Census Data')
plt.show()

# Example 2: Distribution of a specific numerical variable
plt.figure(figsize=(8, 6))
sns.histplot(data['age'], kde=True, color='skyblue')
plt.title('Distribution of Age in Canada Census Data')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Example 3: Boxplot to visualize the distribution of a numerical variable across categories
plt.figure(figsize=(10, 6))
sns.boxplot(x='province', y='income', data=census_data)
plt.title('Income Distribution Across Provinces in Canada')
plt.xlabel('Province')
plt.ylabel('Income')
plt.xticks(rotation=45)
plt.show()