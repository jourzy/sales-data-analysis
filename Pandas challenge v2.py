# CFG MOOC Python challenge v3
# April 2023
# Emma Jourzac


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

# Optional extras:
#
# Use Matplotlib or Seaborn to create detailed graphs of the sales data
# Calculate additional metrics (e.g. median sale price, standard deviation of sale prices)


# ----- importing libraries
import pandas as pd

# ----- helper functions


def read_csv(file):
    # Read in the data from a csv file
    result = pd.read_csv(file)
    return result


def frequency(data_frame, value):
    # checking the frequency of the value in the data set
    result = data_frame[value].value_counts()
    return result


def calc_product(data_frame, new_column, col1, col2):
    # multiplies the columns together and creates a new column with the result
    data_frame[new_column] = data_frame[col1] * data_frame[col2]


def avg(data_frame, col1="Category", col2="Sale Price"):
    # used to find the average in a category.
    # Sales Price used but could also use for other fields.
    # Groups the data by col1.
    # Calculates the mean value for the col2 data.
    # Rounded to 2 d.p.
    result = data_frame.groupby([col1])[col2].mean(numeric_only=True).round(2)
    return result


def group_sum(data_frame, col1="Month", col2="Total Sales"):
    # Group data by col1 e.g. "Month"
    # Add up all of col2. e.g. "Total Sales"
    result = data_frame.groupby([col1])[col2].sum()
    # Adds the index back in - needed to return the index containing highest and lowest values
    result = result.reset_index()
    return result


def highest(result, col2="Total Sales"):
    # Locates the index with the highest value e.g. "total sales"
    # and returns the data in this row - including month name.
    maximum = result.loc[result[col2].idxmax()]
    return maximum


def lowest(result, col2="Total Sales"):
    # Locates the index with the lowest value e.g. "total sales"
    # and returns the data in this row - including month name.
    minimum = result.loc[result[col2].idxmin()]
    return minimum


# ----- main program

# ----- 1. USE PANDAS TO READ IN THE SALES DATA FROM THE CSV FILE

# Read in the sales data from the csv file and print out results
df = read_csv("sales_dataset.csv")
print(df)

# ----- 2. CALCULATE THE TOTAL SALES FOR EACH PRODUCT

# checking that there is only one version of each product in the data
frequency = frequency(df, "Product Name")
print(frequency)

# creates a new column called "Total Sales" by multiplying
# together "Quantity sold" and "Sale Price"
calc_product(df, "Total Sales", "Sale Price", "Quantity Sold")
print(df)

# ----- 6. WRITE THE RESULTS OF YOUR ANALYSIS AS A CSV FILE

# saving the DataFrame as a CSV file
df.to_csv("2.total_sales.csv", index=True)

# ----- 3. DETERMINE THE AVERAGE SALE PRICE FOR EACH PRODUCT CATEGORY

# finding the average sale price for each category
avg_price = avg(df, "Category", "Sale Price")
print(avg_price)


# saving the DataFrame as a CSV file
avg_price.to_csv("3.avg_price.csv", index=True)

# ----- 4. IDENTIFY THE MONTH WITH THE HIGHEST SALES
#          AND THE MONTH WITH THE LOWEST SALES

# calculates the total sales grouped by month
month_total_sales = group_sum(df, "Month", "Total Sales")
print(month_total_sales)

# Locates the index with the highest value e.g. "total sales"
# and returns the data in this row - including month name.
max_month = highest(month_total_sales, "Total Sales")
print(max_month)

# saving the analysis as a CSV file
max_month.to_csv("4a.max_month.csv", index=True)

# Does the same for the minimum value
min_month = lowest(month_total_sales, "Total Sales")
print(min_month)

# saving the analysis as a CSV file
min_month.to_csv("4b.min_month.csv", index=True)


# ----- 5. DETERMINE WHICH CUSTOMER MADE THE MOST PURCHASES AND HOW MUCH THEY SPENT IN TOTAL

# finds total number of purchases and total sales by customer.
customer_purchases = group_sum(df, "Customer Name", ["Quantity Sold", "Total Sales"])
print(customer_purchases)

# Finds the customer with the highest number of purchases.
customer_max = highest(customer_purchases, "Quantity Sold")
print(customer_max)

# saving the DataFrame as a CSV file
customer_max.to_csv("5.customer_max.csv", index=True)
