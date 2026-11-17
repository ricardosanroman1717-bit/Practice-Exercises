employees = ['John', 'Sarah', 'Michael', 'Jennifer', 'David']
sales = [5200, 6800, 4500, 7200, 5800]


def calculate_total(sales):
    total_sales = 0
    for amount in sales:
        total_sales += amount
    return total_sales


def calculate_average(total, number_of_employees):
    return total / number_of_employees


def evaluate_performance(amount):
    if amount >= 7000:
        return 'Excellent'
    elif amount >= 6000:
        return 'Good'
    elif amount >= 5000:
        return 'Average'
    else:
        return 'Needs Improvement'


def find_highest_sales(sales):
    highest = sales[0]
    for amount in sales:
        if amount > highest:
            highest = amount
    return highest


def calculate_commission(amount, rate):
    return amount * rate


def generate_sales_report(employees, sales):
    header = f"{'Employee':<12}{'Sales':<12}{'Performance':<20}Commission"
    report_lines = [
        'EMPLOYEE SALES SUMMARY',
        '-' * len(header),
        header,
        '-' * len(header)
    ]

    for employee, amount in zip(employees, sales):
        performance = evaluate_performance(amount)
        commission = calculate_commission(amount, 0.05)
        sales_text = f'${amount:,.2f}'
        commission_text = f'${commission:,.2f}'
        report_lines.append(
            f'{employee:<12}{sales_text:<12}{performance:<20}{commission_text}'
        )

    return '\n'.join(report_lines)


total = calculate_total(sales)
print(f'Total Monthly Sales: ${total:,.2f}')

average = calculate_average(total, len(employees))
print(f'Average Sales per Employee: ${average:,.2f}')

print('\nEMPLOYEE SALES PERFORMANCE')
print('--------------------------')
for employee, amount in zip(employees, sales):
    performance = evaluate_performance(amount)
    print(f'{employee}: ${amount:,.2f} - {performance}')

highest_sales = find_highest_sales(sales)
print(f'\nHighest Sales Amount: ${highest_sales:,.2f}')

commission = calculate_commission(5200, 0.05)
print(f"John's Commission: ${commission:,.2f}")

report = generate_sales_report(employees, sales)
print(f'\n{report}')


# Challenge 1: Replace the fixed-rate commission with a sales-based rate.
def calculate_commission(amount):
    if amount >= 7000:
        rate = 0.10
    else:
        rate = 0.05
    return amount * rate


jennifers_commission = calculate_commission(7200)
johns_commission = calculate_commission(5200)
print(f"\nJennifer's Commission: ${jennifers_commission:,.2f}")
print(f"John's Commission: ${johns_commission:,.2f}")


def above_average(sales, average):
    count = 0
    for amount in sales:
        if amount > average:
            count += 1
    return count


above_average_count = above_average(sales, average)
print(f'\nEmployees Above Average: {above_average_count}')


def calculate_annual_sales(monthly_sales):
    return monthly_sales * 12


print('\nPROJECTED ANNUAL SALES')
for employee, amount in zip(employees, sales):
    annual_sales = calculate_annual_sales(amount)
    print(f'{employee}: ${annual_sales:,.2f}')
