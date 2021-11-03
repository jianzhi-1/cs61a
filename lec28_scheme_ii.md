# Lecture 28 Notes: Scheme II

```lisp
scm> (define b 4)
b

scm> '(a ,(+ b 1))
(a (unquote (+ b 1)))

scm> '(a ,(+ b 1) a)
(a 5 a)
```

### Eval
```lisp
scm> (eval (make-adder 5))
(lambda (d) (+ d 5))
scm> ( (make-adder 5) 4)
```

### Exceptions
If an exception is not handled, program stops running completely.
```python3
try:
  <try suite>
except <exception class> as <name>:
  <except suite>
```

The \<try suite> is executed first. If during the course of executing, an exception that inherits from \<exception class> is raised, then the \<except suite> is executed, with \<name> bound to the exception.

### Assert
```python3
assert x != 0, "no zero"
```
  
