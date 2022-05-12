class update_class:
    def __init__(self):
        print("Welcome to Admin Login,Hello Admin,make your changes here.")
    
    
    def update(self):
        import ast
        price_catalog=open("price.txt","r")
        price=ast.literal_eval(price_catalog.read())
        catlog=open("cat.txt","r")
        catln=ast.literal_eval(catlog.read())

        #1: Price_update funtion
        def price_update():
            print("Price update menu")
            def price_update_import_func():
                global price_temp,ptk_dict
                import ast
                price_catlog=open("price.txt","r")
                price=ast.literal_eval(price_catlog.read())
                price_catlog.close()

                price_temp=price.copy()
                ptv=list(price.values())
                ptk=list(price.keys())
                ptv_len_list=list(x for x in range(1,len(ptv)+1))
                ptk_len_list=list(x for x in range(1,len(ptk)+1))
                ptk_dict=dict(zip(ptk_len_list,ptk))


            def price_update_del():
                global price_temp,ptk_dict
                print("The current PriceList is:",price_temp)
                while (True):
                    print(ptk_dict)
                    deli=input("Select the product you want to remove or just press enter to go back")
                    if  deli.strip=='' or deli=="" or deli==None:
                        print("strip executed")
                        break
                    elif int(deli)>len(ptk_dict) or int(deli)<=0:
                        print("invalid")
                        continue
                    else:
                        price_temp.pop(ptk_dict[int(deli)])
                        print("Updated list is ",price_temp)
                        price_catlog2=open("price.txt","w")
                        price_catlog2.write(str(price_temp))
                        price_catlog2.close()
                        break

            def price_update_add():
                global price_temp
                print("The current PriceList is:",price_temp)
                while(True):
                    pu_k=input("Enter product name:")
                    if pu_k==None or pu_k=="":
                        print("Invalid")
                        continue
                    else:
                        break
                while(True):
                    pu_v=input("Enter its price")
                    if pu_v==None or pu_v=="":
                        print("Invalid")
                        continue
                    else:
                        break
                print("Following product and its price will be added:",pu_k,int(pu_v))
                #pu_kv=dict(pu_k,int(pu_v))
                price_temp[pu_k]=int(pu_v)
                price_catlog2=open("price.txt","w")
                price_catlog2.write(str(price_temp))
                price_catlog2.close()

            def price_update_ask():
                global pua
                while(True):
                    pua=input("1:Add,2:Delete,3=Exit")
                    if int(pua)==1 or int(pua)==2 or int(pua)==3:
                        pua=int(pua)
                        break
                    else:
                        print("Invalid,Enter the choice again.")
                        continue

            def price_update_recursive():
                global price,price_temp,ptk,ptv,pua,ptk_dict
                while pua==1:
                    price_update_import_func()
                    price_update_add()
                    price_update_ask()
                    price_update_recursive()
                else:
                    if pua==2:
                        price_update_import_func()
                        price_update_del()
                        price_update_ask()
                        price_update_recursive()
                    else:
                        pass
            price_update_ask()  
            price_update_recursive()
        
        #category_update function
        def category_update():
            print("Welcome to Category update menu:")
            def category_update_import_func():
                global ctv_dict,ctk_dict,category_temp
                import ast
                category_catlog=open("cat.txt","r")
                category=ast.literal_eval(category_catlog.read()) # category={"Spice":["Cumin","Pepper"],"Veggies":["Spinach","Onion"]}
                category_catlog.close()

                category_temp=category.copy()
                ctv=list(category_temp.values())
                ctk=list(category_temp.keys())
                ctv_len_list=list(x for x in range(1,len(ctv)+1))
                ctk_len_list=list(x for x in range(1,len(ctk)+1))
                ctk_dict=dict(zip(ctk_len_list,ctk)) # {1:'Spice',2:'Veggies'}
                ctv_dict=dict(zip(ctv_len_list,ctv)) # {1:[Cummin, pepper],2:[Onion,Spinach]}
                
            def category_update_add():
                global ctv_dict,ctk_dict,category_temp
                print("Category List:\n:",ctk_dict)
                cn=input("Enter the new category name:")#cn=category name
                while(True):
                    cp=input("How many products you want to insert inside this category?(or just press enter to go back)")#cp =category product
                    if cp.strip()=="" or cp==None or cp=="" or cp=='':
                        print("Went Back")
                        break
                    elif int(cp)<=0 or int(cp)>5:
                        print("Invalid input,Products less than 10 can be added")
                        continue
                    else:
                        cp=int(cp)                          
                        cpl=[]                                  #cpl=cp list
                        for i in range(cp):                     # enter product names one by one and run loop for cp times.
                            cpi=input("Enter Product name:")    #cpi = cp input
                            cpl.append(cpi)
                        # category add dict
                        category_temp[cn]=cpl
                        
                        category_catlog5=open("cat.txt","w")
                        category_catlog5.write(str(category_temp))
                        category_catlog5.close()
                        
                        break
            def category_update_del():
                while(True):
                    print("Category List:\n:",ctk_dict)
                    sci=input("Select Category:(or just press enter without putting any values to go back)")
                    if sci.strip=="" or sci==None or sci=="":
                        print("")
                        break
                    elif int(sci)>len(ctk_dict):
                        print("Invalid option")
                        continue
                    else:
                        sci=int(sci)
                        print("you selected:",ctk_dict[sci])#if- sci =1, ctk_dict[sci]="Spice"
                        category_temp.pop(ctk_dict[int(sci)])
                        print("Updated list is ",category_temp)
                        category_catlog2=open("cat.txt","w")
                        category_catlog2.write(str(category_temp))
                        category_catlog2.close()
                        break
            
            def category_update_ask():
                global cua
                while(True):
                    cua=input("1:Add Category,2:Delete Category,3=Exit")
                    if int(cua)==1 or int(cua)==2 or int(cua)==3:
                        cua=int(cua)
                        break
                    else:
                        print("Invalid,Enter the choice again.")
                        continue
            def category_update_recursive():
                global price,price_temp,ptk,ptv,cua,ptk_dict
                while cua==1:
                    category_update_import_func()
                    category_update_add()
                    category_update_ask()
                    category_update_recursive()
                else:
                    if cua==2:
                        category_update_import_func()
                        category_update_del()
                        category_update_ask()
                        category_update_recursive()
                    else:
                        pass
            category_update_ask()  
            category_update_recursive()
            
        #product update
        def product_update():
            def product_update_import_func():
                global ctv_dict,ctk_dict,category_temp
                import ast
                category_catlog=open("cat.txt","r")
                category=ast.literal_eval(category_catlog.read()) # category={"Spice":["Cumin","Pepper"],"Veggies":["Spinach","Onion"]}
                category_catlog.close()

                category_temp=category.copy()
                ctv=list(category_temp.values())
                ctk=list(category_temp.keys())
                ctv_len_list=list(x for x in range(1,len(ctv)+1))
                ctk_len_list=list(x for x in range(1,len(ctk)+1))
                ctk_dict=dict(zip(ctk_len_list,ctk)) # {1:'Spice',2:'Veggies'}
                ctv_dict=dict(zip(ctv_len_list,ctv))


            def product_update_add():

                while(True):
                    print(category_temp)
                    print(ctk_dict)

                    pua_sc=input("Select Category:(or just press enter without putting any values to go back)")
                    if pua_sc.strip=="" or pua_sc==None or pua_sc=="":
                        print("")
                        break
                    elif int(pua_sc)>len(ctk_dict):
                        print("Invalid option")
                        continue
                    else:
                        pua_sc=int(pua_sc)
                        print("You have selected:",ctk_dict[pua_sc])

                        temp_list=category_temp[ctk_dict[pua_sc]] #temp_list=["Cinnamon","Pepper"] if Spice is selected


                        #temp_list is updated by adding products 
                        while(True):
                                pp=input("How many products you want to insert inside this category?")#cp =category product
                                if pp.strip()=="" or pp==None or pp=="" or pp=='':
                                    print("Invalid")
                                    break
                                elif int(pp)<=0 or int(pp)>5:
                                    print("Invalid input,Products less than 5 can be added")
                                    continue
                                else:
                                    pp=int(pp)                                    
                                    for i in range(pp):                    
                                        ppi=input("Enter Product name:")    
                                        temp_list.append(ppi)

                                    category_temp[ctk_dict[pua_sc]]=temp_list
                                    print("Updated list is ",category_temp)
                                    category_catlog3=open("cat.txt","w")
                                    category_catlog3.write(str(category_temp))
                                    category_catlog3.close()

                                    break
                    break




            def product_update_del():
                while(True):
                    print(category_temp)
                    print(ctk_dict)
                    pua_sc=input("Select Category:(or just press enter without putting any values to go back)")
                    if pua_sc.strip=="" or pua_sc==None or pua_sc=="":
                        print("")
                        break
                    elif int(pua_sc)>len(ctk_dict):
                        print("Invalid option")
                        continue
                    else:
                        pua_sc=int(pua_sc)
                        print("You have selected:",ctk_dict[pua_sc])
                        temp_list=category_temp[ctk_dict[pua_sc]] #temp_list=["Cinnamon","Pepper"] if Spice is selected


                        #temp_list is updated by adding products 
                        while(True):
                    
                                pp=input("How many products you want to delete inside this category?")#cp =category product
                                if pp.strip()=="" or pp==None or pp=="" or pp=='':
                                    print("Invalid")
                                    break
                                elif int(pp)<=0 or int(pp)>len(temp_list):
                                    print("Invalid input,Products less than the available cannot selected.")
                                    continue
                                else:
                                    pp=int(pp)                                    
                                    for i in range(pp):                    
                                        ppi=input("Enter Product name:")    
                                        temp_list.remove(ppi)

                                    category_temp[ctk_dict[pua_sc]]=temp_list
                                    print("Updated list is ",category_temp)
                                    category_catlog4=open("cat.txt","w")
                                    category_catlog4.write(str(category_temp))
                                    category_catlog4.close()
                                    break
                    break




            def product_update_ask():
                global prua
                while(True):
                    prua=input("1:Add Product,2:Delete Product,3=Exit")
                    if int(prua)==1 or int(prua)==2 or int(prua)==3:
                        prua=int(prua)
                        break
                    else:
                        print("Invalid,Enter the choice again.")
                        continue

            def product_update_recursive():
                global ctv_dict,ctk_dict,category_temp
                while prua==1:
                    product_update_import_func()
                    product_update_add()
                    product_update_ask()
                    product_update_recursive()
                else:
                    if prua==2:
                        product_update_import_func()
                        product_update_del()
                        product_update_ask()
                        product_update_recursive()
                    else:
                        pass

            product_update_ask()  
            product_update_recursive()
            
        #update ask    
        def ask4_func():
            global ask4
            while(True):
                ask4=input("Select your update option :\n1:Prices,2:Categories,3:Products,4:Exit")
                if int(ask4)==1 or int(ask4)==2 or int(ask4)==3 or int(ask4)==4:
                    ask4=int(ask4)
                    break
                else:
                    print("Invalid,Enter the choice again.")
                    continue
        def recursive4_func():
            global ask4
            while ask4==1:
                price_update()
                ask4_func()
                recursive4_func()
            else:
                if ask4==2:
                    category_update()
                    ask4_func()
                    recursive4_func()
                elif ask4==3:
                    product_update()
                    ask4_func()
                    recursive4_func()
                else:
                    pass
        ask4_func()
        recursive4_func()
        
    def show_customer_database(self):
                customer_data=open("customer_database.txt", "r")
                for data in customer_data:
                    print(data)
       
