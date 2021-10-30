# CS61A Extras
Welcome. You have found the gems of CS61A.

### Multiprocessing

[Ray](https://github.com/ray-project/tutorial)

Usual imports and header
```python
import ray
import time
ray.init(num_cpus=4, ignore_reinit_error=True, include_webui=False) # starts processes
```

```@ray.remote``` decorator
```python

@ray.remote
def slow_function():
  return 1
# slow_function.remote() returns ObjectID
# ray.get(slow_function.remote()) evaluates

# These happen in parallel.
for _ in range(4):
   slow_function.remote()

results = ray.get([slow_function.remote(i) for i in range(4)])

```

### Constraint Programming

#### Problem Solving
- Declare arbitrary variables by ```x = connector()```
- Declare constant variables by ```constant(y, 0.5)```
- If you want to broadcast their names, give them a name ```x = connector('X')```
- Join them by constraints (i.e. ```two_var(a, b), adder(x, y, z), multiplier(x, y, z)```

#### Two Variable Constraint
```python
def two_var(a, b):

    def a_to_b(x):
        # logic
        return x + 1
    
    def b_to_a(x):
        # logic, inverse of a_to_b
        return x - 1
    
    def make_constraint(a, b, f, invf):

        def new_value():
            av, bv = [connector['has_val']() for connector in (a, b)]
            if av:
                b['set_val'](constraint, f(a['val']))
            elif bv:
                a['set_val'](constraint, invf(b['val']))
            
        def forget_value():
            for connector in (a, b):
                connector['forget'](constraint)
        
        constraint = {'new_val': new_value, 'forget': forget_value}
        for connector in (a, b):
            connector['connect'](constraint)
        return constraint
    
    return make_constraint(a, b, s, invs)

```
### Tenary Constraints
Credit: Code from CS61A Lecture Slides
```
def ternary_constraint(a, b, c, ab, ca, cb):
    """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b)=a."""
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))

    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint
```

#### Connector
The network holding the constraints.
Credit: Code from CS61A Lecture Slides
```python
def connector(name=None):

    informant = None  # The source of the current val
    constraints = []  # A list of connected constraints

    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)

    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}

    return connector
```
