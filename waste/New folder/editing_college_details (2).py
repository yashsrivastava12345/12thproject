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
                sql="update pcmcollege set course_name = %s where aadhar_number=%s"
                print("chose any one college from the following \n1)IIT MUMBAI \n2)IIT KANPUR \n3)IIT DELHI \n4)IIT GUWAHATI \n5)IIT INDORE \n6)IIIT KOTA \n7)IIIT PUNE \n8)IIIT NAGPUR \n9)IIIT MANIPUR \n10)IIIT RACHI")
                o=input("Enter course name\n>>>")
                value=(o,idm)
                pass
elif cho=="PCB":
                sql="update pcbcollege set course_name = %s where aadhar_number=%s"
                print("chose any one college from the following \n1)ALL INDIA INSTITUTE OF MEDICAL SCIENCE \n2)CHRISTIAN MEDICAL COLLEGE \n3)BANARAS HINDU UNIVERSITY \n4)St. John's Medical college \n5)MAULANA AZAD MEDICAL COLLEGE ")
                o=input("Enter course name\n>>>")
                value=(o,idm)
                pass
elif cho=="COMMERS":
                sql="update commerscollege set course_name = %s where aadhar_number=%s"
                print("chose any one college from the following \n1)ST STEPHEN'S COLLEGE\n2)HINDU COLLEGE \n3)MIRANDA HOUSE\n4)MADRAS CHRISTIAN COLLEGE\n5)ST XAVIER'S COLLEGE ")
                o=input("Enter course name\n>>>")
                value=(o,idm)
                pass
else:
                print("Wrong choice of stream!\nPlease restart!!!!!")
                pass
mycursor.execute(sql,values)
mydb.commit()
