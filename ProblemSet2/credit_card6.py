balance = 50000000.12
annualInterestRate = 0.18
monthlyInterestRate =  annualInterestRate/12
month = 1

LowerBound = balance/12
UpperBound = (balance*(1+annualInterestRate)**12)/12


while True:
    balance0 = balance
    MonthlyPayment = (LowerBound+UpperBound)/2
    for month in range(12):
        
        MonthlyUnpaidBalance =  balance0 - MonthlyPayment
        balance0 = (MonthlyUnpaidBalance) + (monthlyInterestRate * MonthlyUnpaidBalance)
        balance0 = round(balance0, 2)

    
    if balance0 == 0:
        break
    elif balance0 < 0:
        UpperBound = MonthlyPayment 
    else:
        LowerBound = MonthlyPayment 
        
        
     


print("Monthly Payment :%s" % MonthlyPayment )
