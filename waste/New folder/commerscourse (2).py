import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
im=None
k=None
q=None
def selectcommerscourse(im,k,q):           
                print("chose any one course from the following  \n1)B A\n2C A)\n3)Management\n4)Banking\n5)Enterpeniure")
                coll=input("Enter your course name: ").upper()
                sql="insert into commerscourse(aadhar_number,rollnumber,nameofstudent,course_name ) values (%s,%s,%s,%s)"
                values=(im,k,q,coll)
                mycursor.execute(sql,values)
                mydb.commit()
