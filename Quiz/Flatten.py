def flatten(Alist):
    Blist = []
    for i in Alist:
        if type(i) != list:
            
            Blist.append(i)
            
            
        else:
            
            Blist += flatten(i)
    return Blist
            
