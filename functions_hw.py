from math import pi

def sphere_vol(radius):
  return (4/3)*pi*radius**3

print(sphere_vol(2))

def range_check(num, low, high):
  return num>=low and num<=high

print(range_check(5, 2, 7))

def upper_lower(string):
  dict = {'upper': 0, 'lower': 0}
  for ch in string:
    if ch.isupper():
      dict['upper'] += 1
    elif ch.islower():
      dict['lower'] += 1
  print(f"Upper: {dict['upper']}, Lower: {dict['lower']}")

upper_lower('Hello Mr. Rogers, how are you this fine Tuesday?')

def unique_list(nums):
  # unique_list = []
  # for num in nums:
  #   if num not in unique_list:
  #     unique_list.append(num)
  # return unique_list
  return list(set(nums))

print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))

def multiply(nums):
  if not nums:
    return 0
  total=1
  for num in nums:
    total *= num
  return total

print(multiply([1, 2, 3, -4]))

def palindrome(str):
  str = str.replace(' ', '')
  # for i in range(int(len(str)/2)):
  #   if str[i] != str[-(i+1)]:
  #     return False
  #   return True
  return str == str[::-1]

print(palindrome('nurses run'))

from string import ascii_lowercase

def is_pangram(str):
  alphabet = list(ascii_lowercase)
  for ch in str:
    if ch in alphabet:
      alphabet.remove(ch)

  if len(alphabet) == 0:
    return True
  else:
    return False
  
print(is_pangram('The quick brown fox jumps over the lazy dog'))