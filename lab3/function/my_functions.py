import math

def sphere_volume(r):
    return (4/3) * math.pi * (r**3)

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
