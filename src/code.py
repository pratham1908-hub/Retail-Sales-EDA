# ============================================================
# Retail Sales Exploratory Data Analysis (EDA)
# Author : Pratham Zope
# Internship : Oasis Infobyte - Data Analytics
# ============================================================

# ===========================
# Import Libraries
# ===========================

import pandas as pd
import matplotlib.pyplot as plt

# ===========================
# Load Dataset
# ===========================

df = pd.read_csv("dataset.csv")

# ===========================
# Data Exploration
# ===========================

print("\n========== DATASET INFORMATION ==========\n")

print("First 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nDataset Info")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

# ===========================
# Data Cleaning
# ===========================

# Fill missing numerical values with Mean

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Price per Unit"] = df["Price per Unit"].fillna(df["Price per Unit"].mean())
df["Total Amount"] = df["Total Amount"].fillna(df["Total Amount"].mean())

# Fill missing categorical values with Mode

df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Product Category"] = df["Product Category"].fillna(df["Product Category"].mode()[0])

# Remove rows having missing Customer ID

df.dropna(subset=["Customer ID"], inplace=True)
df = df[df["Customer ID"].str.strip() != ""]

# Remove duplicate records

print("\nDuplicate Rows :", df.duplicated().sum())

df.drop_duplicates(inplace=True)

# ===========================
# Exploratory Data Analysis
# ===========================

# Total Revenue

total_revenue = df["Total Amount"].sum()
print("\nTotal Revenue :", total_revenue)

# Total Quantity Sold

total_quantity = df["Quantity"].sum()
print("Total Quantity Sold :", total_quantity)

# Revenue by Product Category

category_sales = (
    df.groupby("Product Category")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Product Category")
print(category_sales)

# Quantity Sold by Product Category

category_quantity = (
    df.groupby("Product Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQuantity Sold by Product Category")
print(category_quantity)

# Sales by Gender

gender_sales = (
    df.groupby("Gender")["Total Amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Gender")
print(gender_sales)

# Monthly Sales

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Total Amount"].sum()

# ===========================
# Data Visualization
# ===========================

# Revenue by Product Category

category_sales.plot(
    kind="bar",
    figsize=(8, 5),
    color="skyblue"
)

plt.title("Revenue by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Quantity Sold by Product Category

category_quantity.plot(
    kind="bar",
    figsize=(8, 5),
    color="red"
)

plt.title("Quantity Sold by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales by Gender

gender_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales by Gender")
plt.ylabel("")
plt.show()

# Total Revenue

plt.figure(figsize=(5, 4))

plt.bar(
    ["Total Revenue"],
    [total_revenue]
)

plt.title("Total Revenue")
plt.ylabel("Revenue")
plt.show()

# Total Quantity Sold

plt.figure(figsize=(5, 4))

plt.bar(
    ["Quantity Sold"],
    [total_quantity]
)

plt.title("Total Quantity Sold")
plt.ylabel("Quantity")
plt.show()

# Age Distribution

plt.figure(figsize=(6, 4))

plt.hist(
    df["Age"],
    bins=10
)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()

# Revenue Distribution

plt.figure(figsize=(6, 4))

plt.hist(
    df["Total Amount"],
    bins=15
)

plt.title("Revenue Distribution")
plt.xlabel("Total Amount")
plt.ylabel("Frequency")
plt.show()

# Monthly Sales Trend

monthly_sales.plot(
    kind="line",
    marker="o",
    figsize=(10, 5)
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n========== ANALYSIS COMPLETED SUCCESSFULLY ==========")