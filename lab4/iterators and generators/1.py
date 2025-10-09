# Task 1:
"""def generate_squares(N):
    for i in range(1, N+1):
        yield i ** 2 #yield - это ключевое слово
        
N=int(input('Enter a number: '))
for sqares in generate_squares(N):
    print(sqares)
    
N=int(input('Enter a number: '))

sqares=(i**2 for i in range(1,N+1)) # это генераторное выражение, которое создает объект-генератор, не хранит все элементы в памяти, а выдает их по одному(похоже на список)

for sqare in sqares:
    print(sqare)"""
    
# Task 2:
"""def generate_even_n(n):
    for i in range(0,n+1):
        if i%2==0:
            c= i
            yield c
        
        
n=int(input('enter a number: '))

print(",".join(str(i) for i in generate_even_n(n)))#Метод .join() работает только со строками, поэтому мы каждое число превращаем в строку через str(i)"""

# Task 3:
"""def divisible_by(n):
    for i in range(0, n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input('enter a number: '))

for i in divisible_by(n):
    print(i, end=' ')"""
    
# Task 4:
'''def sqгares(a,b):
    for i in range(a,b+1):
        yield i**2
        
a=int(input('enter the first number: '))
b=int(input('enter the second number: '))

for i in sqгares(a,b):
    print(i, end=' ')'''
    
'''a=int(input('enter the first number: '))
b=int(input('enter the second number: '))
squares =(i**2 for i in range (a,b+1) )
for i in squares:
    print(i, end=' ')'''
    
# Task 5:
'''def reverse(n):
    for i in range(n,-1, -1):
        yield i 
        
n = int(input('enter a numver: '))

for i in reverse(n):
    print(i, end=' ')'''
    

    
