#Task 1:

"""import re # re - встроенный модуль regular expression, чтобы работать с регулярными выражениями(спец шаблоны для поиска текста)

txt = input(" Enter a text: ")
x = re.search(r"ab*", txt)# re.search()-функция, которая ищет первое совпадение с шаблоном в строке
if x:                    # r"ab*" - регулярное выражение, ищем букву а, b* - за ней может идти любое кол-во б(даже 0)
    print('Yes, we have a match', x.group()) # x.group()- показывает текст совпадения, который был найден шаблоном
else:
    print('no match') 
# raw string — «сырая строка», она помогает питону не интерпритировать обратные слэши '\' как спецсимволы, типа перенос строки и тд"""

#Task 2:

"""import re

txt = input('Enter a text: ')
x = re.search(r"ab{2,3}", txt)

if x:
    print('Yes, we have a match: ', x.group())
else:
    print('No match')"""
    

#Task 3:

'''import re 

txt = input('Enter a text: ')

x = re.findall(r"[a-z]+(?:_[a-z]+)+", txt) #re.findall() возвращает сразу список всех совпадений.

# [a-z]+ - ищет одну или более строчных букв, (?: ... ) - группа без захвата, нужна чтобы объеденить выражение, но не сохдавать отдельный результат, _[a-z]+ - ищет _+буквы, + после скобок говорит одно или больше таких блоков

if x:
    print('yes, we have the match: ', x)
    
else: 
    print('no match')'''
    
#Task 4:

"""import re

txt = input(' enter the text: ')

x = re.findall(r"[A-Z][a-z]+", txt)

if x:
    print('yes, we have the match: ', x)
else:
    print("no match")"""
    
#Task 5:

'''import re

txt = input('enter a text: ')
x = re.findall(r"^a.*b$", txt)

if x:
    print('yes, we have the match: ', x)
    
else:
    print('no match')'''
    
#Task 6:

"""import re

txt = input('enter the text: ')

x = re.sub(r"[ ,.]", ":", txt) #sub() Function - находит совпадения и заменяет их

print(x)"""

#Task 7:
'''import re

txt = input('enter the text: ')

x = re.sub(r"_([a-z])", lambda match: match.group(1).upper() , txt) #lambda — это короткий способ написать маленькую функцию, match — это объект, представляющий найденное совпадение

#group(0) — всё совпадение (_n), group(1) — только то, что в скобках, т.е. буква n
print(x)'''

#Task 8:

'''import re

txt = input("Enter the text: ")


x = re.findall(r"[A-Z][a-z]*", txt)

print("Result:", x)'''

#Task 9:

"""import re

txt = input("Enter the text: ")


x = re.sub(r"([A-Z])", r" \1", txt)


x = x.strip()

print("Result:", x)"""

#Task 10:

"""import re

txt = input("Enter the text: ")


x = re.sub(r"(?<!^)([A-Z])", r"_\1", txt)


x = x.lower()

print("Result:", x)"""