"""print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))"""

"""print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) """

class myclass():
  def len(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return False

if myFunction():
  print("YES!")
else:
  print("NO!")
  
x = 200
print(isinstance(x, int))