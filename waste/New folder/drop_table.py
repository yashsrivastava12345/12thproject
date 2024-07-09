import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
sql="drop table carrerobjective"
mycursor.execute(sql)
mydb.commit()
print("table deleted")
