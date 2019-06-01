class coordinate(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def diffirence(self, other):
		x_dis_sq = (self.x-other.x)**2
		y_dis_sq = (self.y-other.y)**2
		return (x_dis_sq+y_dis_sq)**0.5

##	def __str__(self):

##                return "<" +  str(self.x) +","+ str(self.y) + ">"
        

        
        
        
class Weird(object):
    
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y
    
    

        
            
        
             
        
            
class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
        
    
        
        
    
X = 7
Y = 8

try:
    w1 = Weird(X, Y)
    print(w1.getX())
except:
    pass
w2 = Wild(X, Y)
print(w2.getX())
print(w2.getY())
w3 = Wild(17, 18)
print(w3.getX())
print(w3.getY())
w4 = Wild(X, 18)
print(w4.getX())
print(w4.getY())
X = w4.getX() + w3.getX() + w2.getX()
print(X)

