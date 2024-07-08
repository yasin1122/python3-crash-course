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
print(s.difference(sc))