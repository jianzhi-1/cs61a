# SQL Guide

### SELECT

```sqlite
SELECT [columns] FROM [table] WHERE [condition] ORDER BY [order];
```
##### General
```sqlite
SELECT * FROM table;
SELECT artist, title FROM songs;
SELECT artist AS singer, title AS song_title FROM songs;
SELECT title, views * 100000 FROM songs;
```

##### Ordering ```ORDER BY```
```sqlite
SELECT a, b FROM table ORDER BY a DESC;
SELECT a, b FROM table ORDER BY b ASC;
SELECT a, b FROM table ORDER BY a DESC, b ASC;
```

##### Conditional ```WHERE```
```sqlite
SELECT a FROM table WHERE b = "jz";
SELECT a FROM table WHERE b > 2022;
SELECT a FROM table WHERE b > 2022 and c = "jz";
```

### CREATE


### INSERT


### UPDATE


### DELETE

