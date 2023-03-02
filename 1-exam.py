
#2
class Shop():

	def __init__(product, description, quantity, summa):
		self.product = product
		self.description = description
		self.quantity = quantity
		self.summa = summa 

	def summ(self):
		summs = (self.quantity * self.summa)
		return f'{summs}'

if __name__ =='__main__':
	name_of_product = input('enter a name: ')
	descripts = input('enter the description: ')
	qty = int(input('enter a quantity: '))
	summas = int(input('enter a summ: '))
	print(qty*summas)

#3
class Square(object):
	def __init__(a,b,c,d):
		self.a = a 
		self.b = b 
		self.c = c 
		self.d = d 
	def perimetr(self):
		p = (a + b + c + d)
		return p
if __name__ == '__main__':
	nn = int(input('num'))
	n = int(input('num'))
	num = int(input('num'))
	nums = int(input('num'))
	numbers = Square(nn,n,num,nums).perimetr()
	print(numbers)
	
class Square():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def kv(self):
        self.P = self.a * 4

        self.S = (self.a**2)    
        return self.P,self.S
    
    



class Rect(Square):
    def __init__(self,a,b,sq2):
        super().__init__(a,b)
        self.sq2 = sq2

    def pram(self):

        self.P_2 = ((self.a+self.b)*2)
        self.S_2 = (self.a*self.b)
        
        return self.P_2,self.S_2




class Triangle(Rect):
    def __init__(self, a, b, sq2,c):
        super().__init__(a,b, sq2)
        self.c = c

    def tr(self):
        self.P_3 = (self.a+self.b+self.c)

        return self.P_3
    def trian(self):
    	self.P_4 = ((self.a**2)+(self.b**2))

    	return self.P_4


if __name__ == '__main__':
    jandar_1 = Square(15,10)
    print(jandar_1.kv())

    jandar_2 = Rect(16,17,13)
    print(jandar_2.pram())

    jandar_3 = Triangle(20,14,17,4)
    print(jandar_3.tr())

    jandar_4 = Triangle(20,15,6,25)
    print(jandar_4.trian())









