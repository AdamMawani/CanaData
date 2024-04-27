import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("census.csv")

plt.figure(figsize=(10, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].between(9, 24)])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Age Group")
plt.ylabel("Population Count")
plt.title("Age Group Distribution")
plt.show()

plt.figure(figsize=(8, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].isin([59, 60, 61])])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Marital Status")
plt.ylabel("Population Count")
plt.title("Marital Status Distribution")
plt.show()

plt.figure(figsize=(10, 6))
sns.barplot(x="CHARACTERISTIC_NAME", y="C1_COUNT_TOTAL", data=data[data["CHARACTERISTIC_ID"].between(42, 49)])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Dwelling Type")
plt.ylabel("Count")
plt.title("Dwelling Type Distribution")
plt.show()

sns.pairplot(data)
plt.title('Pairplot of Canada Census Data')
plt.show()

correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Canada Census Data')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(data['age'], kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='province', y='income', data=data)
plt.title('Income Distribution Across Canadian Provinces')
plt.xlabel('Province')
plt.ylabel('Income')
plt.xticks(rotation=45)
plt.show()