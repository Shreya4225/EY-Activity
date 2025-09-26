# SchoolDB SQL Script
## Creating a database
```sql
CREATE DATABASE SchoolDB;
USE SchoolDB;
```
## Creating a table
```sql
CREATE TABLE Students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  age INT,
  course VARCHAR(50),
  marks INT
);
```

## Inserting 1 value
```sql
INSERT INTO Students (name, age, course, marks)
VALUES ('Rahul', 21, 'AI', 85);
```
## Inserting multiple values
```sql
INSERT INTO Students (name, age, course, marks)
VALUES ('Priya', 21, 'ML', 90),
       ('Arjun', 20, 'Data Science', 78);
```

```sql
SELECT * FROM Students;
```

-- CRUD Operations
## Selecting specific values
```sql
SELECT marks, name FROM Students;
SELECT marks, name FROM Students WHERE marks > 80;
```
## Updating
```sql
UPDATE Students
SET marks = 100, age = 25
WHERE id = 2;
```
SELECT * FROM Students;

## Deleting
```sql
DELETE FROM Students WHERE id = 3;
```

SELECT * FROM Students;
