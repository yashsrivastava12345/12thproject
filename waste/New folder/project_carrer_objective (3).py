while True:
                print("Enter you choice as \n1) fill your details \n2) view your details \n3) to correct your details if entered wrong")
                cho=int(input("Enter your choice"))
                if cho==1:
                                import fill_form as cd
                                cd.fill_form()
                                pass
                elif cho==2:
                                import view_form as vf
                                vf.view_of_form()
                                pass
                elif cho==3:
                                break
