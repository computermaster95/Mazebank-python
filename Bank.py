#the name of the Bank Is (MazeBank)
#The ID or PASSWORD is 2011
#The Balance Is 9000000
#The code may be had alot of problems ,So you can solve it and enjoy



import time
trials = 3   ####login trials
id = 2011   ######password
a = 9000000 ####account_balance

def menu():
    #######chose menu#########
    print("welcome sure:-)")
    print("username:dev_20       amount:9000000")
    print("#########################################")
    print("----------------Main Menu----------------")
    print("-----------------------------------------")            
    print("1)Add Money--------------2)Transfer Money")
    print("-----------------------------------------")
    print("3)Show Balance---------------------4)EXIT")        
    print("-----------------------------------------")
    choice = input("Enter Your Choice Here(1/2/3/4)?:")
    print("--------------------------------------------")

    ##########operations########
    if choice == '1':
        #add_money
        x=input("Enter your amount:")
        print("about " + x + " has been added to your balance")
        y = int(a) + int(x)
        print("your balance Right Now is :")
        print(y)
        print("----------")
        time.sleep(2)
    elif choice == '2':
        #transfer_money
        amount = input("Enter Your Amount:")
        username = input("Enter the username of the taker:")
        print("the amount of " +amount+ " has been transfered to " +username+ " SUCCISFULLY!") 
        print("your amount rghit now is")
        z = int(a) - int(amount)
        print(z)
        time.sleep(2)
    elif choice == '3':
        #show_balance
        print(a)
        time.sleep(2)
    elif choice == '4':
        #exiting
        print("Thanks For Using Our Services:)") 
        time.sleep(2)     
    else:
        print("Invalid Syntax")
################login system###############
while trials != 0:
    print("--------------------")
    print("Welcome to MazeBank")
    print("--------------------")
    pin = int(input("Enter your ID:"))
    print("----------------------------")
    if pin != id:
        trials-=1
        print("Wrong Number You Have " ,trials ," Trials Left")
    elif pin == id:
        menu()
