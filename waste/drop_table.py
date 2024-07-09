import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",passwd="")
mycursor=mydb.cursor()
sql="drop database carrer_objective"
mycursor.execute(sql)
mydb.commit()
print("table deleted")
