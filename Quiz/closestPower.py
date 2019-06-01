# bad implementation of closest power

def bad_closest_power(base, num):
    num = int(num)
    exponent = 0
    dif = num - base**exponent
    exponetList = [0,]
    for i in range(num):
        dif1 = num - base**i
        
        if abs(dif1) <= abs(dif):
            exponent = i
        else:
            exponent = exponent
        if base**i > num:
            break
        exponetList.append(i)
    
    for j in exponetList:
        if abs(num - base**j) == abs(dif1):
            exponent = j
            
    
    return exponent


# A better implementation of closest power

def closest_power(base, num):
    num = int(num)
    exponent = 0
    dif = num - base**exponent
    for i in range(num):
        dif1 = num - base**i
        
        if abs(dif1) <= abs(dif):
            exponent = i
        else:
            exponent = exponent
        if base**i > num:
            break     
    
    return exponent



            
    


    
