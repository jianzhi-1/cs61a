# Backus-Naur Form

### Syntax

### Examples

1. Symmetric bracket sequences
```lark
start: symmetric
symmetric: | "(" symmetric ")"
```

2. Balanced bracket sequences
```lark
start: correct
correct: | "(" correct ")" correct
```
