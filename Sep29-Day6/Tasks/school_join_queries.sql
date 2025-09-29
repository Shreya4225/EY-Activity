CREATE database school;
use school

create table teachers(
teacher_id int auto_increment primary key,
name varchar(50),
subject_id int
);

create table subjects(
subject_id int auto_increment primary key,
subject_name varchar(50)
);

INSERT INTO subjects (subject_name) VALUES
('Mathematics'),   -- id = 1
('Science'),       -- id = 2
('English'),       -- id = 3
('History'),       -- id = 4
('Geography');     -- id = 5 (no teacher yet)

INSERT INTO teachers (name, subject_id) VALUES
('Rahul Sir', 1),   -- Mathematics
('Priya Madam', 2), -- Science
('Arjun Sir', NULL),-- No subject assigned
('Neha Madam', 3);  -- English

select * from teachers

select s.subject_name, t.name, t.teacher_id
from subjects s
LEFT JOIN teachers t on s.subject_id = t.subject_id

select s.subject_name, t.name, t.teacher_id
from subjects s
RIGHT JOIN teachers t on s.subject_id = t.subject_id

select s.subject_name, t.name, t.teacher_id
from subjects s
LEFT JOIN teachers t on s.subject_id = t.subject_id
UNION
select s.subject_name, t.name, t.teacher_id
from subjects s
RIGHT JOIN teachers t on s.subject_id = t.subject_id

select s.subject_name, t.name, t.teacher_id
from subjects s
INNER JOIN teachers t on s.subject_id = t.subject_id