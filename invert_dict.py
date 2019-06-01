

def dict_invert(d):
    ValuesWithMultipleOccurences = []
    ValuesWithSingleOccurence = []
    MultipleKeys = []
    SingleKeys = []
    invert_1 = {}
    invert_2 = {}
    for v in list(d.values()):
        if list(d.values()).count(v) > 1:
            ValuesWithMultipleOccurences.append(v)
        else:
            ValuesWithSingleOccurence.append(v)
    for el in ValuesWithMultipleOccurences:
        while ValuesWithMultipleOccurences.count(el) > 1:
            ValuesWithMultipleOccurences.remove(el)
    
    for ele in ValuesWithMultipleOccurences:
        sub_Multiplekeys = []
        for k in d.keys():
            
            if d[k] == ele:
                sub_Multiplekeys.append(k)
                if sub_Multiplekeys not in MultipleKeys:
                    MultipleKeys.append(sub_Multiplekeys)

    for elem in ValuesWithSingleOccurence:
        sub_Singlekeys = []
        for k1 in d.keys():
            
            if d[k1] == elem:
                sub_Singlekeys.append(k1)
                if sub_Singlekeys not in SingleKeys:
                    SingleKeys.append(sub_Singlekeys)
    
        
    while len( ValuesWithMultipleOccurences) and len(MultipleKeys) > 0:
            invert_1[ValuesWithMultipleOccurences[0]] = sorted(MultipleKeys[0])
            ValuesWithMultipleOccurences = ValuesWithMultipleOccurences[1:]
            MultipleKeys = MultipleKeys[1:]

    while len( ValuesWithSingleOccurence) and len(SingleKeys) > 0:
            invert_2[ValuesWithSingleOccurence[0]] = sorted(SingleKeys[0])
            ValuesWithSingleOccurence = ValuesWithSingleOccurence[1:]
            SingleKeys = SingleKeys[1:]
                
    invert_2.update(invert_1)

    return invert_2 
