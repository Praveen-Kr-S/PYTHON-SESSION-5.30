-- create database db_name;
create database surjith_tech;
-- create table table_name(no of column datatype);
use surjith_tech;
create table emp(name varchar(50),age int,dept varchar(50), salary int);
-- add the data
-- insert into table_name values(datas);
insert into emp values("Kumar",25,"ECE",50000),
("Sujith",23,"CSE",55000),
("Jai Prakash",21,"IT",65000);

-- view the table
-- select columns from table_name;
select * from emp;
-- column wise select
-- select column_names from table_name;
select name,salary from emp;
-- row wise select
-- select * from table_name where column=value;
select * from emp where name="Kumar";
select * from emp where dept="Mech";
select * from emp where age=21;

-- update the data
-- update table_name set column = value where changing_column = value;
set sql_safe_updates = 0;
update emp set salary = 70000 where name = "Praveen";


