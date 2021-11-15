# Control

- Any function that doesn't return a value returns a None value.
- ```None + None``` will give error.
- Pure functions are those that just returns a value. It doesn't print anything to console etc.
- Default argument(s)
```python
def f(x, y=2):
  return x*y
print(f(3)) # prints 6
print(f(3, 3)) # prints 9, overrode the argument y = 2

round(50.1234, 2) # returns 50.12
```

- Returning multiple values
```python
def divide(n, d):
   return (n//d), n%d
print(divide(100, 13)) # returns (7, 9)

# unpacking tuple
q, r = divide(100, 13)
```

- Doctest: mimicks a successful interactive session
```python
def divide(n, d):
  """
  >>> q, r = divide(2021, 10)
  >>> q
  202
  >>> r
  1
  """
  return (n//d), n%d
```

- Boolean expressions: returns the last thing that it evaluates
For *or*, once Python evaluates something as *True*, it returns that value (may be integer).
For *and*, once Python evaluates something as *False*, it returns that value (may be integer).
Else, returns last thing that it evaluates.
*not* returns either *True* or *False*.

- Clauses
Python evaluates the first line, then unless directed to, it will not execute the rest of the suites in the clause.
