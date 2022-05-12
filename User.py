def userfunc():
    import user_class_module
    
    def welcome_message():
        global name
        print("Welcome to Jaiswal Grocery")
        name=input("Enter your name:")
        print("\nWelcome ",name)
   
    def write_to_customer_database():
        #global name,actual_amount,discount,final_bill,cart_items
        file=["Name:",name,";","Actual amount(Rs):",choice.actual_amount,";","Dicount(Rs):",choice.discount,";","Final bill(Rs):",choice.final_bill,";","Cart items:",choice.cart_items]
        customer_data = open(files.customer_database, "a")
        customer_data.write("\n")
        for value in file:
            customer_data.writelines(str(value)+" " )
        customer_data.close()    
    def askfunc(): 
            global ask
            while(True):
                ask=input("1: Go to categories,2:My cart,3:Remove from cart,4:Go to bill generation,5:Exit.")
                print("")
                if ask==None or ask=='' or int(ask)>5:
                    print("Invalid")
                    continue
                else:
                    ask=int(ask)
                    break
    def recursivefunc():
        global ask
        while ask==1:
            choice.category_select()
            askfunc()
            recursivefunc()
        else:
            if ask==2:
                choice.mycart()
            
                askfunc()
                recursivefunc()
                
            elif ask==3:
                if choice.cart_items=={}:
                    print("Your cart is empty")
                    askfunc()
                    recursivefunc()
                else:
                    choice.remove_cart()
                    askfunc()
                    recursivefunc()
                     
            elif ask==4:
                if choice.cart_items=={}:
                    print("Your cart is empty")
                    askfunc()
                    recursivefunc()
                else:
                     choice.billfunc()
                     askfunc()
                     recursivefunc()
            else:
                pass


    welcome_message()
    
    files= user_class_module.import_class("price.txt","cat.txt","customer_database.txt")
    files.import_price()
    
    choice= user_class_module.choice_class(files.price_dict,files.cart_items,files.category,files.category_dict)


    askfunc()
    recursivefunc()
    write_to_customer_database()


 
