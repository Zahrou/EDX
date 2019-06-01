def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    saStr = sorted(aStr)
    

    if saStr == []:
        return False
    elif len(saStr)== 1:
        if char == aStr:
            return True
        else:
            return False
    elif char == saStr[int(len(saStr)/2)]:
        return True
    elif char < saStr[int(len(saStr)/2)]:
        return isIn(char, saStr[:int(len(saStr)/2)])
    elif char > saStr[int(len(saStr)/2)]:
        return isIn(char, saStr[int(len(saStr)/2):])

