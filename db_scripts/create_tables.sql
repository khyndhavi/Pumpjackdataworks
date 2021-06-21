create table Employee
(
id  int AUTO_INCREMENT,
first_name text,
last_name text,
salary numeric,
department_id int,
primary key(id),
key(department_id)
);

create table department
(
id int AUTO_INCREMENT,
department_name text,
salary_increment numeric,
primary key(id)
);