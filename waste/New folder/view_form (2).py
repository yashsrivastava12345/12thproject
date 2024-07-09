import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
def view_of_form():
                idc=input("Enter your aadhar number :")
                print("Enter PCM to view Engeniring students, PCB to view medical students and  COMMERS to view Commersial students")
                st=input("Enter your stream : ").upper()
                if len(idc)<=12 and len(idc) != " ":
                                print("Check your details")
                                sql1="select * from carrerobjective where aadhar_number=%s "
                                value=(idc,)
                                mycursor.execute(sql1,value)
                                myresult = mycursor.fetchall()
                                for x in myresult:
                                                print(x)
                                                pass
                                if st=="PCM":
                                                print("Check your college details")
                                                import viewpcmcollege as vp
                                                vp.view_form_of_pcm(idc)
                                                print("check your details of courses you selected")
                                                import viewpcmcourse as vc
                                                vc.view_form_of_pcm_course(idc)
                                                pass
                                elif st=="PCB":
                                                print("Check your college details")
                                                import viewpcbcollege as vb
                                                vb.view_form_of_pcb(idc)
                                                print("check your details of courses you selected")
                                                import viewpcbcourse as vcb
                                                vcb.view_form_of_pcb_course(idc)
                                                pass
                                elif st=="COMMERS":
                                                print("Check your college details")
                                                import viewcommerscollege as vcr
                                                vcr.view_form_of_commers(idc)
                                                print("check your details of courses you selected")
                                                import viewcommerscourse as vcc
                                                vcc.view_form_of_commers_course(idc)
                                                pass
                                else:
                                                print("WRONG CHOICE !!!!!!!!!")
                                                pass
                                pass
                else:
                                print("Invalid aadhar number ! \nPlease restart !!!")
