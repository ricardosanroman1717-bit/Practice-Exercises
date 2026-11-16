1. Why must gross income be converted to a float data type?

A float lets us use numbers with decimals. We use it because money can have cents.

2. Why is the number of dependents converted to an int data type?

An int is used for whole numbers. We use it because we count dependents in whole numbers.

3. What is the purpose of the .2f format specifier in an f-string?

The .2f makes numbers show two decimal places. This makes money look like $100.00 instead of $100.0.

4. Which arithmetic operators did you use in this program, and where?

I used multiplication (*) to calculate deductions and taxes. I used addition (+) to add deductions and subtraction (-) to find taxable income.

5. How would you modify the program to prevent taxable income from becoming negative?

I would use max() to stop taxable income from going below zero. If the deductions are higher than the income, it would show zero instead.