# Collections Module
from collections import Counter
mylist = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]
print(Counter(mylist))
print(Counter('asdfasdfasasfasdfa'))

from collections import defaultdict
d = defaultdict(lambda: 0)
d['correct key'] = 100
# WRONG KEY is matched with default value
print(d['correct key'], d['WRONG KEY'])

from collections import namedtuple
Pet = namedtuple('Pet', ['name', 'age', 'type'])
tombik = Pet(name='Tombik', age=12, type='bird')
print(tombik)
print(tombik.age, tombik[1]) # diff ways getting age

# Shutil (shell utilities) and OS Module
"""
os.listdir() # list files in current dir
os.listdir("C:\\Users\\whois\\Documents")

import shutil
shutil.move('practice.txt','C:\\Users\\whois\\Documents' )

$ pip install send2trash
import send2trash
send2trash.send2trash('practice.txt')

import os
for file in os.walk("module_demo"):
    print(file)
"""
import os
print(os.getcwd())

# Datetime Module
import datetime

mytime = datetime.time(2, 20, 33) # hour, minute, seconds
mytime = mytime.replace(hour = 4)
print(mytime.minute, mytime)

today = datetime.date.today()
print(today, today.ctime())

day_date = datetime.datetime.today()
print(day_date)

date1 = datetime.date(1988, 11, 22)
print(date1.month)