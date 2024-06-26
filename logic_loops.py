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

for num in range(1, 11, 2):
  print(num)

for index, ch in enumerate('Hello'):
  print(index, ch)

list1 = [1, 2, 3, 4] # 4 is ignored
list2 = ['a', 'b', 'c']
for item in zip(list1, list2):
  print(item)

print('x' in list2)
print('k1' in d, 2 in d.values())
print(min(num_list), max(num_list))

from random import shuffle, randint
shuffle(list1)
print(list1)
print(randint(0,100))

# id = input("enter your id: ")
# id = int(id)
# print(f'Your id is {id}')

list_comprehension = [letter for letter in 'Hello']
print(list_comprehension)

list_comp2 = [num**2 for num in range(1, 10)]
print(list_comp2)

list_comp3 = [num for num in range(1, 11) if num%2 == 0]
print(list_comp3)

list_comp4 = ['ODD' if x%2 == 1 else "EVEN" for x in range(1, 11)]
print(list_comp4)

nested_nums = [[1, 2, 3], [4, 5]]
for x in nested_nums:
  for y in x:
    print(y)

list_comp5 = [x*y for x in [1, 2, 3] for y in [10, 100, 1000]]
print(list_comp5)