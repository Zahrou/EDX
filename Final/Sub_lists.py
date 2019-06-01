def getSublists(L, n):
    sub_list = []
    while len(L) >= n:
        try:
            
            sub_list.append(list(L[0:n]))
            L = L[1:]

        except IndexError:
            break

    return sub_list
