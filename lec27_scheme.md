# Scheme

### Primitive Types
- ```#t```, ```#f```, ```true```, ```false```


### Special Forms
- define
```lisp
scm> (define x 2)
x
scm> (+ 2 x)
4
scm> (define x (+ 2 2))
x
scm> x
4
```

- define procedure
```lisp
(define (<name> [param] ...) <body>)
```

```lisp
scm> (define (add a b) (+ a b))
add
scm> (add 2 3)
5
scm> (define (average x y) (/ (+ x y) 2))
average
scm> (average 30 60)
45
```

Note you can override built in this way.
A procedure is equivalent to function.

### Conditional
No explicit ```return``` key word.
```lisp
(define x 5)
(if (> x 0) x -x)
```

### Or , And
```lisp
(and (> x 10) (< x 20))
(and (> x 10) (< x 20) x)
(or x (< x -10) (> x 10))
```

Returns the last evaluated value.
Scheme considers all the number values to be true. ```#f``` is the only value that is false.

### Lambda
evaluates to anonymous procedures
```lisp
scm> (lambda (x) (+ x 4))
(lambda (x) (+ x 4))
```

### Begin

### Let Form

### List
Scheme lists are linked lists.
```nil``` is the empty list.
```cons``` must take two arguments.

```lisp
scm> (cons 1 (cons (2 null)))
(1 2)
```

Access
```lisp
(define lst (cons 1 (cons 2 nil)))
(car lst) ; 1
(cdr lst) ; (2)
```

Built in list procedure
```lisp
(list 1 2 3 4)
(list 1 2 (list 3 4) 5)
(list 1 2 (list 3 4) (cons 1 (cons 2 nil) ) )
```

### Symbolic Programming
```lisp
(define a 1)
(define b 2)
(list a b) ; (1 2)
```

```lisp
(list 'a 'b) ; (a, b)
(list 'a b)  ; (a, 2)
(list (quote a) (quote b)) ; (a, b)
```

```lisp
scm> '(a b c)
(a b c)
scm> (car '(a b c))
a
```

Think with the constraint not to have any mutations.

Note that in the above ```a``` is not even defined!

[Link to 61A Scheme](https://cs61a.org/articles/scheme-spec/#special-forms-2)

