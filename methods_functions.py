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

