# Bean & Brew - Week 7, Module 1
import numpy as np
print('NumPy is ready!')

# Task 1.1: Loop through a 2D array
# Rows: Back Bay, Kendall Square; columns: Mon, Tue, Wed.
cups = np.array([[120, 135, 150],
                 [98, 110, 104]])
for row in cups:
    print(row)
for row in cups:
    for value in row:
        print(value)

# Task 1.2: Join and stack the store data
seaport = np.array([[143, 128, 161]])
all_stores = np.concatenate((cups, seaport))
print(all_stores)
thu_fri = np.array([[140, 172], [101, 95], [150, 166]])
week = np.concatenate((all_stores, thu_fri), axis=1)
print(week)
mon = np.array([120, 98, 143])
tue = np.array([135, 110, 128])
print(np.hstack((mon, tue)))
print(np.vstack((mon, tue)))
print(np.stack((mon, tue), axis=1))

# Task 1.3: Predict, then run: missing data
seaport_week = np.array([143, 128, 161, np.nan, 166])
print(seaport_week)
print(seaport_week.dtype)
print(np.sum(seaport_week))
seaport_none = np.array([143, 128, 161, None, 166])
print(seaport_none.dtype)
# Prediction: adding 1 fails because None is not a number.
# print(seaport_none + 1)  # TypeError: NoneType cannot be added to int.
print(seaport_week + 1)

# Task 1.4: Split the week into parts
# Prediction: the first half will get four values, and the second half three.
days = np.array([140, 152, 138, 160, 171, 199, 185])
halves = np.array_split(days, 2)
print(halves)
print(halves[1])
by_store = np.array_split(week, 3)
print(by_store[2])

# Task 1.5: Find the slow days with where()
TARGET = 150
print(np.where(days < TARGET))
print(np.where(days < TARGET, 'below', 'met'))
print(np.where(days < TARGET, days + 15, days))

# Task 1.6: Sort and filter the sales
print(np.sort(days))
print(days)
codes = np.array(['95', '100', '9', '120'])
print(np.sort(codes))  # Prediction: '100', '120', '9', '95' (text order).
print(np.sort(week))
busy = days > 160
print(busy)
print(days[busy])

# Task 2.1: Make repeatable random numbers
np.random.seed(7)
test_orders = np.random.randint(1, 6, size=(2, 5))
print(test_orders)
tips = np.random.rand(2, 3)
print(tips)

# Task 2.2: Predict, then run: simulate drink sizes
np.random.seed(7)
sizes = ['small', 'medium', 'large']
# Prediction: 0.3 + 0.5 + 0.3 = 1.1, so the probabilities cause a ValueError.
# orders = np.random.choice(sizes, p=[0.3, 0.5, 0.3], size=10)  # ValueError: probabilities do not sum to 1.
orders = np.random.choice(sizes, p=[0.2, 0.5, 0.3], size=10)
print(orders)
print(orders[orders == 'large'])
print(np.random.choice(sizes))

# Task 2.3: Simulate wait times with normal()
np.random.seed(7)
waits = np.random.normal(loc=4, scale=1, size=1000)
print(np.round(np.mean(waits), 2))
print(np.round(np.std(waits), 2))
within_1 = waits[np.absolute(waits - 4) < 1]
print(len(within_1))
within_2 = waits[np.absolute(waits - 4) < 2]
print(len(within_2))

# Task 3.1: Shuffle the barista rota
np.random.seed(7)
baristas = np.array(['Ana', 'Ben', 'Cho', 'Dev', 'Eli'])
print(np.random.permutation(baristas))
print(baristas)
np.random.shuffle(baristas)
print(baristas)

# Task 3.2: Revenue and cost with arithmetic ufuncs
mon_cups = np.array([120, 98, 143])
avg_price = np.array([4.50, 4.25, 4.75])
revenue = np.multiply(mon_cups, avg_price)
print(revenue)
cost = np.array([310, 260, 380])
print(np.subtract(revenue, cost))
print(np.divmod(mon_cups, 25))
print(np.absolute(np.array([-12, 5, -3])))

# Task 3.3: Predict, then run: five ways to round
changes = np.array([-2.7, -0.5, 0.5, 1.5, 2.5, 3.46])
# Prediction: np.round uses the nearest even integer for halfway values: 0.5 -> 0, 1.5 -> 2, 2.5 -> 2.
print(np.trunc(changes))
print(np.fix(changes))
print(np.floor(changes))
print(np.ceil(changes))
print(np.round(changes))
print(np.round(changes, 1))

# Task 3.4: Totals per store, per day and running totals
# Prediction: axis=1 returns 3 store totals and axis=0 returns 5 day totals.
print(week)
print(np.sum(week))
print(np.sum(week, axis=1))
print(np.sum(week, axis=0))
print(np.cumsum(days))

# Task 3.5: Growth and day-to-day change
growth = np.array([1.10, 1.05, 1.20])
print(np.round(np.prod(growth), 3))
print(np.round(np.cumprod(growth), 3))
print(np.diff(days))
print(np.diff(days, n=2))

# Task 4.1 (optional): Compare store menus with set operations
back_bay = np.array(['latte', 'mocha', 'latte', 'cold brew', 'chai'])
kendall = np.array(['latte', 'matcha', 'chai', 'chai'])
print(np.unique(back_bay))
print(np.union1d(back_bay, kendall))
print(np.intersect1d(back_bay, kendall))
print(np.setdiff1d(back_bay, kendall))
print(np.setdiff1d(kendall, back_bay))

# Reflection 1: axis=0 adds numbers down each column, so it produces five daily totals.
# axis=1 adds across each row, so it produces three store totals.
# Reflection 2: np.nan represents a missing number while keeping the array numeric, but the ordinary sum becomes nan.
# None blocks normal arithmetic, and 0 would incorrectly treat the missing day as zero sales.
# Reflection 3: The values are strings, so they are sorted character by character instead of by size.
# Converting them to numbers with codes.astype(int) would give the expected numeric order.
# Reflection 4: A seed makes random test data repeatable, which makes it easier to check calculations.
# Pseudo-random numbers are not suitable for generating secure passwords or encryption keys.
# Reflection 5: I would use np.ceil(143 / 25), which gives six sleeves, to ensure there are enough cups.
# np.divmod(143, 25) also shows five full sleeves plus 18 extra cups, so a sixth sleeve is needed.
# round() is not reliable for ordering because it can round down even when extra cups are needed.
