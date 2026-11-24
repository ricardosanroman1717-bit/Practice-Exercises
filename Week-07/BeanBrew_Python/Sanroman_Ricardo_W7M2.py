# Bean & Brew - Week 7, Module 2
import pandas as pd
import numpy as np
from pathlib import Path

print('pandas is ready!')

# Task 1.1: Drink prices as a Series
price_list = [4.75, 4.25, 5.25]
prices = pd.Series(price_list)
print(prices)
prices = pd.Series(price_list, index=['Latte', 'Cold Brew', 'Mocha'])
print(prices)
menu_dict = {'Chai': 4.50, 'Espresso': 3.00}
more_prices = pd.Series(menu_dict)
print(more_prices)
print(prices['Mocha'])

# Task 1.2: Build the stock DataFrame
stock_data = {
    'drink': ['Latte', 'Cold Brew', 'Mocha'],
    'cups_left': [120, 54, 98]
}
stock = pd.DataFrame(stock_data)
print(stock)
print(stock.to_string())
arr = np.array([[120, 54, 98]])
print(pd.DataFrame(arr))

# Task 1.3: Insert a column and build sample data
stock.insert(1, 'size', ['M', 'L', 'M'])
print(stock)
sample = pd.DataFrame(np.arange(6).reshape((3, 2)),
                      index=['Back Bay', 'Kendall', 'Seaport'],
                      columns=['Mon', 'Tue'])
print(sample)

# Task 1.4: Rows by label and by position
cups = pd.DataFrame({'Mon': [120, 98, 143], 'Tue': [135, 110, 128]},
                    index=['Back Bay', 'Kendall', 'Seaport'])
print(cups)
print(cups['Kendall':])
print(cups.loc['Seaport'])
print(cups.loc[['Back Bay', 'Seaport']])
print(cups.iloc[0])
# print(cups.loc[0])  # Predicted KeyError: 0 is not a row label.
cups.loc['Fenway'] = [88, 91]
print(cups)

# Task 1.5: Read the orders file
folder = Path(__file__).resolve().parent
orders = pd.read_csv(folder / 'bb_orders.csv')
print(orders)
print(pd.options.display.max_rows)

# Task 1.6: Explore the orders
print(orders.head(3))
print(orders.tail(2))
print(orders.describe())
orders.info()
print(orders['store'].value_counts())

# Task 1.7: Turn text into real dates
print(orders['order_date'].dtype)
# print(orders['order_date'].dt.month)  # Predicted AttributeError: dates are still text.
orders['order_date'] = pd.to_datetime(orders['order_date'])
print(orders['order_date'].dtype)
march = orders[orders['order_date'] >= '2026-03-01']
print(len(march))

# Task 2.1: Remove what we don't need
orders = orders.drop('notes', axis=1)
print(orders.shape)
print(orders.duplicated().sum())
result = orders.drop_duplicates(inplace=True)
print(result)  # Prediction: None, because inplace=True changes orders directly.
print(orders.shape)
print(len(orders.dropna()))

# Task 2.2: Filter rows
big = orders[orders['qty'] >= 4]
print(big)
back_bay = orders[orders['store'] == 'Back Bay']
print(len(back_bay))
bb_big = orders[(orders['store'] == 'Back Bay') & (orders['qty'] >= 2)]
print(bb_big[['order_id', 'qty']])

# Task 2.3: Replace values and fill the gap
print(orders['store'].value_counts())
orders.replace({'store': {'Kendall Sq': 'Kendall Square'}}, inplace=True)
print(orders['store'].value_counts())
orders['price'] = orders.price.fillna(5.25)
print(orders.loc[8])

# Task 2.4: Fix or drop bad data
orders.loc[12, 'qty'] = 5
for x in orders.index:
    if orders.loc[x, 'qty'] <= 0:
        orders.drop(x, inplace=True)
print(orders[['order_id', 'qty']].tail(4))
print(orders.shape)

# Task 2.5: Retrieve and add columns
print(orders['qty'].sum())
print(orders.qty.max())
orders['revenue'] = orders['qty'] * orders['price']
print(orders[['drink', 'qty', 'price', 'revenue']].head())

# Task 3.1: Basic aggregations
rev = orders['revenue']
print(rev.sum())
print(rev.count())
print(round(rev.mean(), 2))
print(rev.median())
print(rev.min(), rev.max())
print(orders.aggregate({'qty': ['sum', 'mean'],
                        'revenue': ['sum', 'max']}))

# Task 3.2: Group by store and by drink
store_rev = orders.groupby('store')['revenue'].sum()
print(store_rev)
drink_qty = orders.groupby(['drink'])[['qty']].sum()
print(drink_qty)
print(orders.groupby('store')['qty'].mean().round(2))

# Task 3.3: Sort the results
print(store_rev.sort_values(ascending=False))
top = orders.sort_values('revenue', ascending=False)
print(top[['order_id', 'store', 'revenue']].head(3))
print(drink_qty.sort_index(ascending=False))

# Task 3.4: Rank stores and drinks
print(store_rev.rank(ascending=False))
drink_qty['rank'] = drink_qty['qty'].rank(ascending=False)
print(drink_qty)

# Task 3.5: Merge in the cost of each drink
menu = pd.DataFrame({
    'drink': ['Chai', 'Cold Brew', 'Espresso', 'Latte', 'Mocha'],
    'cost': [1.40, 1.10, 0.90, 1.60, 1.90]
})
drink_cost = pd.merge(menu, drink_qty[['qty']], on=['drink'])
drink_cost['total_cost'] = drink_cost['qty'] * drink_cost['cost']
print(drink_cost)
detail = pd.merge(orders, menu, on=['drink'])
print(detail.shape)

# Task 3.6: Sales by month
orders['month'] = orders['order_date'].dt.month
orders['weekday'] = orders['order_date'].dt.day_name()
print(orders[['order_date', 'month', 'weekday']].head(3))
orders['order_month'] = orders['order_date'].dt.to_period('M')
monthly_sales = orders.groupby('order_month')['revenue'].sum()
print(monthly_sales)

# Task 4.1: Store-by-month report (optional challenge)
report = pd.pivot_table(orders, values='revenue', index='store',
                        columns='order_month', aggfunc='sum', fill_value=0)
print(report)
report.to_csv(folder / 'bb_store_month.csv')
print(pd.read_csv(folder / 'bb_store_month.csv'))

# Reflection 1: .loc uses row labels, so cups.loc[0] failed because 0 was not a store name.
# .iloc[0] worked because it selects by row position. For the 8th row after dropping label 7,
# I would use .iloc[7] because it selects the 8th position even when labels are missing.

# Reflection 2: inplace=True updates the original DataFrame instead of returning a new one.
# The method returns None, so assigning it back to orders would replace the DataFrame with None.

# Reflection 3: I would fix a value if I can confirm the correct number, like the order of 5 cups.
# If the correct value is unknown, I would drop the bad record instead of guessing.

# Reflection 4: Without cleaning, Seaport's 50-cup entry would count as $212.50 rather than $21.25.
# That would overstate its revenue by $191.25. Its cleaned revenue is $60.25, not $251.50.

# Reflection 5: .dt.month only saves the month number, so January from different years gets combined.
# .dt.to_period('M') includes both the year and month to keep those groups separate.
