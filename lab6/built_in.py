#built-in функции - это функции, которые уже встроены в питон и не нуждвются в импорте.

#Task 1

'''import math 

numbers = input('input the numvers: ')
x = [int(num) for num in numbers.split() ]

result = math.prod(x)
print(result)'''

#Task 2

'''a = input('input a string: ')

upper = 0
lower = 0

"""for i in a:
    if i.isupper():
        upper +=1
    elif i.islower():
        lower+=1
print(f'num_of_upper {upper} and num_of_lower {lower}') """

upper = sum(1 for i in a if i.isupper())
lower = sum(1 for i in a if i.islower())
print(f'num_of_upper {upper} and num_of_lower {lower}')'''

#Task 3

'''a = input('input a palindrome word: ')
a = a.lower()

reversed_a = ''.join(reversed(a)) #reversed- дает перевернутую по символам последовательность (возвращает итератор), а join объеденяет ее в строку без пробелов

if reversed_a == a:
    print("yes, it is")
else: 
    print('no')'''
    
#Task 4 (нужно дать ответ пользователю через определенное время)

'''import time
import math 

n = int(input('input a number: '))
mls = int(input('input the miliseconds: '))
seconds = mls/1000

time.sleep(seconds) #пауза

sqr = math.sqrt(n)

print(round(sqr,2))'''

#Task 5 

'''t = (True, False, 1)
t2 = (True, 'False', 1)
chek = all(t) #all() возвращает true если все эл трушные
chek2 = all(t2)
print(chek)
print(chek2)'''