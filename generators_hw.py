def gen_squares(n):
    for i in range(n):
        yield i**2
for i in gen_squares(10):
    print(i, end=" ")
print()

from random import randint
def rand_num(low, high, n):
    for i in range(n):
        yield randint(low, high)
for num in rand_num(1, 10, 12):
    print(num, end=' ')
print()

s = 'hello'
s_iter = iter(s)
for i in range(len(s)):
    print(next(s_iter), end = " ")
print()

my_list = [1,2,3,4,5]
# using () instead of [] creates a generator expression
gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item, end=' ')
print()
