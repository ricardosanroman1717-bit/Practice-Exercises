
# TODO 1: Header comment
# Name: Ricardo
# Date: 11/16/2026
# Description: Calculate estimated income tax based on income and dependents.

# TODO 2: Define constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.00
DEPENDENT_DEDUCTION = 2000.00

# TODO 3: Display title
print("INCOME TAX CALCULATOR")
print("------------------------------------")

# TODO 4: Get gross annual income
gross_income = float(input("Enter gross annual income: "))

# TODO 5: Get number of dependents
number_of_dependents = int(input("Enter number of dependents: "))

# TODO 6: Calculate deductions
dependent_deductions = DEPENDENT_DEDUCTION * number_of_dependents
total_deductions = STANDARD_DEDUCTION + dependent_deductions

# TODO 7: Calculate taxable income
taxable_income = gross_income - total_deductions

# TODO 8: Calculate estimated tax
estimated_income_tax = taxable_income * TAX_RATE

# TODO 9: Display the summary
print()
print("INCOME TAX SUMMARY")
print("------------------------------------")

print(f"{'Gross Income:':<25}${gross_income:,.2f}")
print(f"{'Standard Deduction:':<25}${STANDARD_DEDUCTION:,.2f}")
print(f"{'Dependent Deductions:':<25}${dependent_deductions:,.2f}")
print(f"{'Total Deductions:':<25}${total_deductions:,.2f}")
print(f"{'Taxable Income:':<25}${taxable_income:,.2f}")
print(f"{'Tax Rate:':<25}{TAX_RATE:.0%}")
print(f"{'Estimated Income Tax:':<25}${estimated_income_tax:,.2f}")
