import string

def long(s):
	s2 = s
	MaxSubString = ''
	while len(s2) > 1:
		s = s2
		s0 = s[0]
		for i in range(len(s)-1) :
			if s[i] >= s0[-1] and s[i] < s[i+1]:
				s0 += s[i]
		if  s[0:2] != s0[0:2]:
			s0 = s0[1:]
		if s[-1] > s0[-1]:
                        s0 += s[-1]
                if len(s0) > len(MaxSubString):
                        MaxSubString = s0
                s2 = s2[1:]            
                
        return MaxSubString
        
                        

		
			
		
	
	
        
#431 num extrait de naissance
#acte de mariage 3893 jugement 1978
print(long('azyefaorkjtxvdmpk'))





