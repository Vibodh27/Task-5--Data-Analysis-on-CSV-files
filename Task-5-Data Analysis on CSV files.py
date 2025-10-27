# -----------------------------------------------
# Task 5 : Data Analysis on CSV Files
# Objective : Analyze sales data using Pandas
# -----------------------------------------------

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
# You can replace 'sales_data.csv' with your own CSV file path
df = pd.read_csv('sales_data.csv')

# Display first few rows
print("?? First 5 rows of data:")
print(df.head())

# Display basic information about data
print("\n?? Data Info:")
print(df.info())

# Display summary statistics
print("\n?? Summary Statistics:")
print(df.describe())

# Example columns assumed: ['Date', 'Region', 'Product', 'Sales', 'Profit']

# 1?? Total sales by region
sales_by_region = df.groupby('Region')['Sales'].sum().reset_index()
print("\nTotal Sales by Region:")
print(sales_by_region)

# Plot total sales by region
sales_by_region.plot(x='Region', y='Sales', kind='bar', legend=False, color='skyblue')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.grid(axis='y')
plt.show()

# 2?? Total profit by product
profit_by_product = df.groupby('Product')['Profit'].sum().reset_index()
print("\nTotal Profit by Product:")
print(profit_by_product)

# Plot total profit by product
profit_by_product.plot(x='Product', y='Profit', kind='bar', color='orange', legend=False)
plt.title('Total Profit by Product')
plt.xlabel('Product')
plt.ylabel('Total Profit')
plt.grid(axis='y')
plt.show()

# 3?? Filtering rows example
# Show only rows where sales are greater than 1000
high_sales = df[df['Sales'] > 1000]
print("\nRows where Sales > 1000:")
print(high_sales.head())

# 4?? Check for missing values
print("\n?? Missing Values in Each Column:")
print(df.isna().sum())

# 5?? Shape of the dataset
print("\n?? Shape of the DataFrame:", df.shape)

print("\n? Data Analysis Completed Successfully!")
