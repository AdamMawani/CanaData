import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
data = pd.read_csv("census.csv")

# Explore the first few rows of the dataframe
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Data cleaning (if necessary)
# For this example, we assume the data is clean

# Data analysis and visualization

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