import mysql.connector as mysql
mydb = mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
mycursor.execute("create table PCMcollege(id char(26) primary key not null,rollnumber char(13) not null,nameofstudent char(26) not null ,collegename char(45) not null)")
#mycursor.execute("create table PCbcollege(id char(26) primary key not null,rollnumber char(13) not null,nameofstudent char(26) not null ,collegename char(45) not null)")
#mycursor.execute("create table COMMERScollege(id char(26) primary key not null,rollnumber char(13) not null,nameofstudent char(26) not null ,collegename char(45) not null)")
print ("tables created") 
