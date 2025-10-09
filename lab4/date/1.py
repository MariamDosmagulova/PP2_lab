# Task 1:
'''import datetime #импорт всего модуля 

x= datetime.datetime.now() #нынешняя дата
y= x - datetime.timedelta(days=5)

print('current date: ', x.strftime("%Y-%m-%d"))
print('after substracting: ', y.strftime("%Y-%m-%d"))'''

# Task 2:
'''import datetime 

n = datetime.datetime.today()
y = n - datetime.timedelta(days=1)
t = n + datetime.timedelta(days=1)

print('yesterday: ', y.strftime("%Y-%m-%d"))
print('today: ', n.strftime("%Y-%m-%d"))
print('tomorrow: ', t.strftime("%Y-%m-%d"))'''

# Task 3:

'''import datetime

x = datetime.datetime.now()

print(f'now: {x.strftime("%Y-%m-%d %H:%M:%S")}')'''

#or with replace()

'''import datetime 

print(f'now {datetime.datetime.now().replace(microsecond=0)}')'''

# Task 4:
'''import datetime

date1= datetime.datetime(2025,4,23,12,5,6)
date2= datetime.datetime(2025,4,27,6,8,15)

diff = date2 - date1#diff - это объект timedelta, а не datetime

print(f'the differentce in seconds: {int(diff.total_seconds())}') #метод total_seconds() Возвращает float 
print(diff.days)
print(diff.seconds) #остаток секнд после дней'''


