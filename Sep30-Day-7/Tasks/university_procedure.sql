CREATE DATABASE UniversityDB;
USE UniversityDB;
-- Students Table
CREATE TABLE Students (
student_id INT PRIMARY KEY,
name VARCHAR(50),
city VARCHAR(50)
);
-- Courses Table
CREATE TABLE Courses (
course_id INT PRIMARY KEY,
course_name VARCHAR(50),
credits INT
);
-- Enrollments Table
CREATE TABLE Enrollments (
enroll_id INT PRIMARY KEY,
student_id INT,
course_id INT,
grade CHAR(2),
FOREIGN KEY (student_id) REFERENCES Students(student_id),
FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);
-- Insert Students
INSERT INTO Students VALUES
(1, 'Rahul', 'Mumbai'),
(2, 'Priya', 'Delhi'),
(3, 'Arjun', 'Bengaluru'),
(4, 'Neha', 'Hyderabad'),
(5, 'Vikram', 'Chennai');
-- Insert Courses
INSERT INTO Courses VALUES
(101, 'Mathematics', 4),
(102, 'Computer Science', 3),
(103, 'Economics', 2),
(104, 'History', 3);
-- Insert Enrollments
INSERT INTO Enrollments VALUES
(1, 1, 101, 'A'),
(2, 1, 102, 'B'),
(3, 2, 103, 'A'),
(4, 3, 101, 'C'),

(5, 4, 102, 'B'),
(6, 5, 104, 'A');

delimiter $$
create procedure get_studss_name()
begin
select s.name 
from students s;
end$$
delimiter ;

call get_studss_name();

delimiter $$
create procedure get_course_name()
begin
select c.course_name 
from Courses c;
end$$
delimiter ;

call get_course_name();

delimiter $$
create procedure get_stud_city(IN s_city varchar(50))
begin
select s.name 
from Students s 
where s.city=s_city ;
end$$
delimiter ;

call get_stud_city('Mumbai');

delimiter $$
create procedure get_stud_course()
begin
select s.name, c.course_name
from Students s
join Enrollments e on s.student_id = e.student_id
join Courses c on c.course_id= e.course_id;
end$$

delimiter ;

call get_stud_course();

delimiter $$
create procedure get_stud_per_course(IN output_course_id int)
begin
select s.name, c.course_name
from Students s
join Enrollments e on s.student_id = e.student_id
join Courses c on c.course_id= e.course_id
where c.course_id=output_course_id;
end$$

delimiter ;

call get_stud_per_course(101);

delimiter $$
create procedure stud_count()
begin
select c.course_name, count(s.student_id) as student_count
from Students s
join Enrollments e on s.student_id = e.student_id
join Courses c on c.course_id= e.course_id
group by(c.course_name);
end$$

delimiter ;

call stud_count();

delimiter $$
create procedure get_studs_course_grade()
begin
select s.name, c.course_name, e.grade
from Students s
join Enrollments e on s.student_id = e.student_id
join Courses c on c.course_id= e.course_id;
end$$

delimiter ;

call get_studs_course_grade();

delimiter $$
create procedure get_studs_courses(IN stud_name varchar(50))
begin
select s.name, c.course_name
from Students s
join Enrollments e on s.student_id = e.student_id
join Courses c on c.course_id= e.course_id
where s.name=stud_name;
end$$

delimiter ;

call get_studs_courses('Rahul');

