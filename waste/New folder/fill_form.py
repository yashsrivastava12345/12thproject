import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
pcmrollno=3000
pcbrollno=2000
commersrollno=1000
countpcm=0
countpcb=0
countcommers=0
idc="a12s56d94f5f".upper()
x=""                
idm=""
u=0
z=0
q1=[]
def fill_form():
                idm=input("Enter your aadhar card number: ")
                a=input("Enter student's name : ").upper()
                b=input("Enter father's name: ").upper()
                c=input("Enter mother's name: ").upper()
                d=int(input("Enter house / flat number"))
                e=input("Enter colony name: ").upper()
                f=input("Enter city name: ").upper()
                g=input("Enter state name: ")
                h=int(input("Enter pincode : "))
                print("Enter streams as PCM for Engeniring , PCB for Medical and COMMERS for commersial application")
                i=input("Enter stream: ").upper()
                j=int(input("Enter mobile number: "))
                k=input("Enter your email address: ")
                l=input("Enter school name: ").upper()
                m=input("Enter year of passing: ")
                n=0
                countpcm=0
                countpcb=0
                countcommers=0
                if i=="PCM":
                                countpcm+=1
                                n=pcmrollno+countpcm
                                import selectpcmcoll as se
                                se.selectpcmcollege(idm,n,a)
                                pass
                elif i=="PCB":
                                countpcb+=1
                                n=pcbrollno+countpcb
                                import selectpcbcoll as se
                                se.selectpcbcollege(idm,n,a)
                                pass
                elif i=="COMMERS":
                                countcommers+=1
                                n=commersrollno+countcommers
                                import selectcommcoll as se
                                se.selectcommerscollege(idm,n,a)
                                pass
                else:
                                print("Wrong input please restart")
                                #break
                u=str(n)
                sql="insert into carrerobjective(id,rollnumber,nameofstudent,fathersname,mothersnamr,housenumber,colony,city,state,pincode,mobilenumber,Email,schoolname,class12passingyear,stream) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values=(idm,u,a,b,c,d,e,f,g,h,j,k,l,m,i)
                mycursor.execute(sql,values)
                mydb.commit()
                pass
