# Lecture 30: Structure of An Interpreter

## Eval
Base cases
- primitive values (numbers)
- (new) look up values bound to symbols

Recursive calls
- eval(operator, operands) of call expressions
- apply(procedure, argument)
- (new) eval(sub-expressions) of special forms

## Apply
Base cases
- built-in primitive procedures

Recursive calls
- (new) eval(body) of user-defined procedures

Mutual recursion: ```apply``` calling ```eval``` which calls ```apply```

scheme_eval()

## Frame
```python3
g = Frame(None)
g.define('y', 3)
g.lookup('y')
```

## Lambda



