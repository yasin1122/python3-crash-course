def create_cubes(n):
    for x in range(n):
        yield x**3

# Generators are memory efficient
for x in create_cubes(10):
    print(x, end=' ')
print()

def gen_fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        # tuple matching avoids temp var
        a, b = b, a+b

for i in gen_fib(5):
    print(i, end=' ')