# CS 61A
### UC Berkeley Fall 2021, taught by Prof John DeNero and Prof Pamela Fox
This repository is meant to store my lecture/discussion notes, which I think would be nice to share with my peers. I will **not** be uploading anything related to homework or assignments. Please contact me if you feel any file should not be here. Thanks!

### Misc
- General
```shell
$ python3 -i file.py
$ python3 -m doctest lab00.py
```
- Submission
```shell
$ python3 ok
$ python3 ok --submit
```

### Notes
#### Control (09/01 Lab)
- Things that represents False: False, 0, None, [], "", ()
- Short circuiting behavior: 
  - ```and``` short-circuits when it hits a False value. 
  - ```or``` short-circuits when it hits a True value.
- ```not``` always return True or False value
- Order of binding (placing of parenthesis): ```not```, ```and```, ```or```

#### Errors (09/01 Lab)
- ```SyntaxError```
- ```IndentationError```: just use consistent indenting
- ```TypeError```: called function on an operand that wasn't the correct type
- ```ZeroDivisionError```: 1/0
