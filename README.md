# CS 61A
### UC Berkeley Fall 2021, taught by Prof John DeNero and Prof Pamela Fox
This repository is meant to store my lecture/discussion notes, which I think would be nice to share with my peers. I will **not** be uploading anything related to homework or assignments. Please contact me if you feel any file should not be here. Thanks!

### Misc
- General
```shell
$ python3 -i file.py
$ python3 -m doctest lab00.py
$ python3 -m doctest lec4.py -v
```
- Submission
```shell
$ python3 ok
$ python3 ok --submit
```

### Notes

#### Definitions
- Higher order function: either takes another function as an argument or returns a function as a result
- First order function: all other functions
- Refactoring: produces same result, but make code organization/structure better

#### Control (09/01 Lab)
- Things that represents False: False, 0, None, [], "", ()
- Short circuiting behavior: 
  - ```and``` short-circuits when it hits a False value. 
  - ```or``` short-circuits when it hits a True value.
- ```not``` always return True or False value
- Order of binding (placing of parenthesis): ```not```, ```and```, ```or```
- Interesting Python behaviors:
```python
>>> 5 == True
False
>>> 1 == True
True
>>> "" == False
False
```
- ```__eq__``` dunder method: Python automatically calls ```__eq__``` when the ```==``` operator is used. Otherwise, it uses ```is``` by default.
```python
    def __eq__(self, other):
        # firstly, check the instance
        if isinstance(other, Person):
            return self.age == other.age
        return False
```
- ```is``` checks whether the operands refer to the same object (i.e. present in the same memory location), while ```==``` checks for value equality of the operands

#### Errors (09/01 Lab)
- ```SyntaxError```
- ```IndentationError```: just use consistent indenting
- ```TypeError```: called function on an operand that wasn't the correct type
- ```ZeroDivisionError```: 1/0
- ```AttributeError```: when calling an attribute that an object doesn't have

### Lambdas (09/01 Lecture)
- Can only return an expression, which limits how much lambda functions can do.
- Useful if function is not used anywhere else (adhoc function)
- Shows up a bit differently in environmental diagrams
```python
# lambda <parameters>: <expression>

f = lambda x: x if x >= 0 else -x # lambda with ternary
comp = lambda x, y: x > y # lambda with multiple parameters
g = lambda x: (x, x*x) # lambda returning multiple values
```

### Environmental Diagram and Global (09/03 Discussion)
- global

```
Global frame
f1: f [parent=Global]
f2: λ <line 8> [parent=f1]
```

- Any name evaluates to the value bound in its earliest frame
- Every user defined function has a parent frame, which is the frame in which the function is defined.

```python
f(lambda x: x*x) # here, the parent of lambda is Global
```

- For variable look-up, look in the current frame before going up the sequence

- Call expressions
  - evaluate operator
  - evaluate operand (left to right)
  - apply functions (if any) to operand, opening new frames

```python
f(g(x)) # here, the parent of g's frame is Global
```

- Opening a new frame
  - Frame number
  - Frame name
  - Frame's parent
  - Bind parameters to arguments
  - Execute body of function


