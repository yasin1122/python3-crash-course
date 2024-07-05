try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("There is a TypeError!")

try:
    x, y = 5, 0
    z = x / y
except ZeroDivisionError:
    print("Division by Zero!")
finally:
    print("All Done.")

def ask():
    while True:
        try:
            x = input("enter an int: ")
            print(f"{x} squared is {int(x)**2}")
        except Exception as error:
            print(error, "try again: ")
        else:
            break

ask()