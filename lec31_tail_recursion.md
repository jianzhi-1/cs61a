# Tail Recursion

Lexical (static) scope: The parent of the frame is the frame in which the procedure was defined.

Dynamic scope: The parent of the frame in which a procedure was called.
Scheme uses the ```mu``` special form for dynamic scoping.

### Mu
```lisp
(define f (mu (x) (+ x y)))
(define g (lambda (x y) (f (+ x y))))
```

Remark: this is about the look up rule (changing the parent of a frame), not about nonlocal.
Sets the parent to where it was called.

Tail recursion only needs constant number of frames.

In a tail recursive function, every recursive call must be a tail call. (i.e. no additional computation; no need to wait for return value)
- The last body sub-expression in a ```lambda``` expression
- Sub-expression 2 and 3 in a tail-context ```if``` expression
- All non-predicate sub-expressions in a tail context ```cond```
- The last sub-expression in a tail context ```and```, ```or```, ```begin``` or ```let```

Linear recursive procedures can be rewritten to use tail calls (use additional parameter as memoization).

For example:
```lisp
(define (length s)
  (if (null? s) 0
  (+ 1 (length (cdr s)))))
```

```lisp
(define (length-tail s)
  (define (length-iter s n)
    (if (null? s) n
    (length-iter (cdr s) (+ 1 n))))
  (length-iter s 0))
```

Bottom line: consider the last operation of the frame. It must be the recursive function **ONLY**.

### Trampolining
Thunk: an expression wrapped in an argument-less function, which supports lazy evaluation
```python
thunk = lambda: 2 * (3 + 4)
thunk = lambda: add(2, 4)
```
Trampoline: a loop that iteratively invokes thunk-returning functions
```python
def trampoline(f, *args):
  v = f(*args)
  while callable(v):
    v = v()
  return v
```

```python
def factorial(n, k):
  if (n == 0): return k
  return lambda: factorial(n - 1, k * n)
```

```python
trampoline(factorial, 3, 1)
```

Returning a thunk allows Python to close the frame.
