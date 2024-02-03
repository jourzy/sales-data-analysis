# CFG MOOC Python challenge v3
# April 2023
# Emma Jourzac

# Import the library to use in this program
import pandas as pd


# Imagine you work for a small company that sells products online.
# Your manager has asked you to analyse the sales data from the past year to determine
# which products are the best-selling.
# You have also been asked to identify any trends in customer purchasing behaviour.


# Your task is to write a Python program that reads in a CSV file containing the sales data.
# You should  perform  the following tasks:

# 1. Use Pandas to read in the sales data from the CSV file provided in the
# “student materials” folder on Slack (sales_dataset.csv)
# 2. Calculate the total sales for each product
# 3. Determine the average sale price for each product category 
# 4. Identify the month with the highest sales and the month with the lowest sales
# 5. Determine which customers made the most purchases and how much they spent in total
# 6. Write the results of your analysis as a CSV file

# ----- 1. USE PANDAS TO READ IN THE SALES DATA FROM THE CSV FILE

# Read in the sales data from the csv file
df = pd.read_csv("sales_dataset.csv")
print(df)

# checking that there is only one version of each product in the data
df["Product Name"].value_counts()


# ----- 2. CALCULATE THE TOTAL SALES FOR EACH PRODUCT

# You can create a new column of data like this:
df["Total Sales"] = df["Sale Price"] * df["Quantity Sold"]

print(df)

# ----- 6. WRITE THE RESULTS OF YOUR ANALYSIS AS A CSV FILE

# saving the DataFrame as a CSV file
df.to_csv("2.total_sales.csv", index=True)

# ----- 3. DETERMINE THE AVERAGE SALE PRICE FOR EACH PRODUCT CATEGORY

# Groups the data by Category. 
# Calculates the mean value for the Sale Price data. 
# Rounded to 2 d.p.
avg_price = df.groupby(["Category"])["Sale Price"].mean(numeric_only=True).round(2)
print(avg_price)

# ----- 6. WRITE THE RESULTS OF YOUR ANALYSIS AS A CSV FILE

# saving the DataFrame as a CSV file
avg_price.to_csv("3.avg_price.csv", index=True)

# ----- 4. IDENTIFY THE MONTH WITH THE HIGHEST SALES AND THE MONTH WITH THE LOWEST SALES

# Group data by month.
# Add up all sales for that month
month_total = df.groupby(["Month"])["Total Sales"].sum()
print(month_total)

# Adds the index back in - needed to return the index containing highest and lowest values
month_total = month_total.reset_index()

print(month_total)

# Locates the index with the highest total sales and returns the data in this row - including month name.
max_month = month_total.loc[month_total["Total Sales"].idxmax()]
print(max_month)

# saving the analysis as a CSV file
max_month.to_csv("4a.max_month.csv", index=True)

# Does the same for the minimum value
min_month = month_total.loc[month_total["Total Sales"].idxmin()]
print(min_month)

# saving the analysis as a CSV file
min_month.to_csv("4b.min_month.csv", index=True)


# ----- 5. DETERMINE WHICH CUSTOMER MADE THE MOST PURCHASES AND HOW MUCH THEY SPENT IN TOTAL

# Adds up all purchases (quantity sold) grouped by customer name.
customer = df.groupby(["Customer Name"])[["Quantity Sold", "Total Sales"]].sum(numeric_only=True)
print(customer)

# Finds the customer with the highest number of purchases.
customer_max = customer.loc[customer["Quantity Sold"].idxmax()]
print(customer_max)

# saving the DataFrame as a CSV file
customer_max.to_csv("5.customer_max.csv", index=True)
