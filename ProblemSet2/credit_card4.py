


def interest_counter(balance, annual_interest_rate, min_month_payment_rate):
    month = 1
    monthly_interest_rate = annual_interest_rate/12
    total_payment = 0
    remaining_balance = balance  
    for month in range(12):
        min_month_payment = remaining_balance *min_month_payment_rate
        total_payment += min_month_payment
        month += 1
        mothly_unpaid_balance = remaining_balance - min_month_payment
        remaining_balance = mothly_unpaid_balance  * (1+monthly_interest_rate)
        r_mmp = round(min_month_payment, 2)
        r_tp = round(total_payment, 2)
        r_rb = round(remaining_balance, 2)
        print("Month: %s" %  month)
        print("Minimum monthly payment: %s" % r_mmp)
        print("Remaining balance: %s" % r_rb)
    
    
    print("Total paid: %s" % r_tp)
    print("Remaining balance: %s" % r_rb)
    

print(interest_counter(4213, 0.2, 0.04))   
        
        
