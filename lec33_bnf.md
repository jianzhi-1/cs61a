# Backus-Naur Form

```lark
symbol0: symbol1 symbol2 ... symboln
```

Symbols represent sets of strings and can be non-terminal or terminal.
Non-terminal symbols can expand into either non-terminal symbols or terminals.
Terminals are like tokens.

```lark
?start: numbers
numbers: INTEGERS | numbers "," INTEGER
INTEGERS: /-?\d+/
```

In the above, ```INTEGERS``` is defined by regular expressions.

For the Lark library, grammars need to start with a ```start``` symbol. Non-terminal symbol names written in lower-case. Terminal symbols are written in upper-case.

The line below ignores whitespaces between symbols, but not in the sense of stripping the whitespaces away.
```lark
%ignore /\s+/
```

```lark
?start: sentence
noun: NOUN
noun_phrase: article noun
article: | ARTICLE
verb: VERB
NOUN: "horse" | "dog" | "hamster"
ARTICLE: "a" | "the"
VERB: "stands" | "walks" | "jumps"
```

In the above example, the article can be ```None```.

### EBNF
Extended version of BNF.

```items*```: Zero or more items, i.e. optional
```item+```: 
```item?```: Zero or one item.

### Grouping
```
NAME: /\w+/
NUMBER: /\d+/
list: ( name | number )+
comma_separated_list: [ NAME ("," NAME)* ]
```

### Predefined 
```lark
%import common.NUMBER
```

### Calculator
```
?start: calc_expr
?calc_expr: NUMBER | calc_op
calc_op: "(" OPERATOR calc_expr* ")"
OPERATOR: "+" | "-" | "*" | "/"

%ignore /\s+/
%import common.NUMBER
```

The ```?``` means not to display it in the parse tree.

### Ambiguity Resolving
Just fix the order of your expressions. Put the higher priority one in front.
