create database hospital;
use hospital;

create table patients(
patient_id INT PRIMARY KEY,
name VARCHAR(50),
age INT,
gender CHAR(1),
city VARCHAR(50)
);

create table doctors(
doctor_id INT PRIMARY KEY,
name VARCHAR(50),
specialization VARCHAR(50),
experience INT
);

create table appointments(
appointment_id INT PRIMARY KEY,
patient_id int,
doctor_id int,
appointment_date DATE,
status VARCHAR(20),
foreign key(patient_id) references patients(patient_id),
foreign key(doctor_id) references doctors(doctor_id)
);

create table medicalrecords(
record_id INT PRIMARY KEY,
patient_id int,
doctor_id int,
foreign key(patient_id) references patients(patient_id),
foreign key(doctor_id) references doctors(doctor_id),
diagnosis VARCHAR(100),
treatment VARCHAR(100),
date DATE
);

create table billing(
bill_id INT PRIMARY KEY,
patient_id int,
foreign key(patient_id) references patients(patient_id),
amount DECIMAL(10,2),
bill_date DATE,
status VARCHAR(20)
);

INSERT INTO patients VALUES
(1, 'Amit Sharma', 30, 'M', 'Delhi'),
(2, 'Priya Verma', 25, 'F', 'Mumbai'),
(3, 'Rahul Singh', 40, 'M', 'Chennai'),
(4, 'Sneha Reddy', 35, 'F', 'Hyderabad'),
(5, 'Vikram Joshi', 50, 'M', 'Bangalore'),
(6, 'Neha Kapoor', 28, 'F', 'Kolkata'),
(7, 'Ravi Mehta', 45, 'M', 'Ahmedabad'),
(8, 'Anjali Nair', 32, 'F', 'Pune'),
(9, 'Karan Malhotra', 38, 'M', 'Jaipur'),
(10, 'Divya Iyer', 29, 'F', 'Coimbatore');

INSERT INTO doctors VALUES
(1, 'Dr. Rajiv Menon', 'Cardiology', 15),
(2, 'Dr. Meera Das', 'Orthopedics', 10),
(3, 'Dr. Arjun Patel', 'Pediatrics', 8),
(4, 'Dr. Kavita Rao', 'Dermatology', 12),
(5, 'Dr. Sanjay Gupta', 'Neurology', 20);

INSERT INTO appointments VALUES
(1, 1, 1, '2025-09-01', 'Completed'),
(2, 2, 2, '2025-09-02', 'Scheduled'),
(3, 3, 1, '2025-09-03', 'Completed'),
(4, 4, 3, '2025-09-04', 'Cancelled'),
(5, 5, 4, '2025-09-05', 'Completed'),
(6, 6, 5, '2025-09-06', 'Scheduled'),
(7, 7, 1, '2025-09-07', 'Completed'),
(8, 8, 2, '2025-09-08', 'Scheduled'),
(9, 9, 3, '2025-09-09', 'Completed'),
(10, 10, 1, '2025-09-10', 'Scheduled');

INSERT INTO medicalrecords VALUES
(1, 1, 1, 'Hypertension', 'Medication A', '2025-09-01'),
(2, 3, 1, 'Arrhythmia', 'Medication B', '2025-09-03'),
(3, 7, 1, 'Chest Pain', 'ECG & Medication', '2025-09-07'),
(4, 5, 4, 'Acne', 'Topical Cream', '2025-09-05'),
(5, 9, 3, 'Fever', 'Paracetamol', '2025-09-09');

INSERT INTO billing VALUES
(1, 1, 1500.00, '2025-09-01', 'Paid'),
(2, 2, 1200.00, '2025-09-02', 'Unpaid'),
(3, 3, 1800.00, '2025-09-03', 'Paid'),
(4, 4, 1000.00, '2025-09-04', 'Unpaid'),
(5, 5, 1300.00, '2025-09-05', 'Paid'),
(6, 6, 1600.00, '2025-09-06', 'Unpaid'),
(7, 7, 1700.00, '2025-09-07', 'Paid'),
(8, 8, 1100.00, '2025-09-08', 'Unpaid'),
(9, 9, 900.00, '2025-09-09', 'Paid'),
(10, 10, 1400.00, '2025-09-10', 'Unpaid');

-- task 1
select p.name, d.specialization
from patients p
join appointments a on a.patient_id= p.patient_id
join doctors d on d.doctor_id= a.doctor_id
where d.specialization = 'Cardiology';
-- task2
select * from appointments a
where a.patient_id=1;

delimiter $$
create procedure get_appointment(IN patient_data int)
begin
select * from appointments a
where a.patient_id=patient_data;
end$$

delimiter ;

call get_appointment(1)

-- task3
select * from billing b
where b.status='unpaid';

-- task 4
delimiter $$
create procedure GetPatientHistoryy(IN patient_id int)
begin
select a.appointment_date, m.diagnosis, m.treatment, m.patient_id
from appointments a
join medicalrecords m on a.patient_id= m.patient_id;
end $$

delimiter ;

call GetPatientHistoryy(1)

-- task 5
delimiter $$
create procedure GetDoctorAppointments(IN doctor_id int)
begin
select a.appointment_date, m.diagnosis, m.treatment, m.doctor_id
from appointments a
join medicalrecords m on a.patient_id= m.patient_id;
end $$

delimiter ;

call GetPatientHistoryy(1)