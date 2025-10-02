"""def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return round(ounces,2)

grams = float(input("enter the amount in grams: "))
print(f"it is {grams_to_ounces(grams)} ounces")"""

"""def fahrenheit_to_celsius(fahrenheit):
    celsius = ((5 / 9) * (fahrenheit - 32))
    return round(celsius, 3)

f = float(input("input temperature in fahrenheit: "))
print(f"the tempetature {fahrenheit_to_celsius(f)} celsius")"""

"""def solve(numheads, numlegs):
    for rabbits in range(numheads+1):
        chikens = numheads-rabbits
        if 2*chikens + 4*rabbits == numlegs:
            return chikens, rabbits
    return None, None

chikens, rabbits = solve(35, 94)
print(f"chikens {chikens}, rabbits {rabbits}")"""

"""import math

def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(num for num in numbers if is_prime(num))

nums = list(map(int, input("enter the numbers with spaces: ").split())) #.split() разбивает строку на отдельные слова (по пробелам).
print(f"the prime numbers is: {filter_prime(nums)}")  #map(int, ...) применяет функцию int() к каждому элементу списка, то есть превращает строки в числа."""


"""def permutations(s, step=""): #s - оставшаяся часть строки для перестановок
    if len(s) == 0: #step - уже собранная часть перестановки (изначально пустая)
        print(step)  # когда строка пустая - выводим собранное слово
    else:
        for i in range(len(s)):
            # фиксируем i-й символ и переставляем остальные
            permutations(s[:i] + s[i+1:], step + s[i]) #строка БЕЗ текущего символа s[i] and добавляем текущий символ к собранной части

# пример использования
s = input("Введите строку: ")
permutations(s)"""

"""def reverse(sentence):
    words = sentence.split() #split() → превращает строку в список слов
    reverse = words[::-1] #переворачиваем список. Синтаксис среза: list[start:stop:step]
    return " ".join(reverse) #соединяет слова обратно в строку через пробел.

s= input("input sentence: ")
print(reverse(s))"""

"""def has_33(nums):
    for n in range(len(nums)-1):
        if nums[n] == nums[n+1]:
            return True
    return False

n= list(map(int, input("enter the numbers: ").split()))
print(has_33(n))"""

"""def spy_game(nums):
    code = [0, 0, 7]   # последовательность, которую ищем
    for n in nums:
        if n == code[0]:    # если совпало с первым нужным элементом
            code.pop(0)     # удаляем его из списка code
        if not code:        # если code стал пустым
            return True
    return False

# Проверим
print(spy_game([1,2,4,0,0,7,5]))   # True
print(spy_game([1,0,2,4,0,5,7]))   # True
print(spy_game([1,7,2,0,4,5,0]))   # False"""

import math

"""def sphere_volume(r):
    volume = (4/3) * math.pi * (r**3)
    return round(volume, 2)  # округлим до 2 знаков после запятой

# пример использования
radius = float(input("input sphere's radius: "))
print("sphere's volume:", sphere_volume(radius))"""


"""def unique(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list
nums = [1, 2, 2, 3, 4, 4, 5, 1]
print("original list:", nums)
print("unique list:", unique(nums))  """

          
            


