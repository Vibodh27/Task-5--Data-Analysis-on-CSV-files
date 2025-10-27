
## 📄 **README.md**

### 🧠 Project Title:

**Data Analysis on CSV Files**

### 🎯 Objective:

Analyze sales data using **Pandas** to gain insights such as total sales by region, profit by product, and visualize the data using charts.

---

### 🧩 Tools Used

* **Python 3.x**
* **Pandas** for data manipulation
* **Matplotlib** for visualization
* **Jupyter Notebook / Google Colab**

---

### 🚀 Steps to Run

1. Open **Jupyter Notebook** or **Google Colab**.
2. Upload `sales_data.csv` (ensure it contains columns like `Date, Region, Product, Sales, Profit`).
3. Run each code cell in order.
4. Charts will appear inline.

---

### 📊 Sample Outputs

* **Bar Chart 1:** Total Sales by Region
* **Bar Chart 2:** Total Profit by Product
* **Filtered Rows:** Rows where Sales > 1000
* **Data Summary:** Info, describe(), shape, and missing values

---

## 💬 **Interview Questions and Answers**

### 1️⃣ What is Pandas used for?

Pandas is a Python library used for **data manipulation and analysis**. It provides data structures like **Series** and **DataFrame** for handling structured data efficiently.

---

### 2️⃣ What’s a DataFrame?

A **DataFrame** is a 2D labeled data structure in Pandas, similar to an Excel sheet, with rows and columns.

---

### 3️⃣ How do you read a CSV file?

Using `pd.read_csv('filename.csv')`.

```python
df = pd.read_csv('data.csv')
```

---

### 4️⃣ What is groupby()?

`groupby()` is used to **split data into groups** based on some column values, then apply aggregation functions like sum, mean, etc.
Example:

```python
df.groupby('Region')['Sales'].sum()
```

---

### 5️⃣ How do you filter rows?

You can filter rows using boolean conditions.

```python
df[df['Sales'] > 1000]
```

---

### 6️⃣ Difference between loc[] and iloc[]?

* **loc[]** → Label-based indexing (uses column names).
* **iloc[]** → Integer-based indexing (uses row/column positions).

Example:

```python
df.loc[0:3, ['Product', 'Sales']]   # by label  
df.iloc[0:3, [1, 2]]               # by index position
```

---

### 7️⃣ What does .head() do?

Displays the first 5 rows of a DataFrame (default).

```python
df.head()
```

---

### 8️⃣ How can you create a bar chart?

Using `plot(kind='bar')` or Matplotlib.

```python
df.plot(x='Region', y='Sales', kind='bar')
plt.show()
```

---

### 9️⃣ What’s the shape of a DataFrame?

Returns a tuple representing the number of rows and columns.

```python
df.shape  # (rows, columns)
```

---

### 🔟 What is NaN?

**NaN** stands for “Not a Number” — it represents **missing or null values** in the dataset.

---

