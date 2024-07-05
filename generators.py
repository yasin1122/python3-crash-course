def create_cubes(n):
    for x in range(n):
        yield x**3

cube_list = list(create_cubes(10))
print(cube_list)

# Generators are memory efficient
for x in create_cubes(10):
    print(x, end=' ')

