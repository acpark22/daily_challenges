"""Income cap and tax rate.  $10000 : 0%, $30000: 10%, $100000: 25%, >$100k: 40%.  Given a whole-number income amount up to $100000000, find the amount of tax owed to Examplania. Round down to a whole number."""

import math

def taxamount(income):
    if income <= 10000:
        return 0
    elif income <= 30000:
        return (income - 10000)*0.1
    elif income <= 100000:
        return taxamount(30000) + (income - 30000)*0.25
    else:
        return taxamount(100000) + (income - 100000)*0.40

print(math.floor(taxamount(200000)))
print(math.floor(taxamount(9999)))
print(math.floor(taxamount(234982543)))


