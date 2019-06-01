
balance = 4773
annualInterestRate = 0.2
monthlyInterestRate =  annualInterestRate/12
month = 1
total_paid = 0
MonthlyPayment = 10
balance0 = balance
while balance0 > 0:
    balance0 = balance
    for month in range(12):
        
        MonthlyUnpaidBalance =  balance0 - MonthlyPayment
        balance0 = (MonthlyUnpaidBalance) + (monthlyInterestRate * MonthlyUnpaidBalance)
        
    if balance0 < 0:
        break
    else:
        MonthlyPayment += 10
     
    

print("Monthly Payment :%s" % round(MonthlyPayment, 2))


