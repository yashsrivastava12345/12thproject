import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
im=None
k=None
q=None
def selectpcmcourse(im,q):           
                print("chose any one course from the following  \n1) B Tech \n 2)BTech in computer science \n3)B Sc \n4) B E\n5)B.Arch \n6)chemical Engenering")
                coll=input("Enter your course name: ").upper()
                sql="insert into pcmcourse(aadhar_number,nameofstudent,course_name ) values (%s,%s,%s)"
                values=(im,q,coll)
                mycursor.execute(sql,values)
                mydb.commit()
