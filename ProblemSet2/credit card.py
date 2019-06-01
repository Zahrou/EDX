

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate =  annualInterestRate/12
month = 1
total_paid = 0   
while month < 13:
    if monthlyPaymentRate <= 0.2:
        MinimumMonthlyPayment = monthlyPaymentRate * balance
        MonthlyUnpaidBalance =  balance - MinimumMonthlyPayment
        balance = (MonthlyUnpaidBalance) + (monthlyInterestRate * MonthlyUnpaidBalance)
        Round_MMP = round(MinimumMonthlyPayment, 2)
        Round_B = round(balance, 2)
        print("Month:%s " % month )
        print("Minimum monthly payment: %s" % Round_MMP)
        print("Remaining balance: %s" % Round_B)
        total_paid += MinimumMonthlyPayment
        Round_t = round(total_paid, 2)
        month += 1
print("Total paid:%s" % Round_t)
print("Remaining balance: %s" % Round_B)
        


    
