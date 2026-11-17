import statistics


days = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
]

sales = [1250, 1480, 1100, 1650, 1850,
         1420, 1700, 1300, 2100, 1950]

print('DAILY SALES REPORT')
print('------------------')
for i in range(len(days)):
    print(f'{days[i]} (Week {i // 5 + 1}): ${sales[i]:,.2f}')

print('\nDESCRIPTIVE STATISTICS')
print('----------------------')
total_sales = sum(sales)
average_sales = statistics.mean(sales)
median_sales = statistics.median(sales)
mode_sales = statistics.mode(sales)
standard_deviation = statistics.stdev(sales)
lowest_sales = min(sales)
highest_sales = max(sales)

print(f'Number of sales records: {len(sales)}')
print(f'Total sales: ${total_sales:,.2f}')
print(f'Mean: ${average_sales:,.2f}')
print(f'Median: ${median_sales:,.2f}')
if sales.count(mode_sales) == 1:
    print('Mode: No meaningful mode (all sales values occur once)')
else:
    print(f'Mode: ${mode_sales:,.2f}')
print(f'Standard deviation: ${standard_deviation:,.2f}')
print(f'Lowest sales: ${lowest_sales:,.2f}')
print(f'Highest sales: ${highest_sales:,.2f}')

print('\nSALES PERFORMANCE CLASSIFICATION')
print('--------------------------------')
excellent_days = 0
good_days = 0
average_days = 0
needs_improvement_days = 0

for i in range(len(sales)):
    if sales[i] >= 1800:
        performance = 'Excellent'
        excellent_days += 1
    elif sales[i] >= 1500:
        performance = 'Good'
        good_days += 1
    elif sales[i] >= 1200:
        performance = 'Average'
        average_days += 1
    else:
        performance = 'Needs Improvement'
        needs_improvement_days += 1
    print(f'{days[i]} (Week {i // 5 + 1}): ${sales[i]:,.2f} - {performance}')

print(f'Excellent days: {excellent_days}')
print(f'Good days: {good_days}')
print(f'Average days: {average_days}')
print(f'Needs Improvement days: {needs_improvement_days}')

print('\nSALES TARGET ANALYSIS')
print('---------------------')
sales_target = 1500
target_days = 0
for i in range(len(sales)):
    if sales[i] >= sales_target:
        print(f'{days[i]} (Week {i // 5 + 1}): ${sales[i]:,.2f}')
        target_days += 1

percentage_met = target_days / len(sales) * 100
print(f'Days meeting the $1,500.00 target: {target_days}')
print(f'Target achievement rate: {percentage_met:.2f}%')

print('\nFINAL BUSINESS ANALYSIS')
print('-----------------------')
print(f'Average daily sales: ${average_sales:,.2f}')
if average_sales >= 1700:
    print('Sales performance is excellent.')
elif average_sales >= 1500:
    print('Sales performance is good.')
else:
    print('Sales performance needs improvement.')

print('Days with above-average sales:')
above_average_days = 0
for i in range(len(sales)):
    if sales[i] > average_sales:
        print(f'{days[i]} (Week {i // 5 + 1}): ${sales[i]:,.2f}')
        above_average_days += 1
print(f'Number of above-average days: {above_average_days}')

highest_index = sales.index(highest_sales)
print(f'Highest sales day: {days[highest_index]} (Week {highest_index // 5 + 1}) - ${highest_sales:,.2f}')
