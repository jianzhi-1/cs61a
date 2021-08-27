### Function Decorators
### @ is the decorator and the function is evaluated first
### then, def is executed
### then, result of evaluating decorated expression is applied on newly defined fn
### then, result is bound to the name in def

def trace(f):
    def wrapped(x):
        print('-> {}({})'.format(f, x))
        return f(x)
    return wrapped

@trace
def fib(x):
    if (x == 0 or x == 1): return 1
    return fib(x - 1) + fib(x - 2)

print(fib(3))

def apply_to_all(f, s):
    return [f(x) for x in s]
