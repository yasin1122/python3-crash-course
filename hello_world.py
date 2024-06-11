print("Hello Python World!")

# python3 --version
# Type python3 to use the REPL and quit() to exit
# Type python3 file_name.py to run it in terminal
# Use SHIFT + CTRL + DOWN to copy paste to new line

# 24 / 5 prints 4.8
# 24 // 5 prints 4
# round(24 / 5) prints 5

# True and False is False
# True or False is True

grade = 80

if grade > 65:
  print("Passed!")
else:
  print("Failed!")

print("Passed!") if grade > 65 else print("Failed!")

world = 'World'
print(f'Hello {world}')
print("This is {x}".format(x='Python!'))

new_list = ['apple', 'blueberry']
new_list.append('cherry')
first_item = new_list.pop(0)
print(new_list, first_item)

num_list = [5, 4, 8, 2, 1]
num_list.sort()
print(num_list)
letter_list = ['c', 'hhh', 'dd', 'k', 'fff', 'zz', 'ttt']
letter_list.sort(reverse=True)
print(letter_list)

my_dict = {'key1': 11, 'key2': 22}
print(my_dict)
d = {'k1': 111, 'k2': [1, 2, 3], 'k3': {'inKey1': 11111, 'inKey2': 22222}}
print(d["k2"][2], d['k3']['inKey2'])