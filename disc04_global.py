def square(x):
    return x*x

def change_square():
    global square
    square = lambda x: x
    return 2

print(square(change_square()))
print(square(3))
