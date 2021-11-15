def vf_number(n):
    """Compute the nth Virahanka-Fibonacci number, for N >= 1
    >>> vf_number(2)
    1
    >>> vf_number(6)
    8
    """
    prev = 0
    curr = 1
    counter = 1
    while (counter < n):
        prev, curr = curr, prev + curr
        counter += 1
    return curr

def identity(x):
    return x

def square(x):
    return x*x

def cube(x):
    return x**3

def summation(n, term):
    """Sum the first N terms of a sequence
    >>> summation(5, cube)
    225
    >>> summation(5, square)
    55
    >>> summation(5, identity)
    15
    """
    total = 0
    for i in range(n):
        total += term(i + 1)
    return total

# define functions within functions
# returning a function
def make_adder(n):
    """
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    >>> make_adder(8)(9)
    17
    """
    def adder(k):
        return k + n
    return adder
