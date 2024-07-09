print("<","--"*25,"WELCOME","--"*25,">")
print("<","--"*27,"TO","--"*27,">")
print("<","--"*23,"CARRER OBJECTIVE","--"*22,">")
print("<","--"*25,"PROJECT","--"*26,">")
print("Enter your choice accordingly to the instructions given as do follow it")
while True:
                print("\n\n\n\nPress 'Y' to continue else 'N' to quit")
                cho=input("Enter your choice\n>>>").upper()
                if cho=="Y":
                                print("Press the numbers alloted to functions to move on to next step!")
                                print("1)To Fill Form\n2)To Check the Details\n3)To Edit or to change the details in the form\n4)To cancle registration of a perticular")
                                ch=int(input("Enter your choice here\n>>>"))
                                if ch==1:
                                                import filling_form as ff
                                                ff.fill_form()
                                                pass
                                elif ch==2:
                                                import view_form as vf
                                                vf.view_of_form()
                                                pass
                                elif ch==3:
                                                import Edit_Details
                                                pass
                                elif ch==4:
                                                import cancelling_registration
                                else:
                                                print("Entered Wrong degit! Please Restart!")
                                                continue
                                pass
                elif cho=="N":
                                quit()
                                pass
                else:
                                print("Wrong choice!!!!")
                                break
