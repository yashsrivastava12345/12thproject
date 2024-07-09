import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
print("enter names of cources to edit the details")
idm=input("Enter your aadhar card number")
values=None
sql=""
cho=input("Enter your streanm as \nPCM\nPCB\nCOMMERS\n>>>").upper()
if cho=="PCM":
                sql="update pcmcourse set course_name = %s where aadhar_number=%s"
                print("chose any one course from the following  \n1) B Tech \n 2)BTech in computer science \n3)B Sc \n4) B E\n5)B.Arch \n6)chemical Engenering")
                o=input("Enter course name\n>>>")
                value=(o,idm)
                pass
elif cho=="PCB":
                sql="update pcbcourse set course_name = %s where aadhar_number=%s"
                print("chose any one course from the following  \n1)B pharma \n2)B BA\n3)B Sc\n4)M Sc\n5)B A")
                o=input("Enter course name\n>>>")
                value=(o,idm)
                pass
elif cho=="COMMERS":
                sql="update commerscourse set course_name = %s where aadhar_number=%s"
                print("chose any one course from the following  \n1)B A\n2C A)\n3)Management\n4)Banking\n5)Enterpeniure")
                o=input("Enter course name\n>>>")
                value=(o,idm)
                pass
else:
                print("Wrong choice of stream!\nPlease restart!!!!!")
                pass
mycursor.execute(sql,values)
mydb.commit()
