from argparse import Action
from decimal import Decimal
from unicodedata import decimal
import json

class vendingMachine (): 
    def __init__(self) -> None: #starting variables for the class 

        self.data = json.load(open('database.json'))
        self.curTotalInMachine = Decimal("{:.2f}".format(float(0.00)))
        self.itemsForSale = [x for x in self.data['product']]
        
    
    def storeInDatabase(self): # using this method to store data after changes are made to database json
        
        filename = 'database.json'
        with open(filename, "w") as f:
            f.write(json.dumps(self.data))
        
    
    def insertMoney (self,amount): # This method adds amount to varible moneyInMachine 
        
        
        self.curTotalInMachine += Decimal(self.data['translation'][amount])
        #self.curTotalInMachine =round(self.curTotalInMachine, 2)
        self.data['moneyInMachine'][self.data['translation'][amount]]+=1
        print('After Inserting {} your total is {:.2f}'.format(amount,self.curTotalInMachine))
        return True
    
    def coinReturn(self): #This method returns the coin in dict format highest amount returned first
        coinReturn = {}
        translation = {              
        }
         
        sorted_amount = [float(x) for x in self.data['moneyInMachine']]
        sorted_amount.sort()
        x = -1
        print(sorted_amount)
        #print(sorted_amount[-1])
        self.curTotalInMachine=Decimal('{:.2f}'.format(self.curTotalInMachine))
        while self.curTotalInMachine> 0.01:
            
            self.curTotalInMachine=Decimal('{:.2f}'.format(self.curTotalInMachine))
            cur_ammount=Decimal('{:.2f}'.format(float(sorted_amount[x])))
            
            #print(self.curTotalInMachine,x, sorted_amount[x],self.curTotalInMachine >= sorted_amount[x])
            if self.curTotalInMachine >= cur_ammount:
                
                self.curTotalInMachine -= cur_ammount
                self.data['moneyInMachine']["{:.2f}".format(cur_ammount)]-=1
                
                coinReturn[self.data['translation']['{:.2f}'.format(sorted_amount[x])]]=coinReturn.get(self.data['translation']['{:.2f}'.format(sorted_amount[x])],0)+1
            else: 
               
                x-=1
        self.storeInDatabase()    
        return coinReturn    
    def getItem(self,item): # this method uses the moneyInMachine varible and data var to use the money in exchange of the amount
        
        if item not in self.data['product']:
            print("the product doesn't exist. Please try again")
            return False
        
        price = Decimal(self.data['product'][item]['price'])
        quantity = self.data['product'][item]['quantity']
        if quantity< 1 : 
            print('The item is not avalible. we are sorry :(')
            
            return False
        if price>self.curTotalInMachine: 
            print('Insufficient funds, Current Bal:{:.2f} the required amount is {:.2f}'.format(self.curTotalInMachine,price))
            return False
        self.data['product'][item]['quantity']-=1
        self.curTotalInMachine = self.curTotalInMachine - price 
        
        self.storeInDatabase()
        return True
    def service(self,password): # This method can help service the machine where amount saved in the machine and change the quanitty of the product 
        
        if self.data['password'] != password:
            return "The Password is incorrect"
        action = 0 
        while action !=-1: 
            action = int(input ("Please Enter 1 to change amount in the machine.\nPlease enter 2 to change the product price or quantity\n\n\nPlease enter -1 to exit service mode\n\n"))
            if action ==1: 
                for amount in self.data['moneyInMachine']:
                    quantityDelta = int(input("\n\nPlease enter positve or negetive value to change the {}$ by that number.\nNegetive number can't be less than current quatity of the curreny or it will not take the changes.\n\n".format(amount)))
                    if self.data['moneyInMachine'][amount]+quantityDelta >=0:
                        self.data['moneyInMachine'][amount]= self.data['moneyInMachine'][amount]+quantityDelta
                    else: 
                        print("changes did not take affect as you are removing more for Vending machine than it currently has! Please try again for {}$".format(amount))
                    
                    
                    
                    
                    
            elif action ==2: 
                print("In progress")
            #To Do - create a process where the user can edit the quantity for the current products
            
        self.storeInDatabase()    
        
        
if __name__ == '__main__':
    
    print("welcome to VM\n\n")
    VM = vendingMachine()
    
    while True: 
        for count, product in enumerate(VM.itemsForSale):
            print('Please enter {} to get {}'.format(count+1,product))
        print('Please enter 0 for service')
        print('Enter -1 to quit the application')
        action =int(input())
        if action > 0 and action <= len(VM.itemsForSale):
            pass
        elif action == 0:
            password = input("Please enter password to access service mode")
            VM.service(password) 
        elif action == -1: 
            print('\n\n\nThank you for using our VM. Please come again :)')
            break
        
        
