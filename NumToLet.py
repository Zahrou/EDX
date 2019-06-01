DictEng = {  '1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
             '6':'six', '7':'seven', '8':'eight', '9':'nine', '10':'ten',
             '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen',
             '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen',
             '19':'nineteen', '20':'twenty', '21':'twenty one', '22':'twenty two',
             '23':'twenty three', '24': 'twenty four', '25':'twenty five', '26':'twenty six',
             '27':'twenty seven', '28':'twenty eight', '29':'twenty nine',
             '30':'thirty', '31':'thirty one', '32':'thirty two', '33':'thirty three',
             '34': 'thirty four', '35': 'thirty five','36':'thirty six',
             '37':'thirty seven', '38':'thirty eight', '39':'thirty nine',
             '40':'fourty', '41':'fourty one', '42':'fourty two', '43':'fourty three',
             '44': 'fourty four', '45': 'fourty five','46':'fourty six',
             '47':'fourty seven', '48':'fourty eight', '49':'fourty nine',
             '50':'fifty', '51':'fifty one', '52':'fifty two', '53':'fifty three',
             '54': 'fifty four', '55': 'fifty five','56':'fifty six',
             '57':'fifty seven', '58':'fifty eight', '59':'fifty nine',
             '60':'sixty', '61':'sixty one', '62':'sixty two', '63':'sixty three',
             '64': 'sixty four', '65': 'sixty five','66':'sixty six',
             '67':'sixty seven', '68':'sixty eight', '69':'sixty nine',
             '70':'seventy', '71':'seventy one', '72':'seventy two', '73':'seventy three',
             '74': 'seventy four', '75': 'seventy five','76':'seventy six',
             '77':'seventy seven', '78':'seventy eight', '79':'seventy nine',
             '80':'eighty', '81':'eighty one', '82':'eighty two', '83':'eighty three',
             '84': 'eighty four', '85': 'eighty five','86':'eighty six',
             '87':'eighty seven', '88':'eighty eight', '89':'eighty nine',
             '90':'ninety', '91':'ninety one', '92':'ninety two', '93':'ninety three',
             '94': 'ninety four', '95': 'ninety five','96':'ninety six',
             '97':'ninety seven', '98':'ninety eight', '99':'ninety nine',
             }

def get_format(amount):#000000100.00
    amount = str(amount)
    if amount[0:3] == '000':
        amount = amount
        principal = amount
    else:
        famount = round(float(amount), 2)
        amount = str(famount)
        if amount[-3] == '.':
            amount = amount
            principal = amount[:-3]
        else:
            amount += '0'
            principal = amount[:-3]
        
        if principal[0] == '0':
            principal = principal[1:]
        else:
            principal = principal

    return principal, amount
    


def get_hundreds(amount):
    principal = get_format(amount)[0] 
    
    if len(principal) == 1:
        output = DictEng[principal]
                 
    elif len(principal) == 2:
        if principal[0] == '0':
            output = DictEng[principal[1]]
        else:
            output = DictEng[principal[0:]]

    elif len(principal) == 3:
        if principal == '000':
            output = ''
        elif principal[-2:] == '00':
            output = DictEng[principal[0]] + ' hundred '
        elif principal[1] == '0':
            output = DictEng[principal[0]] + ' hundred ' +  'and ' + DictEng[principal[2:]]
        else:
            output = DictEng[principal[0]] + ' hundred ' + 'and ' + DictEng[principal[1:]]
    
             
    return output
    

def get_thousands(amount): #000100
    principal = get_format(amount)[0]
    amount = get_format(amount)[1]
    
        
    if len(principal) == 4:
        if principal[0] == '0':
            output = get_hundreds(principal[1:])
        elif principal[1:] == '000':
            output = DictEng[principal[0]] + ' thousands'     
        else:
            output = get_hundreds(amount[0]) + ' thousands ' + get_hundreds(principal[1:])
    elif len(principal) == 5:
        if principal[0:2] == '00':
            output = get_hundreds(principal[2:])
        elif principal[2:] == '000':
                output = get_hundreds(principal[0:2]) + ' thousands'     
        else:
            output = get_hundreds(principal[0:2]) + ' thousands ' + get_hundreds(principal[2:])
    elif len(principal) == 6:
        if principal[0:3] == '000':
            output = get_hundreds(principal[3:])
        elif principal[3:] == '000':
            output = get_hundreds(principal[0:3]) + 'thousands'
        else:
            output = get_hundreds(principal[0:3]) + ' thousands ' + get_hundreds(principal[3:])
    return output                    


