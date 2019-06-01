
def f(i):
    return i + 2
def g(i):
    return i > 5





def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest
    """
    L1 = []
    for i in L:
        s = f(i)
        
        if g(s) == True:
            
            L1.append(i)
    
    L.clear()
    for e in L1:
        L.append(e)
    if len(L) == 0:
        return -1
    else:
        return max(L)
    
        
