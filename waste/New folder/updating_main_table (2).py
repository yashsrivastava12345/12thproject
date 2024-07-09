import mysql.connector as mysql
import pandas as pd
import numpy as np
mydb=mysql.connect(host="localhost",user="root",passwd="",database="carrer_objective")
mycursor=mydb.cursor()
print("Press  the alloted numbers to edit the details")
print("1)Edit name of student\n2)Edit name of father\n3)Edit mothers name\n4)Edit house number\n5)Edit colony name\n6)Edit city name\n7)Edit state name\n8)Edit pincode of city\n9)Edit mobile number\n10)Edit Email Id\n11)School name\n12)Edit passing year")
cho = int(input("Enter your choice here \n>>>"))
ida=input("Enter your aadhar card number here\n>>>")
values=None
sql,sql1,sql2="","",""
if cho==1:
                sql="update carrerobjective set nameofstudent=%s where aadhar_number=%s"
                print("Enter your stream please do select from following three fields namly \n1)PCM\n2)PCB\n3)COMMERS")
                st=input(">>>").upper()
                if st=="PCM":
                                sq1l="update pcmcollege set nameofstudent=%s where aadhar_number=%s"
                                sql2="update pcmcourse set nameofstudent=%s where aadhar_number=%s"
                                pass
                elif st=="PCB":
                                sq1l="update pcbcollege set nameofstudent=%s where aadhar_number=%s"
                                sql2="update pcbcourse set nameofstudent=%s where aadhar_number=%s"
                                pass
                elif st=="COMMERS":
                                sq1l="update commerscollege set nameofstudent=%s where aadhar_number=%s"
                                sql2="update commerscourse set nameofstudent=%s where aadhar_number=%s"
                                pass
                name=input("Enter name of student\n>>>")
                values=(name,ida)
                mycursor.execute(sq1l,values)
                mycursor.execute(sql2,values)
                pass
elif cho==2:
                sql="update carrerobjective set fathersname=%s where aadhar_number=%s"
                name=input("Enter name of father\n>>>")
                values=(name,ida)
                pass
elif cho==3:
                sql="update carrerobjective set mothersname=%s where aadhar_number=%s"
                name=input("Enter name of mother\n>>>")
                values=(name,ida)
                pass
elif cho==4:
                sql="update carrerobjective set housenumber=%s where aadhar_number=%s"
                name=input("Enter House / flat number\n>>>")
                values=(name,ida)
                pass
elif cho==5:
                sql="update carrerobjective set colony=%s where aadhar_number=%s"
                name=input("Enter name of colony \n>>>")
                values=(name,ida)
                pass
elif cho==6:
                sql="update carrerobjective set city=%s where aadhar_number=%s"
                name=input("Enter name of city\n>>>")
                values=(name,ida)
                pass
elif cho==7:
                sql="update carrerobjective set state=%s where aadhar_number=%s"
                name=input("Enter name of state\n>>>")
                values=(name,ida)
                pass
elif cho==8:
                sql="update carrerobjective set pincode=%s where aadhar_number=%s"
                name=input("Enter pincode of city\n>>>")
                values=(name,ida)
                pass
elif cho==9:
                sql="update carrerobjective set mobilenumber=%s where aadhar_number=%s"
                name=input("Enter mobile number\n>>>")
                values=(name,ida)
                pass
elif cho==10:
                sql="update carrerobjective set Email=%s where aadhar_number=%s"
                name=input("Enter your email id \n>>>")
                values=(name,ida)
                pass
elif cho==11:
                sql="update carrerobjective set schoolname=%s where aadhar_number=%s"
                name=input("Enter your school name\n>>>")
                values=(name,ida)
                pass
elif cho==12:
                sql="update carrerobjective set class12passingyear=%s where aadhar_number=%s"
                name=input("Enter name of passing year of class 12")
                values=(name,ida)
                pass
else:
                print("Wrong choice !!!\nplrase restart the process!!!!!")
                pass
mycursor.execute(sql,values)
mydb.commit()
