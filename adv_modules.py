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

# Math and Random Modules
import math
# help(math)
math.pi

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(random.randint(0, 100), 
      random.choice(letters),
      # can pick the same choice MORE than once
      random.choices(population=letters, k=3),
      # can ONLY pick each choice ONCE
      random.sample(population=letters, k=3),
      # floating point random number
      random.uniform(a=0, b=10))
random.shuffle(letters)

# Python Debugger
import pdb # python debugger
"""
pdb.set_trace()
print(10 / 0)
# q to quit
"""

# Zipping and Unzipping files
"""
f = open("new_file.txt",'w+')
f.write("Here is some text")
f.close()

f = open("new_file2.txt",'w+')
f.write("Here is some text")
f.close()

import zipfile

comp_file = zipfile.ZipFile('comp_file.zip','w')
comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall("extracted_content")

import shutil

directory_to_zip='C:\\Users\\Marcial\\Pierian-Data-Courses\\Complete-Python-3-Bootcamp\\12-Advanced Python Modules'

# Creating a zip archive
output_filename = 'example'
# Just fill in the output_filename and the directory to zip
# Note this won't run as is because the variable are undefined
shutil.make_archive(output_filename,'zip',directory_to_zip)

# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
shutil.unpack_archive(output_filename,dir_for_extract_result,'zip')
"""