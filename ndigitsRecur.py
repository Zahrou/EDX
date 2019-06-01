def ndigits(x):
    """
    Takes x, an integer as input
    Returns the number of digits in x
    """
    if abs(x) < 10:
        
        return 1
    
    else:
        
        return  1 + ndigits(abs(x)/10)
