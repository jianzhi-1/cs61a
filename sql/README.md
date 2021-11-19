# SQL Guide

### SELECT

```sql
SELECT [columns] FROM [table] WHERE [condition] ORDER BY [order];
```
##### General
```sql
SELECT * FROM table;
SELECT artist, title FROM songs;
SELECT artist AS singer, title AS song_title FROM songs;
SELECT title, views * 100000 FROM songs;
```

##### Ordering ```ORDER BY```
```sql
SELECT a, b FROM table ORDER BY a DESC;
SELECT a, b FROM table ORDER BY b ASC;
SELECT a, b FROM table ORDER BY a DESC, b ASC;
```

##### Conditional ```WHERE```
```sql
SELECT a FROM table WHERE b = "jz";
SELECT a FROM table WHERE b > 2022;
SELECT a FROM table WHERE b > 2022 and c = "jz";
```

### CREATE

##### Common
```sql
CREATE TABLE table (col1 TEXT, col2 INTEGER);
```

(edit below)
```sql
CREATE TABLE table (
  col1 INTEGER PRIMARY KEY, ...
  col1 TEXT, 
  col2 INTEGER
);
```

##### From ```SELECT```
```sql
CREATE TABLE table AS SELECT a, b FROM maintable;
```

##### From UNION
```sql
CREATE TABLE table AS SELECT "jz" AS a, 22 AS b;
```

```sql
CREATE TABLE table AS 
  SELECT "jz" AS a, 22 AS b UNION
  SELECT "jz2" AS a, 23 AS b UNION
  SELECT "jz3" AS a, 24 AS b;
```

### INSERT
```sql
INSERT INTO table VALUES ("JZ", 22);
```

### UPDATE


### DELETE

### JOIN


