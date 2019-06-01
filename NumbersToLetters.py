
import fileinput

DictEng = {  '00':'', '0':'', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five',
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

def AmountsToLetters(amount):
    famount = round(float(amount), 2)
    amount = str(famount)
    output = ''

    if amount[-3] == '.':
        amount = amount
    else:
        amount += '0'
    principal = amount[:-3]
    
    if len(principal) == 1:
        output = DictEng[principal] 
        
    elif len(principal) == 2:
        if principal[0] == '0':
            output = DictEng[principal[1]]
        else:
            output = DictEng[principal]

    elif len(principal) == 3:
        if principal[-2:] == '00':
            output = DictEng[principal[0]] + ' hundred '
        elif principal[1] == '0':
            output = DictEng[principal[0]] + ' hundred ' +  'and ' + DictEng[principal[2:]]
        else:
            output = DictEng[principal[0]] + ' hundred ' + 'and ' + DictEng[principal[1:]]

            
    elif len(principal) == 4:
        if principal[-3:] == '000':
            output = DictEng[principal[0]] + ' thousand ' 
        elif principal[-2:] == '00':
            output = DictEng[principal[0]] + ' thousand ' + DictEng[principal[1]] + ' hundred '
        elif principal[-1:] == '0':
            output = DictEng[principal[0]] + ' thousand ' + DictEng[principal[1]] + \
                     ' hundred ' + 'and ' + DictEng[principal[-2:]] 
        elif principal[1] == '0' and principal[-2] == '0':
            output = DictEng[principal[0]] + ' thousand ' + 'and ' + \
                     DictEng[principal[-1:]]
        elif principal[1] == '0':
            output = DictEng[principal[0]] + ' thousand ' +  'and ' + DictEng[principal[2:]]
        elif principal[-2] == '0':
            output = DictEng[principal[0]] + ' thousand ' + DictEng[principal[1]] + ' hundred ' +\
                     'and ' + DictEng[principal[-1:]]
            
        else:
            output = DictEng[principal[0]] + ' thousand ' + DictEng[principal[1]] + ' hundred ' +\
                     'and ' + DictEng[principal[2:]]

            
    elif len(principal) == 5: 
        if principal[-3:] == '000':
            output = DictEng[principal[0:2]] + ' thousands' 
        elif principal[-2:] == '00':
            output = DictEng[principal[0:2]] + ' thousands ' + DictEng[principal[1]] + ' hundred '
        elif principal[-1:] == '0':
            output = DictEng[principal[0:2]] + ' thousands ' + DictEng[principal[1]] + ' hundred ' \
                     + 'and ' + DictEng[principal[-2:]]
        elif principal[2] == '0' and principal[-2] == '0':
            output = DictEng[principal[0:2]] + ' thousands ' + 'and ' + DictEng[principal[-1:]]
        elif principal[2] == '0':
            output = DictEng[principal[0:2]] + ' thousands ' +  'and ' + DictEng[principal[-2:]]
        elif principal[-2] == '0':
            output = DictEng[principal[0:2]] + ' thousands ' + DictEng[principal[2]] + ' hundred ' +\
                     'and ' + DictEng[principal[-1:]]
        else:
            output = DictEng[principal[0:2]] + ' thousands ' + DictEng[principal[2]] + ' hundred ' +\
                     'and ' + DictEng[principal[-2:]]      

    elif len(principal) == 6: 
        if principal[-5:] == '00000':
            output = DictEng[principal[0]] + ' hundred' + ' thousands' 
        elif principal[-4:] == '0000':
            output = DictEng[principal[0]] + ' hundred ' + DictEng[principal[1:3]] +' thousands' 
        elif principal[-2:] == '00':
            output = DictEng[principal[0]] + ' hundred ' + DictEng[principal[1:3]] +' thousands ' \
                     + DictEng[principal[3]] + ' hundred '
        elif principal[1] == '0' and principal[-2] == '0':
            output = DictEng[principal[0]] + ' hundred ' + DictEng[principal[2]] +' thousands ' \
                     + DictEng[principal[-1:]]
            
        elif principal[4] == '0':
            output = DictEng[principal[0]] + ' hundred ' + DictEng[principal[1:3]] +' thousands ' \
                     + DictEng[principal[3]] + ' hundred ' + DictEng[principal[-1:]]
        elif principal[3] == '0':
            output = DictEng[principal[0]] + ' hundred ' + DictEng[principal[1:3]] +' thousands ' \
                     + DictEng[principal[-2:]]
        elif principal[2] == '0':
            output = DictEng[principal[0]] + ' hundred ' + DictEng[principal[2]] +' thousands ' \
                     + DictEng[principal[-2:]]
        else:
            output = DictEng[principal[0]] + ' hundred ' + DictEng[principal[1:3]] +' thousands ' \
                     + DictEng[principal[3]] + ' hundred ' + DictEng[principal[-2:]]
            
    if output == '':
        return 'zero ' + currency
    else:
        return output + ' ' + currency

    

def addcents(amount, currency):
    famount = round(float(amount), 2)
    amount = str(famount)
    if amount[-3] == '.':
        amount = amount
    else:
        amount += '0'

    if amount[-2:] == '00':
        return AmountsToLetters(amount), currency
    elif amount[-2] == '0':
        return AmountsToLetters(amount), currency + ' and ' + DictEng[amount[-1:]] + ' cents'
    else:
        return AmountsToLetters(amount), currency + ' and ' + DictEng[amount[-2:]] + ' cents'
        
    
print(addcents(9014509000, 'dinars'))



            
    
