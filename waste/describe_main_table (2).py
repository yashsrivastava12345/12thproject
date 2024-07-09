import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database = "carrer_objective")
mycursor=mydb.cursor()
sql="describe carrerobjective"
mycursor.execute(sql)
for i in mycursor:
    print(i)
