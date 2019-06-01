

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    keys = []
    values = []
    lenlist = []
    

    for c, v in aDict.items():
        keys.append(c)
        values.append(v)
        
    for i in values:
        lenlist.append(len(i))
    for d in keys:
        if keys.index(d) == lenlist.index(max(lenlist)):
            return d
        
    
        
       
    

    
                       
        
    
    
    
        
     




