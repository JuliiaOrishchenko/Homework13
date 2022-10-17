def my_func():
    x = 1
    y = 2
    return x*y

print(my_func.__code__.co_nlocals)
