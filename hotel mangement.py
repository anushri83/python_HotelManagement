
menu={"pizza":100,        #to store menu
      "burger":80,
      "cold drink":60,
      "momos":90,
      "sandwich":70
      }
bill={}    #to storw bill
total=0    # to stote total of bill

print("----------HOTEL ASHIRWAD----------")

while True:
    print("1.Show menu")
    print("2.Add product in menu")
    print("3.Delete product in menu")
    print("4.Make a bill")
    print("5.exit")
       
    choice=int(input("Enter your choice:- "))

    match(choice):
       
        case 1:                   #show menu 
           print("MENU")
           for i ,j in menu.items():
               print(i,":", j)
    

        case 2:                  #add item in menu
          product=input("Enter item name:- ")
          price=int(input("Enter price of item:- "))
          menu[product]=price
          print("successfully added item")
    

        case 3:                 #remove item in menu
          delete=input("Enter name of product to delete:- ")
          menu.pop(delete)
          print("successfully deleted item")


        case 4:                #Make a bill
          while True:
            y_n=input("you wanna add item or exit(Y/N):- " )
            if y_n=="y":
                bill_prod=input("Add product in bill:-")
                quantity=int(input("Enter quantity:- "))
                if bill_prod in menu:
                  x=menu[bill_prod]*quantity
                  bill[bill_prod]=x
                  print(bill)
                else:
                   print("sorry product not in menu !!")
            elif y_n=="n":
                for key,value in bill.items():
                    print(key,":", value)
                for key,value in bill.items():
                    total+=value
                print(f"your total bill is :{total}")
                exit

                 
        case 5:   #exit from program
          exit
                





                
             
             
             
    
    
    
          
          
    
 
