def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    if char == aStr[aStr/2]:
        return True
    elif char < aStr[aStr/2]:
        return isIn(char, aStr[0:aStr/2])
    else:
        return isIn(char, aStr[aStr/2:])

print(isIn("a", "akhftedfhv"))
