# Scheme

### Primitive Types


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
(define (<name> [param] ...) <body>
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





[Link to 61A Scheme](https://cs61a.org/articles/scheme-spec/#special-forms-2)
