import numpy as np

sales = np.array([
    [[1200, 1500, 1800], [2000, 2200, 2500]],
    [[1400, 1600, 1900], [2100, 2300, 2600]]
])

print(sales)

for amount in np.nditer(sales):
    print(amount)

for store in sales:
    for month in store:
        for amount in month:
            print(amount)

total_sales = 0
for amount in np.nditer(sales):
    total_sales += int(amount)
print(f'Total sales: ${total_sales:,}')

record_count = 0
for amount in np.nditer(sales):
    record_count += 1
average_sales = total_sales / record_count
print(f'Number of records: {record_count}')
print(f'Average sales: ${average_sales:,.2f}')

highest_sales = 0
for amount in np.nditer(sales):
    if amount > highest_sales:
        highest_sales = int(amount)
print(f'Highest sales: ${highest_sales:,}')
