income = float(input("Type the annual income: "))

if income <= 85528:
    tax = income * 0.18
    tax = tax - 556.02
else:
    tax = 14839.02
    surplus = income - 85528
    surplusTax = surplus * 0.32
    tax = tax + surplusTax
    
if tax < 0:
    tax = 0
    
tax = round(tax, 0)
print("The Tax is: ", tax, "thalers")