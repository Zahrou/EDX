
annualInterestRate = 0.2
balance0 = 4773
monthlyPayment = 10
monthlyInterestRate = annualInterestRate/12
balance = balance0

while True:
    balance = balance0
    for month in range(1, 13):
        unpaidbalance =  balance - monthlyPayment
        balance = unpaidbalance + unpaidbalance * monthlyInterestRate
    if balance < 0:
        break
    else:
        monthlyPayment += 10
    
print("Lowest Payment:%s" % round(monthlyPayment, 2))

