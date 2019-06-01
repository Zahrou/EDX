
def nfruits(dictionary, strin):
    while len(strin) > 0:
        if len(strin) == 1:
            dictionary[strin] -= 1
        else:
            for k in strin:
                if k in dictionary.keys():
                    dictionary[k] -= 1
                break
            for i in dictionary.keys():
                if i != k:
                    dictionary[i] += 1
        strin = strin[1:]

    
    output = "".join(['%s%s' % (k, v) for k, v in dictionary.items()])
    strialpha = ''
    for n in output:
        if n.isalpha():
            output = output.replace(n, '')
            strialpha += n

    for letter in strialpha:
        if output.index(max(output)) == strialpha.index(letter):
            l = letter
        
    return 'The max value is %s: %s' % (l, max(output))
    

                        
print(nfruits({'A': 1, 'B': 2, 'C': 3}, 'AC'))
