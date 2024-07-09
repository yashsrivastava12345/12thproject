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
                print("chose any one course from the following  \n1)MBBS \n2)BDS\n3)PHARM D\n4)B Sc\n5)BAMS")
                o=input("Enter course name\n>>>")
                value=(o,idm)
                pass
elif cho=="COMMERS":
                sql="update commerscourse set course_name = %s where aadhar_number=%s"
                print("chose any one course from the following  \n1)CMA\n2)C A\n3)B.Com\n4)BBA\n5)BMS")
                o=input("Enter course name\n>>>")
                value=(o,idm)
                pass
else:
                print("Wrong choice of stream!\nPlease restart!!!!!")
                pass
mycursor.execute(sql,values)
mydb.commit()
