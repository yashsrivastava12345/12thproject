import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
im=None
k=None
q=None
def selectpcmcollege(im,k,q):
           
                print("chose any one college from the following \n1)IIT MUMBAI \n2)IIT KANPUR \n3)IIT DELHI \n4)IIT GUWAHATI \n5)IIT INDORE \n6)IIIT KOTA \n7)IIIT PUNE \n8)IIIT NAGPUR \n9)IIIT MANIPUR \n10)IIIT RACHI")
                coll=input("Enter your college name: ").upper()
                sql="insert into pcmcollege(aadhar_number,rollnumber,nameofstudent,collegename) values (%s,%s,%s,%s)"
                values=(im,k,q,coll)
                mycursor.execute(sql,values)
                mydb.commit()
#selectpcmcollege(im,k,q)
