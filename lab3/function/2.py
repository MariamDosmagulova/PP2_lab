"""def is_palindrome(s):
    s = s.lower().replace(" ", "")  # убираем пробелы и приводим к нижнему регистру
    return s == s[::-1]

# пример использования
word = input("enter word: ")
if is_palindrome(word):
    print("it is palindrome")
else:
    print("it is not palindrome")"""
    
    
"""def histogram(lst):
    for num in lst:
        print("*" * num)


histogram([4, 9, 7])"""

"""import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)   
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break


guess_the_number()"""





