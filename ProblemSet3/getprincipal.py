def getprincipal(amount):#000000100.00
    amount = str(amount)
    if amount[0:3] == '000':
        amount = amount
        principal = amount
    else:
        famount = round(float(amount), 2)
        amount = str(famount)
        if amount[-3] == '.':
            amount = amount
            principal = amount[:-3]
        else:
            amount += '0'
            principal = amount[:-3]
        
        if principal[0] == '0':
            principal = principal[1:]
        else:
            principal = principal

    return principal, amount

print(getprincipal('000100'))
