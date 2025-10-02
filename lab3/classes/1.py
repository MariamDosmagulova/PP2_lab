"""class StringClass: 
    def __init__(self): # self - ссылка на текущий объект
        self.s = "" # этот атрибут принадлежит объекту
        
    def getString(self):
        self.s = input("Input string: ")
        
    def printString(self):
        print(self.s.upper())
        
obj = StringClass()
obj.getString()
obj.printString()"""

"""class shape:
    def area(self):
        return 0 
    
class sqare(shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length*self.length
    
s = sqare(5)
print("sqare's area: ", s.area())

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length*self.width
    

r = rectangle(4, 5)
print("Reactangle's area: ", r.area())"""

"""import math

class point:
    def __init__(self, y=0, x=0):# y=0 and x=0 стоят как юы по умолчанию, то есть еслимы зададим точку без x или y, то это не будет ошибка
        self.y = y
        self.x = x
        
    def show(self):
        print(f"coordinates of the point {self.y}, {self.x}")
        
    def move(self, y,x):
        self.y = y
        self.x = x
        
    def dist(self, other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
    
point1 = point(2,3)
point2 = point(5,8)

point1.show()
print(f"the distance between point1 and point2 is ", point1.dist(point2))"""

"""class account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance 
        
    def deposit(self, amount):
       self.balance += amount 
       print(f"deposit: {amount} balance: {self.balance}")
       
    def withdraw(self, amount):
        if amount>self.balance:
            print("not enough money on account")
        else:
            self.balance -= amount
            print(f"withdraw: {amount} balance: {self.balance}")
            
acc = account("Mariam", 500)
acc.deposit(10000)
acc.withdraw(999)
acc.withdraw(555)
acc.withdraw(10000001)"""


"""def is_prime(n):
    if n<2:
        return False
    for i in range(2, (int(n**0.5)+1)):
        if n%i ==0:
            return False
    return True

numbers = [1,2,3,4,5,6,7,8,9,10]
primes = list(filter(lambda x: is_prime(x), numbers)) #filter(функция, список) оставляет только те элементы, для которых функция возвращает True
print(f"primes: {primes}") """
        
        


    