def inc_longestRun(L):

    longestRun = []
    
    while len(L) > 0:
        current_longest = [L[0]]
        L1 = L
        for k in range(len(L)):
            if  L1[0] >= current_longest[-1]:
                current_longest.append(L1[0])
                L1 = L1[1:]
        
        current_longest = current_longest[1:]

        if len(current_longest) > len(longestRun):
            longestRun = current_longest

        
        L = L[1:]
    return longestRun


def dec_longestRun(L):

    longestRun = []
    
    while len(L) > 0:
        current_longest = [L[0]]
        L1 = L
        for k in range(len(L)):
            if  L1[0] <= current_longest[-1]:
                current_longest.append(L1[0])
                L1 = L1[1:]
        
        current_longest = current_longest[1:]

        if len(current_longest) > len(longestRun):
            longestRun = current_longest

        
        L = L[1:]
    return longestRun


def longestRun(L):
    decreasing = dec_longestRun(L)
    increasing = inc_longestRun(L)
    


    if len(decreasing) > len(increasing):
        output = sum(decreasing)
        
    elif len(decreasing) == len(increasing):
        if L.index(decreasing[0]) < L.index(increasing[0]):
            output = sum(decreasing)
        else:
            output = sum(increasing)
    else :
        output = sum(increasing)

    return output
