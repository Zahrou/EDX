def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
        count = 0
    else:
        count = 1 + lenRecur(aStr[1:])
    return count 


print(lenRecur('dbd:fbdfb,'))

