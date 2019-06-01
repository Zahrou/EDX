

def semordnilap(str1, str2):
        '''
        str1: a string
        str2: a string
    
        returns: True if str1 and str2 are semordnilap;
        False otherwise.
        '''
        if len(str1) < 1 or len(str2) < 1:
                
                return True
        else:
                
                return str1[0] == str2[-1] and semordnilap(str1[1:], str2[:-1])
def semordnilapWrapper(str1, str2):
        # Strings with different length cannot be semordnilap
        if len(str1) != len(str2) :
                
                return False
        # A single-length string cannot be semordnilap
        elif len(str1) == 1 or len(str2) == 1:
                return False
        # Equal strings cannot be semordnilap
        elif str1 == str2:
                return False
        else:
                return semordnilap(str1, str2)

        

    
    