def get_millions(amount):
    principal = get_format(amount)[0]

    if len(principal) == 7:
        if principal[0] == '0':
            output = get_thousands(principal[1:])
            
        elif principal[1:] == '000000':
            output = DictEng[principal[0]] + ' millions'
            
        else:
            output = get_hundreds(principal[0]) + ' million ' + get_thousands(principal[1:])
            
    elif len(principal) == 8:
        if principal[0:2] == '00':
            output = get_thousands(principal[2:])
        if principal[2:] == '000000':
            output = get_hundreds(principal[0:2]) + ' millions'     
        else:
            output = get_hundreds(principal[0:2]) + ' millions ' + get_thousands(principal[2:])
    elif len(principal) == 9:
        if principal[0:3] == '000':
            output = get_thousands(principal[3:])
        if principal[3:] == '000000':
            output = get_hundreds(principal[0:3]) + ' millions'
        else:
            output = get_hundreds(principal[0:3]) + ' millions ' + get_thousands(principal[3:])

    return output
    
                                                                 

def get_billions(amount):
    principal = get_format(amount)[0]
    
    if len(principal) == 10:
        if principal[1:4] == '000':
            output = get_hundreds(principal[0]) + ' billions ' + get_thousands(principal[4:])
            
        elif principal[0] == '0':
            output = get_millions(principal[1:])
        elif principal[1:] == '000000000':
            output = DictEng[principal[0]] + ' billions'     
        else:
            output = get_hundreds(principal[0]) + ' billions ' + get_millions(principal[1:])
    elif len(principal) == 11:
        if principal[2:5] == '000':
            output = get_hundreds(principal[0:2]) + ' billions ' + get_thousands(principal[5:])
        elif principal[0:2] == '00':
            output = get_millions(principal[2:])
        elif principal[2:] == '000000000':
            output = get_hundreds(principal[0:2]) + ' billions'     
        else:
            output = get_hundreds(principal[0:2]) + ' billions ' + get_millions(principal[2:])
    elif len(principal) == 12:
        if principal[3:6] == '000':
            output = get_hundreds(principal[0:3]) + ' billions ' + get_thousands(principal[6:])
        elif principal[0:3] == '000':
            output = get_millions(principal[3:])
        elif principal[3:] == '000000000':
            output = get_hundreds(principal[0:3]) + ' billions'
        else:
            output = get_hundreds(principal[0:3]) + ' billions ' + get_millions(principal[3:])
    return output        
    
    
def addcents(amount, currency = 'dollars'):
    principal = get_format(amount)[0]
    amount = get_format(amount)[1]
    
    if len(principal) < 4:
        if amount[-2:] == '00':
            final_output = get_hundreds(principal) + ' ' + currency 
        elif amount[-2] == '0':
            final_output = get_hundreds(principal) + ' ' + currency + ' and ' + DictEng[amount[-1:]] + ' cents'
        else:
            final_output = get_hundreds(principal) + ' ' + currency + ' and ' + DictEng[amount[-2:]] + ' cents'
    
    elif len(principal) < 7:
        if amount[-2:] == '00':
            final_output = get_thousands(principal) + ' ' + currency
        elif amount[-2] == '0':
            final_output = get_thousands(principal)+ ' ' + currency + ' and ' + DictEng[amount[-1:]] + ' cents'
        else:
            final_output = get_thousands(principal) + ' '+ currency + ' and ' + DictEng[amount[-2:]] + ' cents'
            
    elif len(principal) < 10:
        if amount[-2:] == '00':
            final_output = get_millions(principal) + ' ' + currency
        elif amount[-2] == '0':
            final_output = get_millions(principal) + ' ' + currency + ' and ' + DictEng[amount[-1:]] + ' cents'
        else:
            final_output = get_millions(principal) + ' ' + currency + ' and ' + DictEng[amount[-2:]] + ' cents'

    elif len(principal) < 13:
        if amount[-2:] == '00':
            final_output = get_billions(principal) + ' ' + currency
        elif amount[-2] == '0':
            final_output = get_billions(principal) + ' ' + currency + ' and ' + DictEng[amount[-1:]] + ' cents'
        else:
            final_output = get_billions(principal) + ' ' + currency + ' and ' + DictEng[amount[-2:]] + ' cents'

    return final_output

arg1 = input("please enter anumber not longer than 12 digits: ")
arg2 = input("please enter type a currency: ")
print(addcents(arg1,arg2))

