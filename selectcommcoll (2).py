import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
idm=None
n=None
a=None
def selectcommerscollege(idm,n,a):
                print("chose any one college from the following \n1)ST STEPHEN'S COLLEGE\n2)HINDU COLLEGE \n3)MIRANDA HOUSE\n4)MADRAS CHRISTIAN COLLEGE\n5)ST XAVIER'S COLLEGE ")
                coll=input("Enter your college name: ").upper()
                sql="insert into commerscollege(aadhar_number,rollnumber,nameofstudent,collegename) values (%s,%s,%s,%s)"
                values=(idm,n,a,coll)
                mycursor.execute(sql,values)
                mydb.commit()
#selectcommerscollege(idm,n,a)
