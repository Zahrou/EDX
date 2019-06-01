def num2word(amount,  currency = ''):
    DictFrn = {  '1':'un', '2':'deux', '3':'trois', '4':'quatre', '5':'cinq',
             '6':'six', '7':'sept', '8':'huit', '9':'neuf', '10':'dix',
             '11':'onze', '12':'douze', '13':'treize', '14':'quatorze',
             '15':'quinze', '16':'seize', '17':'dix-sept', '18':'dix-huit',
             '19':'dix-neuf', '20':'vingt', '21':'vingt un', '22':'vingt deux',
             '23':'vingt trois', '24': 'vingt quatre', '25':'vingt cinq', '26':'vingt six',
             '27':'vingt sept', '28':'vingt huit', '29':'vingt neuf',
             '30':'trente', '31':'trente un', '32':'trente deux', '33':'trente trois',
             '34': 'trente quatre', '35': 'trente cinq','36':'trente six',
             '37':'trente sept', '38':'trente huit', '39':'trente neuf',
             '40':'quarante', '41':'quarante un', '42':'quarante deux', '43':'quarante trois',
             '44': 'quarante quatre', '45': 'quarante cinq','46':'quarante six',
             '47':'quarante sept', '48':'quarante huit', '49':'quarante neuf',
             '50':'cinquante', '51':'cinquante un', '52':'cinquante deux', '53':'cinquante trois',
             '54': 'cinquante quatre', '55': 'cinquante cinq','56':'cinquante six',
             '57':'cinquante sept', '58':'cinquante huit', '59':'cinquante neuf',
             '60':'soixante', '61':'soixante un', '62':'soixante deux', '63':'soixante trois',
             '64': 'soixante quatre', '65': 'soixante cinq','66':'soixante six',
             '67':'soixante sept', '68':'soixante huit', '69':'soixante neuf',
             '70':'soixante-dix', '71':'soixante-onze', '72':'soixante-douze', '73':'soixante-treize',
             '74': 'soixante-quatorze', '75': 'soixante-quinze','76':'soixante-seize',
             '77':'soixante dix-sept', '78':'soixante dix-huit', '79':'soixante dix-neuf',
             '80':'quatre-vingt', '81':'quatre-vingt un', '82':'quatre-vint deux', '83':'quatre-vint trois',
             '84': 'quatre-vingt quatre', '85': 'quatre-vingt cinq','86':'quatre-vingt six',
             '87':'quatre-vingt sept', '88':'quatre-vingt huit', '89':'quatre-vingt neuf',
             '90':'quatre-vingt dix', '91':'quatre-vingt onze', '92':'quatre-vingt douze', '93':'quatre-vingt treize',
             '94': 'quatre-vingt quatorze', '95': 'quatre-vingt quinze','96':'quatre-vingt seize',
             '97':'quatre-vingt dix-sept', '98':'quatre-vingt dix-huit', '99':'quatre-vingt dix-neuf',
            }
    
    def get_format(amount):
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
            output = DictFrn[principal]
                 
        elif len(principal) == 2:
            if principal[0] == '0':
                output = DictFrn[principal[1]]
            else:
                output = DictFrn[principal[0:]]

        elif len(principal) == 3:
            if principal == '000':
                output = ''
            elif principal[-2:] == '00':
                if principal[0] == '1':
                    output = 'cent '
                else:
                    output = DictFrn[principal[0]] + ' cent '
            elif principal[1] == '0':
                if principal[0] == '1':
                    output = 'cent ' + DictFrn[principal[2:]]
                else:
                    
                    output = DictFrn[principal[0]] + ' cent '  + DictFrn[principal[2:]]
            else:
                if principal[0] == '1':
                    output = 'cent ' + DictFrn[principal[1:]]
                else:
                    output = DictFrn[principal[0]] + ' cent '  + DictFrn[principal[1:]]
                
        return output

    def get_thousands(amount):
        principal = get_format(amount)[0]
        amount = get_format(amount)[1]
        
        if len(principal) == 4:
            if principal[0] == '0':
                output = get_hundreds(principal[1:])
            elif principal[1:] == '000':
                if principal[0] == '1':
                    output = 'mille '
                else:
                    output = DictFrn[principal[0]] + ' mille'     
            else:
                if principal[0] == '1':
                    output = 'mille ' + get_hundreds(principal[1:])
                else:
                    output = get_hundreds(amount[0]) + ' mille ' + get_hundreds(principal[1:])
        elif len(principal) == 5:
            if principal[0:2] == '00':
                output = get_hundreds(principal[2:])
            elif principal[2:] == '000':
                output = get_hundreds(principal[0:2]) + ' mille'     
            else:
                output = get_hundreds(principal[0:2]) + ' mille ' + get_hundreds(principal[2:])
        elif len(principal) == 6:
            if principal[0:3] == '000':
                output = get_hundreds(principal[3:])
            elif principal[3:] == '000':
                output = get_hundreds(principal[0:3]) + 'mille'
            else:
                output = get_hundreds(principal[0:3]) + ' mille ' + get_hundreds(principal[3:])
        return output

    def get_millions(amount):
        principal = get_format(amount)[0]

        if len(principal) == 7:
            if principal[0] == '0':
                output = get_thousands(principal[1:])
            
            elif principal[1:] == '000000':
                output = DictFrn[principal[0]] + ' millions'
            
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
                output = get_hundreds(principal[0]) + ' milliards ' + get_thousands(principal[4:])
            
            elif principal[0] == '0':
                output = get_millions(principal[1:])
            elif principal[1:] == '000000000':
                output = DictFrn[principal[0]] + ' milliards'     
            else:
                output = get_hundreds(principal[0]) + ' milliards ' + get_millions(principal[1:])
        elif len(principal) == 11:
            if principal[2:5] == '000':
                output = get_hundreds(principal[0:2]) + ' milliards ' + get_thousands(principal[5:])
            elif principal[0:2] == '00':
                output = get_millions(principal[2:])
            elif principal[2:] == '000000000':
                output = get_hundreds(principal[0:2]) + ' milliards'     
            else:
                output = get_hundreds(principal[0:2]) + ' milliards ' + get_millions(principal[2:])
        elif len(principal) == 12:
            if principal[3:6] == '000':
                output = get_hundreds(principal[0:3]) + ' milliards ' + get_thousands(principal[6:])
            elif principal[0:3] == '000':
                output = get_millions(principal[3:])
            elif principal[3:] == '000000000':
                output = get_hundreds(principal[0:3]) + ' milliards'
            else:
                output = get_hundreds(principal[0:3]) + ' milliards ' + get_millions(principal[3:])
        return output

    def addcents(amount, currency = 'dollars'):
        principal = get_format(amount)[0]
        amount = get_format(amount)[1]
    
        if len(principal) < 4:
            if amount[-2:] == '00':
                final_output = get_hundreds(principal) + ' ' + currency 
            elif amount[-2] == '0':
                final_output = get_hundreds(principal) + ' ' + currency + ' et ' + DictFrn[amount[-1:]] + ' centimes'
            else:
                final_output = get_hundreds(principal) + ' ' + currency + ' et ' + DictFrn[amount[-2:]] + ' centimes'
    
        elif len(principal) < 7:
            if amount[-2:] == '00':
                final_output = get_thousands(principal) + ' ' + currency
            elif amount[-2] == '0':
                final_output = get_thousands(principal)+ ' ' + currency + ' et ' + DictFrn[amount[-1:]] + ' centimes'
            else:
                final_output = get_thousands(principal) + ' '+ currency + ' et ' + DictFrn[amount[-2:]] + ' centimes'
            
        elif len(principal) < 10:
            if amount[-2:] == '00':
                final_output = get_millions(principal) + ' ' + currency
            elif amount[-2] == '0':
                final_output = get_millions(principal) + ' ' + currency + ' et ' + DictFrn[amount[-1:]] + ' centimes'
            else:
                final_output = get_millions(principal) + ' ' + currency + ' et ' + DictFrn[amount[-2:]] + ' centimes'

        elif len(principal) < 13:
            if amount[-2:] == '00':
                final_output = get_billions(principal) + ' ' + currency
            elif amount[-2] == '0':
                final_output = get_billions(principal) + ' ' + currency + ' et ' + DictFrn[amount[-1:]] + ' centimes'
            else:
                final_output = get_billions(principal) + ' ' + currency + ' et ' + DictFrn[amount[-2:]] + ' centimes'

        return final_output

    return addcents(amount, currency)

uotput = num2word(9887854.454, 'euro' )


    
    

