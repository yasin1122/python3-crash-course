try:
    f = open('testfile.txt', 'r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("There was an OS Error!")
finally:
    print("Finally block always runs.")