import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
def fill_form(x):
                idm=input("Enter your aadhar number: ")
                a=input("Enter student's name : ").upper()
                b=input("Enter father's name: ").upper()
                c=input("Enter mother's name: ").upper()
                d=int(input("Enter house / flat number"))
                e=input("Enter colony name: ").upper()
                f=input("Enter city name:").upper()
                g=input("Enter state name: ")
                h=int(input("Enter pincode : "))
                print("Enter streams as PCM for Engeniring , PCB for Medical and COMMERS for commersial application")
                i=input("Enter stream: ").upper()
                j=int(input("Enter mobile number: "))
                k=input("Enter your email address: ")
                l=input("Enter school name: ").upper()
                m=input("Enter year of passing: ")
                
                if i=="PCM":
                                import selectpcmcoll as se
                                se.selectpcmcollege(idm,n,a)
                                import engicourse as pm
                                pm.selectpcmcourse(idm,n,a)
                                pass
                elif i=="PCB":
                                import selectpcbcoll as se
                                se.selectpcbcollege(idm,n,a)
                                import medicalcourse as pb
                                pb.selectpcbcourse(idm,n,a)
                                pass
                elif i=="COMMERS":
                                import selectcommcoll as se
                                se.selectcommerscollege(idm,n,a)
                                import commerscourse as cc
                                cc.selectcommerscourse(idm,n,a)
                                pass
                else:
                                print("Wrong input please restart")
                                #break
                u=str(n)
                sql="insert into carrerobjective(aadhar_number,rollnumber,nameofstudent,fathersname,mothersname,housenumber,colony,city,state,pincode,mobilenumber,Email,schoolname,class12passingyear,stream) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values=(idm,u,a,b,c,d,e,f,g,h,j,k,l,m,i)
                mycursor.execute(sql,values)
                mydb.commit()
                pass

