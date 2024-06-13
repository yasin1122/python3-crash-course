from random import randint
random_num = randint(1, 101)
# print(random_num)

user_guess = None
counter = 0

while user_guess != random_num:
  user_guess = int(input("Guess a number from 1 to 100: "))
  counter += 1

  if user_guess == random_num:
    print(f'That is CORRECT! It only took you {counter} tries.')
  elif user_guess < 1 or user_guess > 100:
    print('OUT OF BOUNDS')
  elif abs(random_num-user_guess) <= 10 and counter == 1:
    print('WARM!')
  elif abs(random_num-user_guess) > 10 and counter == 1:
    print('COLD!')
  elif abs(random_num-user_guess) <= abs(random_num-old_guess) and counter > 1:
    print('WARMER!')
  elif abs(random_num-user_guess) > abs(random_num-old_guess) and counter > 1:
    print('COLDER!')

  old_guess = user_guess