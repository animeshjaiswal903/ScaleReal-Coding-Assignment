import User
import Admin
def ask_func():
    print(" Welcome to Jaiswal Grocery")
    global ask2
    while(True):
        
        ask2=input("1:User login,2:Admin login,3:Exit")
        ask2=int(ask2)
        if ask2==0 or ask2==""or ask2==None or ask2>3:
            print("Invalid")
            continue
        else:
            break

def recursive():
    global ask2
    while ask2==1:
            User.userfunc()
            ask_func()
            recursive()
    else:
        if ask2==2:
            Admin.adminfunc()
            ask_func()
            recursive()            
        elif ask2==3:
            exit()
        
            
ask_func()
recursive()
    
    
