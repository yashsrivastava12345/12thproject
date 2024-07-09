import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
a=None
def view_form_of_pcm_course(a):
                sql="select * from pcmcourse where aadhar_number=%s "
                value=(a,)
                mycursor.execute(sql,value)
                myresult=mycursor.fetchall()
                for i in myresult:
                                print(i)
                                
