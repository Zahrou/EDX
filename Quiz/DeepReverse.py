def deep_reverse(L):
    
    L1 =[]
    for i in L:
        Li = []
        while len(i) > 0:
            Li.append( i[-1])
            i = i[:-1]
        L1.append(Li)
    
    L .clear()
    while len(L1) > 0:
        L.append(L1[-1])
        L1 = L1[:-1]
    
    

    

    

    
