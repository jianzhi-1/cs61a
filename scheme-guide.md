# Scheme Guide
Here we go again!

### Getting Started
- Starting
```shell
$ python3 scheme
```
- Exiting
```lisp
scm> (exit)
```
- Commenting
```lisp
; this is a comment
```

### Primitive Types

##### Boolean
```lisp
scm> #t
#t
scm> #f
#f
scm> true
#t
scm> false
#f
```

### Operations
```lisp
scm> (+ 1 2 3 4)
10

scm> (/ 36 2 2)
9

scm> (= 1 2)
#f

scm> (< 1 2)
#t

scm> (or 1 #t)
1

scm> (and 1 #f #t)
#f

scm> (not #f)
#t
```

### Call Exceptions / Procedures
```( <operator> <arg1> <arg2> ... <argn>)```
Lisp evaluates all operands, unless the operator is a special form.

##### Common
```lisp
scm> (modulo 42 2)
4

scm> (quotient 101 10)
10

scm> (even? 10)
#t

scm> (print 1)
1

scm> (null? nil)
#t
```

##### Special Forms
Consists of ```if```, ```and```, ```or```, ```lambda```, ```define``` and more...

1. ```if```
Only evaluates one of operands
```lisp
(if <predicate> <if-true> [if-false])
```
2. ```cond```
```lisp
(cond
    (<p1> <e1>)
    (<p2> <e2>)
    ...
    (<pn> <en>)
    [(else <else-expression>)])
```
Example
```lisp
(cond
    ((< a b) 3)
    ((= a b) 5)
    ((> a b) 7))
```

```lisp
(cond
    ((< a b) 1)
    ((= a b) 2)
    (else 7))
```


3. ```define```
Operands of ```define``` are not evaluated at all.
```lisp
(define <name> <expression>)
(define (<name> <param1> <param2> ...) <body> )
```

Example:
```lisp
scm> (define a 5)
a

scm> (define (add1 x) (+ x 1))
add1
```

Lisp on Procedures will evaluate all of its operands first!

```lisp
scm> (define x 3)
x
```



4. lambda
All Scheme procedures are lambda procedures.
Returns the last expression in the ```<body>```.
```lisp
(lambda (<param1> <param2> ...) <body>)
```

Example:
```lisp
(define (mult num) 
    (lambda (num2) (- num num2))
)
```

### Applications
##### Higher Order Functions
Given *f, g*, return *g ∘ f*.
```lisp
(define (composed f g) 
    (lambda (x) (f (g x)))
)
```


### List

```lisp
scm> nil
()
```

```lisp
scm> (define a (list 1 2 3 4 5))
(1 2 3 4 5)
scm> (cons 1 (cons 2 (cons 3 (cons 4 (cons 5 nil)))))
(1 2 3 4 5)
```

- Note: the second argument of cons **MUST** be either a pair or nil
- Otherwise will result in *improper list* i.e. the second argument is a primitive
- Many methods (like ```length```) will not work
```lisp
scm> (cons 1 2)
(1 . 2)
```

##### Methods on List
1. ```car```

```lisp
scm> (car a)
1
```
2. ```cdr```
```
scm> (cdr a)
(2 3 4 5)

scm> (cdr '(1 (2 3)))
((2 3))
```

3. ```length```
```lisp
scm> (null? nil)
#t
scm> (append '(1 2 3) '(4 5 6)))
(1 2 3 4 5 6)
scm> (length '(1 2 3 4 5))
5
```

4. ```append```

### Extras
- filter
returns a list consisting of only elements that return ```#t``` on pred (one argument function).
```lisp
(filter <pred> <lst>)
```

### Tricks
- ```()``` is interchangeable with ```[]```

### Unresolved Questions
Question what does print return? is there a none in scheme? is none falsy i dont think so
What is ```scm> (load-all ".")```?





