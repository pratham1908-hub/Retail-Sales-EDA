# 🛍️ Retail Sales Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project focuses on **Exploratory Data Analysis (EDA)** of a retail sales dataset. The objective is to clean the data, analyze customer purchasing behavior, identify sales trends, and generate business insights through statistical analysis and data visualization.

This project was completed as part of the **Data Analytics Internship** at **Oasis Infobyte**.

---

## 🎯 Objectives

* Perform data cleaning and preprocessing.
* Analyze retail sales data.
* Understand customer purchasing patterns.
* Identify the best-performing product categories.
* Visualize important business metrics.
* Generate actionable business insights.

---

## 📂 Project Structure

```text
Retail-Sales-EDA/
│
├── data/
│   └── dataset.csv
│
├── images/
│   ├── revenue_by_category.png
│   ├── quantity_by_category.png
│   ├── sales_by_gender.png
│   ├── age_distribution.png
│   ├── revenue_distribution.png
│   ├── daily_sales.png
│   ├── monthly_sales.png
│   └── correlation_heatmap.png
│
├── report/
│   └── EDA_Report.pdf
│
├── src/
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset Information

The dataset contains retail transaction records with the following attributes:

| Column Name      | Description                   |
| ---------------- | ----------------------------- |
| Transaction ID   | Unique transaction identifier |
| Date             | Date of purchase              |
| Customer ID      | Unique customer identifier    |
| Gender           | Customer gender               |
| Age              | Customer age                  |
| Product Category | Purchased product category    |
| Quantity         | Number of items purchased     |
| Price per Unit   | Price of one unit             |
| Total Amount     | Total transaction amount      |

---

## 🧹 Data Cleaning

The following preprocessing steps were performed:

* Checked dataset dimensions
* Inspected data types
* Generated descriptive statistics
* Checked missing values
* Handled missing values (where applicable)
* Removed duplicate records
* Converted date column to datetime format

---

## 📈 Exploratory Data Analysis (EDA)

The following analyses were performed:

* Total Revenue
* Average Purchase Amount
* Total Quantity Sold
* Revenue by Product Category
* Quantity Sold by Product Category
* Sales by Gender
* Customer Age Distribution
* Daily Sales Trend
* Monthly Sales Trend
* Correlation Analysis

---

## 📉 Visualizations

The project includes the following visualizations:

* 📊 Revenue by Product Category (Bar Chart)
* 📊 Quantity Sold by Product Category (Bar Chart)
* 🥧 Sales by Gender (Pie Chart)
* 📈 Daily Sales Trend (Line Chart)
* 📈 Monthly Sales Trend (Line Chart)
* 📊 Age Distribution (Histogram)
* 📊 Revenue Distribution (Histogram)
* 🔥 Correlation Heatmap

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Retail-Sales-EDA.git
```

Navigate to the project folder:

```bash
cd Retail-Sales-EDA
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python src/main.py
```

---

## 📋 Business Insights

Some of the insights that can be generated include:

* Highest revenue-generating product category.
* Most purchased product category.
* Customer purchasing patterns based on gender.
* Sales trends over time.
* Revenue distribution across transactions.
* Relationship between quantity sold and total revenue.

---

## 🔮 Future Improvements

* Interactive dashboard using Power BI or Tableau.
* Sales forecasting using Machine Learning.
* Customer segmentation.
* Profit analysis.
* Regional sales analysis.
* Interactive web dashboard using Streamlit.

---

## 👨‍💻 Author

**Pratham Zope**

Bachelor of Engineering (Computer Engineering)
Government Engineering College, Modasa (GTU)

---

## 📜 License

This project is developed for educational and internship purposes.
