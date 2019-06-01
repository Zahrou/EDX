
annualInterestRate = 0.2
balance = 3926
monthlyPayment = 10

monthlyInterestRate = annualInterestRate /12

while True:
    for month in range(1,13):
        balance = balance - monthlyPayment
        updatedBalance = balance + balance * monthlyInterestRate
        #print round(balance,2),round(updatedBalance,2)

    if updatedBalance <= 0:
        break
    else:
        monthlyPayment += 10

print ("Lowest Payment:", monthlyPayment)
