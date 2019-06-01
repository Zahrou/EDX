def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    us_num = str(us_num)
    if len(us_num) == 1:
        return trans[us_num]
    
    elif len(us_num) == 2:
        if us_num == '10':
            return 'shi'
            
        elif us_num[1] == '0':
            return  trans[us_num[0]] + ' shi'
        elif us_num[0] == '1':
            return 'shi ' + trans[us_num[1]]
        
        else:
            return trans[us_num[0]] + ' shi ' + trans[us_num[1]]
    
