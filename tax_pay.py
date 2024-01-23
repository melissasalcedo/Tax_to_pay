# Calculate Income Tax

# Given
money_income = 700000
payable_tax = 0
print("your income:", money_income)

# Calculate 
if money_income <= 10000:
    payable_tax = 0
elif money_income <= 20000:
    payable_tax = (money_income - 10000)* 10 / 100
else:
    payable_tax = 10000 * 10 / 100
    payable_tax += (money_income - 20000)* 20 / 100

# Print
print("Your total tax to pay is:", payable_tax)