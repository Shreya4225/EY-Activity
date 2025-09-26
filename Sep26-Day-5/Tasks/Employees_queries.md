```sql
CREATE EMPLOYEES TABLE
CREATE TABLE Employees(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
age INT,
department VARCHAR(50),
salary DECIMAL(10,2)
)
```

```sql
INSERT INTO Employees(name, age, department, salary)
VALUES 
('Shreya', 22, 'consultancy', 2000000),
('Prajakta', 23, 'Tax', 1500000),
('Anushka', 24, 'assurance', 1300000),
('Rohit', 25, 'AI', 1700000);
```

```sql
SELECT *  from Employees
```

```sql
SELECT name, department FROM Employees
```

```sql
SELECT name, department FROM Employees where department='consultancy'
```

```sql
UPDATE Employees
SET department='AI&DS'
WHERE id=4
```

```sql
DELETE from Employees WHERE id=4
```
