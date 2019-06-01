
def f(a, b):
    return a-b



def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    diff = {}
    for k1 in d1.keys():
        for k2 in d2.keys():
            if k1 == k2 :
                intersect[k1] = f(d1[k1], d2[k2])
    for j in d1.keys():
        if j not in intersect :
            diff[j] = d1[j]
            
    for i in d2.keys():
        if i not in intersect:
            diff[i] = d2[i]
                
    return intersect, diff
