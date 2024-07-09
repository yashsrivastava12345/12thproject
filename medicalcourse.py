import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
im=None
k=None
q=None
def selectpcbcourse(im,q):           
                print("chose any one course from the following  \n1)MBBS \n2)BDS\n3)PHARM D\n4)B Sc\n5)BAMS")
                coll=input("Enter your course name: ").upper()
                sql="insert into pcbcourse(aadhar_number,nameofstudent,course_name ) values (%s,%s,%s)"
                values=(im,q,coll)
                mycursor.execute(sql,values)
                mydb.commit()
