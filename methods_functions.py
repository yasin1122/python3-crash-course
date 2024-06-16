def say_hello(name='Default'):
  return f'Hello {name}!'
print(say_hello('Jordan'))

points = [('Jordan', 35), ('LeBron', 28), ('Kobe', 50)]
def top_scorer(points):
  top_player = ''
  top_score = 0

  for player, score in points:
    if score > top_score:
      top_player = player
      top_score = score

  return (top_player, top_score)

top_player, top_score = top_scorer(points)
print(top_player, top_score)

from random import shuffle
init_list = [' ', 'O', ' ']
shuffle(init_list)
print(init_list)

def get_sum(*args):
  return sum(args)
print(get_sum(1, 2, 3))

def get_laker(**kwargs):
    if 'laker' in kwargs:
        print(f"{kwargs['laker']} is a Laker.")
    else:
        print('No Laker players were found.')

get_laker(bull='Jordan', laker='Kobe')

def square(num):
   return num**2

nums_list = [1, 2, 3, 4, 5]

for num in map(square, nums_list):
   print(num)

squared_nums = list(map(square, nums_list))
print(squared_nums)

def check_odd(num):
   return num%2==1

odd_nums = list(filter(check_odd, nums_list))
print(odd_nums)

square = lambda num: num**2
print(square(4))

cubed_nums = list(map(lambda num: num**3, nums_list))
print(cubed_nums)

even_nums = list(filter(lambda num: num%2 == 0, nums_list))
print(even_nums)

outer_num = 5

def inner_func():
   global outer_num
   print(outer_num)
   outer_num = 55

print(outer_num)
inner_func()
print(outer_num)