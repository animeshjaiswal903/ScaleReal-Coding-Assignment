def adminfunc():
    import admin_class_module
    
   

    def askfunc3(): 
                global ask3
                while(True):
                    ask3=input("1:Update (Price,Category,Product),2:Check customer database, 3:Exit.")
                    print("")
                    if ask3==None or ask3=='' or int(ask3)>3:
                        print("Invalid")
                        continue
                    else:
                        ask3=int(ask3)
                        break

    def recursivefunc3():
            global ask3
            while ask3==1:
                    update_ob.update()
                    askfunc3()
                    recursivefunc3()
            else:
                if ask3==2:
                    update_ob.show_customer_database()
                    askfunc3()
                    recursivefunc3()
                else:
                    pass

    update_ob=admin_class_module.update_class()
    askfunc3()
    recursivefunc3()

