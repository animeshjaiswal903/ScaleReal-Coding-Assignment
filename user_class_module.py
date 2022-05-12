class import_class:
    def __init__(self,price,category,customer_database):
        self.price=price
        self.category=category
        self.customer_database=customer_database
        
        
    def import_price(self):
        #global price_dict,category,category_dict,cart_items
        import ast
        price_catlog=open(self.price,"r")
        self.price_dict=ast.literal_eval(price_catlog.read())

        catlog=open(self.category,"r")
        catln=ast.literal_eval(catlog.read())
        #catln={"Spices":["Cinnamon","Cumin","Pepper"],"Veggies":["Onion","Spinach","Cabbage"]}

        a=list(x for x in range(1,len(catln)+1))
        b=list(catln.keys())
        self.category=dict(zip(a,b))
            #category={1:"Spices",2:"Veggies"}

        c=list(catln.values()) #[['Cinnamon', 'Cumin', 'Pepper'],['Onion', 'Spinach', 'Cabbage']]
        c3=[]
        c_length=list(len(x) for x in c) #c3=[3,3]
        for i,v in enumerate(c):  
            d=dict(zip( list(x for x in range(1,c_length[i]+1)) ,c[i]))
            c3.append(d)
        self.category_dict=dict(zip(a,c3)) # {1: {1: 'Cinnamon', 2: 'Cumin', 3: 'Pepper'}, 2: {1: 'Onion', 2: 'Spinach', 3: 'Cabbage'}}

        self.cart_items={}  
        
    








class choice_class:
    
    def __init__(self,a,b,c,d):
        self.price=a
        self.cart_items=b
        self.category=c
        self.category_dict=d
    
    def category_select(self):
   
        def product_price(a,b):
            sl=list(b.values())
            sv=[]
            for v in sl:
                sv.append(a[v])
            sp=dict(zip(sl,sv))
            print(sp)

        #global y,self.category,self.cart_items,self.category_dict
        print("Category selection:")
        print("")

        while(True):
            y=input("Select a category:{}".format(self.category))
            if y==None or y=='' or int(y)>len(self.category):          # if user do not type anything and press enter
                print("You did not select the availble categories, kindly select the ones which are available.")
                continue
            else:
                y=int(y)
                print("You selected category:",y,self.category[y])
                print("Price(in Rs) :")
                product_price(self.price,self.category_dict[y])             #price_product() using here
                break
    

        

        z1=[]     #z1 will contain selected product's name's number:[ 1 2 3], values inside z1 will be used to extract the actual names(product_names) from category_dict[category[y]]           
        z2=[]     #z2 is a list that will have quantity of products choosen by customer:[45 55 30]
        z3={}     #z3 is a dict that will have keys:product_names,values:z2(product quantities)
        product_names=[]


        #z1 execution
        while(True):
            print("Available {c1} products:{c2}".format(c1=self.category[y], c2=self.category_dict[y] ))
            z1=input("Select the {c3} you want to add in cart (in spaces)".format(c3=self.category[y]))
            z1=z1.split()
            z1=list(map(int,z1))

            #for loop to check any value which is not in the option and assign value to "error"
            for i in range(len(z1)):
                if z1[i]==None or z1[i]=="" or z1[i] >len(self.category_dict[y]):
                    error=1
                else:
                    error=0   
            # if error parameter is 1,then the program will ask user to type in again the correct available product numbers
            if error==1:
                print("Your selected products are not available at this time, kindly select the ones which are available and type their corresponding number.")
                continue   
            else:
                print("you have selected:")                                #product_names are printed here which was taken from z1
                for v in z1:                                               
                    product_names.append(self.category_dict[y][v])
                print(product_names)
                break
        #z2 execution    
        while(True):                                                       #z2 is a list that will have quantity of products choosen by customer.
            z2=input("Enter the amount of {c4} you want to purchase: (in spaces)".format(c4=product_names))
            z2=z2.split()
            z2=list(map(int,z2))
            for i in range(len(z1)):
                    if z2[i]==None or z2[i]=="" or z2[i] >100:
                        error=1
                    else:
                        error=0
            # if error parameter is 1,then the program will ask user to type in again the correct available quantity
            if error==1:
                print("Items quantity more than 100 is not permitted to a single user.")
                print("Your selected products are not available at this time, kindly select the ones which are available and type their corresponding number.")
                continue   
            else:
                break
        #z3 = {product_name:quantity}
        z3=dict(zip(product_names,z2))
        if self.cart_items=={}:# cart_items will be an updated form of z3 #defining product_names list and checking if cart_items is already filled
            self.cart_items=z3
        else:
            self.cart_items.update(z3)
                                           #cart_items is updated z3
        print("Your cart items with quantity are:",self.cart_items)    
    
    def mycart(self):
        if self.cart_items=={}:
            print("Your cart is empty")
        else:
            print("Your cart items are:",self.cart_items)
        
    def remove_cart(self):

        print("")
        cart_items_length_list=[x for x in range(1,len(self.cart_items)+1)] # list for keys for dictionary z5  {1:Cinnamon,2:...} as cart_items={Cinnamon:45,Pepper:....}
        z5=dict(zip(cart_items_length_list,self.cart_items))                # z5 dict will contain the dictionary of added cart items with new keys so that the keys will be used to delete items
        
        #z6 input loop    #z6 will be a list of user selected products number to remove from cart, as z5 will be shown as{1:cinnamon}
        while(True):
            print("Items in the cart are:",z5)
            
            z6=input("Enter the item product numbers you want to delete(in spaces):") 
            z6=z6.split()    
            z6=list(map(int,z6))
        
            #for loop to check any value which is not in the option and assign value to "error"
            for i in range(len(z6)):
                if z6[i]==None or z6[i]=="" or z6[i] >len(z5):
                    error=1
                else:
                    error=0
        
            if error==1:
                print("Your selected products are not in your cart, kindly select the ones which are present in your and type their corresponding number to remove them.")
                continue   
            else:
                break
        z7=[]                            #z7 will store the name of products that will be deleted. [Cinnamon, Pepper...]
        print("Your removed items are:")
        for i in z6:
            print(z5[i])
            z7.append(z5[i])
    
        print("Updated cart is: ")       # we will use the z7 list as list of keys of cart_items and delete the selected ones 
        for i in z7:
            del self.cart_items[i]
        print(self.cart_items)
        print("cart_items after remove func is",self.cart_items)

    def billfunc(self):
        #global cart_items,price,actual_amount,discount,final_bill
        self.discount=500
        atc=self.cart_items
        
        price_vl=[]
        atc_kl=list(atc.keys())   #key_list
        atc_al=list(atc.values()) #amount list

        for i in range(len(atc_kl)):
            price_vl.append(self.price[atc_kl[i]])
        

        bill=[]                   #list of multiplication result of price and quantity
        for i in range(len(atc_al)):
            bill.append(atc_al[i]*price_vl[i])
        print(bill)
        self.actual_amount=sum(bill)   #summation of bill list:actual amount
        
        if self.actual_amount>10000:                    #discount statement
            self.final_bill=self.actual_amount-self.discount
        else:                 
            self.discount=0  
            self.final_bill=self.actual_amount

    
        print("Your total bill was:{a}.\nYou got a discount of {b}.\nYour final bill amount is {c}.".format(a=self.actual_amount,b=self.discount,c=self.final_bill))
    
          

