def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    
    def apply_x(x):
        if len(L) == 0:

            result = 1 
            return result

        elif  len(L) == 1:
            result = L[0]*x**0
            return result
        
        else:
            
            result = (L[0]*x**(len(L)-1) + general_poly(L[1:])(x)) 
            
            return result

       
            
           
    return apply_x 























