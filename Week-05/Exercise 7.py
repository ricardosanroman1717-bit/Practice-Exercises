
# Exercise 7: Analyzing Monthly Sales Data

# Task 1: Create dataset
monthly_sales = [12500.50, 14200.75, 11800.25,
                 15600.00, 16250.50, 17500.00]

months = ['January', 'February', 'March',
          'April', 'May', 'June']

# Task 2: Basic Enumeration
months = ['January', 'February', 'March',
          'April', 'May', 'June']

for index, month in enumerate(months, start=1):
    print(f'Month {index}: {month}')

# Task 3: Analyze Monthly Sales
monthly_sales = [12500.50, 14200.75, 11800.25,
                 15600.00, 16250.50, 17500.00]

for index, sales in enumerate(monthly_sales, start=1):
    print(f'Month {index} Sales: ${sales:,.2f}')
