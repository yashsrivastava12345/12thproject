import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
def view_of_form():
                idc=input("Enter your aadhar number :")
                print("Enter PCM to view Engeniring students, PCB to view medical students and  COMMERS to view Commersial students")
                st=input("Enter your stream :").upper()
                if st=="PCM":
                                sql="select co.* , collegename from carrerobjective co , pcmcollege pm where rollnumber= %s"
                                val=(idc)
                                mycursor.execute(sql,val)
                                pass
                elif st=="PCB":
                                sql="select co.* , collegename from carrerobjective co , pcbcollege pb where rollnumber= %s"
                                val=(idc)
                                mycursor.execute(sql,val)
                                pass
                elif st=="COMMERS":
                                sql="select co.* , collegename from carrerobjective co , commerscollege cc where rollnumber= %s"
                                val=(idc)
                                mycursor.execute(sql,val)
                                pass
                else:
                                print("Wrong input")
                                pass
                myresult = mycursor.fetchall()
                for x in myresult:
                                print(x)
view_of_form()
