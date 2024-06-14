def lesser_of_two_evens(a, b):
  if a%2 == 0 and b%2 == 0:
    return min(a, b)
  elif a%2 == 1 or b%2 == 1:
    return max(a, b)
  
print(lesser_of_two_evens(4, 8))

def animal_crackers(a, b):
  if a[0] == b[0]:
    return True
  else:
    return False
  
print(animal_crackers('Hello', 'Howdy'))

def makes_twenty(a, b):
  if a == 20 or b == 20 or a+b == 20:
    return True
  else:
    return False

print(makes_twenty(-20, 40))

def old_macdonald(name):
  counter = 1
  new_name = ''

  for ch in name:
    if counter == 1 or counter == 4:
      new_name +=  ch.upper()
    else:
      new_name += ch

    counter += 1
    
  return new_name

print(old_macdonald('macdonald'))

def master_yoda(sentence):
  return sentence.split()[::-1]

print(master_yoda('Hello how are you'))

def almost_there(num):
  if abs(100-num) <= 10 or abs(200-num) <= 10:
    return True
  else:
    return False
  
print(almost_there(199))

def has_33(nums):
  counter = 0
  nums.append(0)

  for num in nums:
    if num == 3 and nums[counter+1] == 3:
      return True
    counter += 1

  return False

print(has_33([3, 1, 3]))

def paper_doll(text):
  new_text = ''
  for ch in text:
    new_text += ch + ch + ch

  return new_text

print(paper_doll('Hello'))

def blackjack(a, b, c):
  if a+b+c <= 21:
    return a+b+c
  elif a==11 or b==11 or c==11 and a+b+c <= 31:
    return a+b+c - 10
  else:
    return 'BUST'
  
print(blackjack(10,10,11))

def summer_69(arr):
  sum = 0
  index6 = -1
  index9 = -1
  counter = 0

  for num in arr:
    if num == 6:
      index6 = counter
    if num == 9:
      index9 = counter
    counter += 1

  counter = 0
  for num in arr:
    if counter >= index6 and counter <= index9:
      pass
    else:
      sum += num
    counter += 1

  return sum

print(summer_69([2, 1, 6, 9, 11]))

def spy_game(nums):

  for i in range(len(nums)):
    if nums[i] == 0:
      for i in range(i, len(nums)):
        if nums[i] == 0:
          for i in range(i, len(nums)):
            if nums[i] == 7:
              return True

  return False

print(spy_game([1,2,4,0,1,0,7,5]))

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def count_primes(num): 
  prime_count = 0
  for i in range(2, num+1):
    if is_prime(i):
      prime_count += 1

  return prime_count

print(count_primes(100))

letter_a = "  *  \n" + \
           " * * \n" + \
           "*****\n" + \
           "*   *\n" + \
           "*   *"
letter_b = "*****\n" + \
           "*   *\n" + \
           "**** \n" + \
           "*   *\n" + \
           "*****"
letter_c = " *** \n" + \
           "*   *\n" + \
           "*    \n" + \
           "*   *\n" + \
           " *** "
letter_d = "**** \n" + \
           "*   *\n" + \
           "*   *\n" + \
           "*   *\n" + \
           "**** "
letter_e = "*****\n" + \
           "*    \n" + \
           "**** \n" + \
           "*    \n" + \
           "*****"
alphabet = {'a': letter_a,
            'b': letter_b,
            'c': letter_c,
            'd': letter_d,
            'e': letter_e}

def print_big(letter):
  return alphabet[letter.lower()]

print(print_big('A'))