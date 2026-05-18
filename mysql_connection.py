import pymysql as sql
# CURD -> Create,Read,Update,Delete
db = sql.connect(user="root",host="localhost",port=3306,password="root",database="kasi_tech")
cur = db.cursor()
# cur.execute(""" create database kasi_tech """)
# cur.execute(""" create table emp(id int,name varchar(50),dept varchar(50),salary int) """)
# cur.execute(""" insert into emp values(2,"Suriya","Developer",55000) """)
# cur.execute(""" insert into emp values(3,"Sanjay","AI",50000) """)
# cur.execute(""" insert into emp values(4,"Praveen","MECH",65000) """)
# cur.execute(""" insert into emp values(1,"Kumar","ECE",95000) """)
# cur.execute(""" insert into emp values(1,"Jai","Hr",75000) """)
# cur.execute(" update emp set id = 5 where name='Kumar' ")
# cur.execute(" update emp set id = 6 where dept='Hr' ")
# cur.execute(""" delete from emp where name = "Suriya" """)
# cur.execute(""" delete from emp where name = "Sanjay" """)

# table column level changes --> alter
# alter table table_name rename column current_column to new_name;
# cur.execute(""" alter table emp rename column  dept to department""")
# alter table table_name add column new_column_name datatype;
# cur.execute(""" alter table emp add column  phone int """)
# cur.execute(""" alter table emp drop column  phone """)

# cur.execute(""" select * from emp """)
# all_data = cur.fetchall()
# print(all_data)
# for i in all_data:
#     print(i)

# cur.execute(""" select * from emp where id = 5 """)
# user_data = cur.fetchone()
# print(user_data)
# for i in user_data:
#     print(i)
# data = ("Emp id","Name","Dept","Salary")
# for i in range(len(user_data)):
#     print(data[i]," : ",user_data[i])

db.commit()
db.close()
# print("column name changed")
