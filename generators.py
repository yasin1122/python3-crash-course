def create_cubes(n):
    for x in range(n):
        yield x**3

# Generators are memory efficient
for x in create_cubes(10):
    print(x, end=' ')
print()

def gen_fib():
    a, b = 1, 1
    for i in range(5):
        yield a
        # tuple matching avoids temp var
        a, b = b, a+b

current_fib = gen_fib()
print(next(current_fib))
print(next(current_fib))
print(next(current_fib))
print(next(current_fib))
print(next(current_fib))

iter_str = iter("Hello")
print(next(iter_str), next(iter_str),
      next(iter_str), next(iter_str), next(iter_str))