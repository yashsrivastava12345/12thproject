import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
im=None
k=None
q=None
def selectcommerscourse(im,q):           
                print("chose any one course from the following  \n1)CMA\n2)C A\n3)B.Com\n4)BBA\n5)BMS")
                coll=input("Enter your course name: ").upper()
                sql="insert into commerscourse(aadhar_number,nameofstudent,course_name ) values (%s,%s,%s,%s)"
                values=(im,q,coll)
                mycursor.execute(sql,values)
                mydb.commit()
