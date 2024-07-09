import mysql.connector as mysql
mydb = mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
mycursor.execute("create table pcmcourse(aadhar_number char(26) primary key not null,rollnumber char(13) not null,nameofstudent char(26) not null ,course_name char(45) not null)")
#mycursor.execute("create table pcbcourse(aadhar_number char(26) primary key not null,rollnumber char(13) not null,nameofstudent char(26) not null ,course_name char(45) not null)")
#mycursor.execute("create table commerscourse(aadhar_number char(26) primary key not null,rollnumber char(13) not null,nameofstudent char(26) not null ,course_name char(45) not null)")
print ("tables created") 
