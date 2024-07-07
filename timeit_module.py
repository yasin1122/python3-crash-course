# Timing Your Python Code
import time

def func_one(n):
    return [str(num) for num in range(n)]
print(func_one(10))

def func_two(n):
    return list(map(str, range(n)))
print(func_two(10))

# func one time
start_time = time.time()
result = func_one(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

# func two time
start_time = time.time()
result = func_two(1000000)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

import timeit
statement = """
func_one(100)
"""
setup = """
def func_one(n):
    return [str(num) for num in range(n)]
"""
print(timeit.timeit(statement, setup, number=100000))

statement2 = """
func_two(100)
"""
setup2 = """
def func_two(n):
    return list(map(str, range(n)))
"""
print(timeit.timeit(statement2, setup2, number=100000))
