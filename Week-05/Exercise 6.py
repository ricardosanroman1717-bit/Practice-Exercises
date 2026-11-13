day = 1

monday = 1200
tuesday = 1500
wednesday = 1100
thursday = 1800
friday = 1400

total_sales = 0


for day in range(1, 6):

    if day == 1:
        total_sales += monday
    elif day == 2:
        total_sales += tuesday
    elif day == 3:
        total_sales += wednesday
    elif day == 4:
        total_sales += thursday
    elif day == 5:
        total_sales += friday


average_sales = total_sales / 5

print("Total Sales: $", total_sales)
print("Average Daily Sales: $", average_sales)
