# Lab 10/13

### Python Look Up Rule

- No overloading of methods, even if arguments are different.
- For variable selection:
  - Checks instance in dict
  - Checks class in dict (go up the hierarchy)
  - Errors if neither exists
- For overriding of methods:
  - Find the instance of self (king)
  - Check if current instance has method
  - If not, go up the hierarchy
- If two methods with same name, the last defined one wins.


Treat Python objects as a big dictionary.
As long as f() exists in self instance, it is allowed.

class Ant:
    def f(self):
        self.smash() # this works for BigAnt instance

class BigAnt(Ant):
    def smash(self):
        print("smash")

x = BigAnt()
x.f() # this is fine

### Magic
- __add__: +
- __get__: obj[key]
- __dict__: returns a dict of all instance variables

Not possible to edit a class variable through an instance. Assigning self.color always assigns the instance variable.

yield from
