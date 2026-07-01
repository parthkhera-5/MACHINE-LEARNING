# Superstore Sales Data Analysis

## Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the Superstore Sales dataset to uncover valuable business insights related to sales performance, customer behavior, product demand, shipping efficiency, and regional trends. The objective is to help businesses make data-driven decisions that improve sales and overall performance.

---

## Problem Statement

The Superstore dataset contains information about customer orders, products, sales, and shipping details. The goal of this project is to analyze the dataset, identify meaningful patterns and trends, and provide actionable business recommendations based on the findings.

---

## Dataset Information

* **Dataset Name:** Superstore Sales Dataset
* **Number of Rows:** 9,800
* **Number of Columns:** 25
* **Data Type:** Mixed (Numerical, Categorical, Date)
* **Missing Values:** Postal_Code contains missing values.

---

## Variables Used

* Row_ID
* Order_ID
* Order_Date
* Ship_Date
* Ship_Mode
* Customer_ID
* Customer_Name
* Segment
* Country
* City
* State
* Postal_Code
* Region
* Product_ID
* Category
* Sub_Category
* Product_Name
* Sales
* Order_Year
* Order_Month
* Order_Day
* Ship_Year
* Ship_Month
* Ship_Day
* Shipping_Days

---

## Data Preprocessing

The following preprocessing steps were performed:

* Converted **Order_Date** and **Ship_Date** from object to datetime format.
* Created new features:

  * Order_Year
  * Order_Month
  * Order_Day
  * Ship_Year
  * Ship_Month
  * Ship_Day
  * Shipping_Days
* Checked for missing values.
* Explored data types and unique values.
* Performed descriptive statistical analysis.

---

## Exploratory Data Analysis

The following visualizations were created:

* Region-wise Sales Distribution
* Orders by Customer Segment
* Top 10 Customers by Sales
* Sales vs Shipping Days
* Top 15 States by Sales
* Top 20 Products by Sales
* Sales Distribution across Sub-Categories
* Sales Distribution Histogram
* Sales vs Postal Code by Region
* Monthly Sales Trend
* Orders by Year
* Average Sales by Segment and Ship Mode
* Year-wise Sales Share
* Correlation Heatmap
* Pair Plot

---

## Key Insights

* Sales are unevenly distributed across different regions.
* The Consumer segment contributes the highest number of orders.
* A few customers generate a significant portion of total sales.
* Certain products contribute much higher sales than others.
* Sales show seasonal variation across different months.
* Shipping days have very little impact on sales.
* Numerical variables show weak correlation with sales, while categorical variables provide stronger business insights.

---

## Business Recommendations

* Focus marketing efforts on high-performing regions and customer segments.
* Retain top customers through loyalty programs and personalized offers.
* Ensure sufficient inventory for high-selling products.
* Improve performance in underperforming regions and product categories.
* Plan promotions during peak sales months.
* Use customer and product insights for better business decision-making.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Google Colab

---

## Conclusion

The analysis reveals that sales are primarily influenced by customer segments, products, and regions rather than shipping duration or time-based features. By leveraging these insights, businesses can optimize marketing strategies, improve inventory management, enhance customer retention, and achieve sustainable business growth.

---
