# Inheritance

```python

class SubClass(ParentClass):
  def methods(self):
    # logic
```

- Equivalent ways of calling superclass
```python
ParentClass.method(self, food);

super().eat(food);
super().__init__()
```

```python
class A:
  x = 2
  @staticmethod
  def get():
    return A.x
```

- Extending multiple classes
```python
class A(B, C):
  # logic
```

Every Python class inherits from ```object``` class.
```python
dir(object)
```
In particular ```__init__``` is a method of ```object```.


   
