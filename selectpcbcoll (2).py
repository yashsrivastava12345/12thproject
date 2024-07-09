import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
idm=None
n=None
a=None
def selectpcbcollege(idm,n,a):
                print("chose any one college from the following \n1)ALL INDIA INSTITUTE OF MEDICAL SCIENCE \n2)CHRISTIAN MEDICAL COLLEGE \n3)BANARAS HINDU UNIVERSITY \n4)St. John's Medical college \n5)MAULANA AZAD MEDICAL COLLEGE ")
                coll=input("Enter your college name: ").upper()
                sql="insert into pcbcollege(aadhar_number,rollnumber,nameofstudent,collegename) values (%s,%s,%s,%s)"
                values=(idm,n,a,coll)
                mycursor.execute(sql,values)
                mydb.commit()
#selectpcbcollege(idm,n,a)
