
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12
balance0 = 50000000
maxi = balance0*(1+monthlyInterestRate)**12
lowerBound = balance0/12
uperBound = (balance0*(1+monthlyInterestRate)**12)/12
monthlyPayment = (lowerBound+uperBound)/2


while True:
    balance = balance0
    
    for month in range(1, 13):
        unpaidbalance =  balance - monthlyPayment
        balance = unpaidbalance + unpaidbalance * monthlyInterestRate
    
    if int(balance) == 0 :
        break
    
    elif int(balance) > 0:
        lowerBound = monthlyPayment
        
    else:
        uperBound = monthlyPayment

    monthlyPayment = (lowerBound+uperBound)/2
print("Lowest Payment:%s" % round(monthlyPayment, 2))
