import mysql.connector as mysql
mydb = mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
mycursor.execute("create table carrerobjective(aadhar_number char(26) primary key not null,nameofstudent char(26) not null ,fathersname char(26) not null,mothersname char(26) not null,housenumber char(32) not null,colony char(32) not null,city char(26) not null,state char(32) not null,pincode int(11),mobilenumber varchar(50) not null,Email varchar(70),schoolname char(45) not null,class12passingyear date not null,stream char(26) not null)")
print ("table created") 

