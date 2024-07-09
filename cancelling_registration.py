import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database = "carrer_objective")
mycursor=mydb.cursor()
sql1="delete from carrerobjective where aadhar_number=%s"
d=input("Enter your aadhar number to cancle your restration \n>>>")
value=(d,)
st=input("Enter your stream\n>>>").upper()
sql2,sql3="",""
if st=="PCM":
                sql2="delete from pcmcollege where aadhar_number=%s"
                sql3="delete from pcmcourse where aadhar_number=%s"
                pass
elif st=="PCB":
                sql2="delete from pcmcollege where aadhar_number=%s"
                sql3="delete from pcmcourse where aadhar_number=%s"
                pass
elif st=="COMMERS":
                sql2="delete from pcmcollege where aadhar_number=%s"
                sql3="delete from pcmcourse where aadhar_number=%s"
                pass
else :
                print("Entered wrong choice !!\n please restart!!!!!!!")
#mycursor.execute(sql1,value)
mycursor.execute(sql2,value)
mycursor.execute(sql3,value)
mydb.commit()
