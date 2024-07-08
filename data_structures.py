# Advanced Numbers

print(hex(15)) # hexadecimal representation
print(bin(15)) # binary representation
print(pow(2, 4), abs(-11), round(3.141592, 2))

# Advanced Strings

s = 'hello world'
print(s.capitalize(), s.upper(), s.count('o'),
      s.find('o'), s.center(20, '*'), '\n',
      s.isalnum(), s.isalpha(), s.islower(), 
      s.isspace(), s.istitle(), s.isupper(),
      s.endswith('d'), '\n', s.split('o'),
      s.partition('o'))

# Advanced Sets

s = set()
s.add(1)
s.add(2)
s.add(2) # no duplicates
print(s)
s = s.clear # clears the set
s = {1, 2, 3, 4}
sc = s.copy()
s.add(5)
print(s.difference(sc), s.difference_update(sc),
      s.discard(1), s.intersection(sc))

# Advanced Dictionaries

d = {'k1': 1, 'k2': 2}
print({x:x**2 for x in range(5)})

# .keys(), .values(), .items()
for key, value in d.items():
    print(key, value)

# Advanced Lists
list1 = [1, 2, 2, 2, 3, 3, 5, 4, 9, 7]
list1.extend([4, 3, 2, 1])
print(list1.count(2), list1.index(4), 
      list1.insert(4, 4))

# reverse, remove