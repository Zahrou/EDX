def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    exp = int(abs(exp))
    if exp == 0:
        return 1
    elif exp == 1:
        
        return base
    else:
        result = base
        while exp > 1:
            result *= base
            exp -= 1
        return result

print(iterPower(8.94, 6))
