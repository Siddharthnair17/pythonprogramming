class account:
    def __int__(self,acc,name,type):
       self.balance=0
       self.acc=acc
       self.name=name
       if(type==1):
         self.type="current"
       else:
         self.type="savings"
      
    def deposit(self):
        amount=float(input("enter amount tobe deposited:"))
        self.balance+=amount
    def withdraw(self):
        amount+=flopat(input("enter amount to be withdraw"))
       
        if(self.balance<amount):
           print("insufficent balance")
        else:
           self.balance==amount
    def display(self):
        print("name:",self.name,"/t/t account no:",self.acc,"\t \t balance:",self.balance,"\t\t acc:",self.type)
        acc=input("enter account number")
        name=input("enter name")
        type=input("choose account type \n1.current\n2.savings")
        obj=account(acc,name,type)
        while true:
            obj.display()
            ch=int(input("\n1.deposit\n2.withdraw\n3.exit"))
            if(ch==1):
               Obj.deposit()
            elif(ch==2):
              obj.withdraw()
            elif(ch==3):
                break
            else:
               print("invalid entry")
     
