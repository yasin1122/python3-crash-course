if True:
  print('True')
elif False:
  print('False')
else:
  print('Error')

num_list = [4, 2, 6, 8, 1]
for num in num_list:
  print(f'The number in the list is {num}')

for ch in 'Hello':
  print(ch.upper())

nested_list = [[0], [1, 2], [3, 4, 5]]
for a, *b in nested_list:
  print(a, b)

d = {'k1':1, 'k2':2}
for key, value in d.items():
  print(key, value)

x = 5
while x > 0:
  x -= 1
  if x == 4:
    pass
  elif x == 3:
    continue
  elif x == 1:
    break
  print(x)