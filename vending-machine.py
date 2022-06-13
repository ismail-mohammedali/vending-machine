from decimal import Decimal
from unicodedata import decimal
import json

class vendingMachine ():
    def __init__(self) -> None:
        
        
        dataFile = open('database.json')
        self.data = json.load(dataFile)
        self.curTotalInMachine = Decimal("{:.2f}".format(float(0.00)))
        
        
        # self.moneyInMachine = {.25:100,
        #  .05:100,
        #  .10:100,
        #  1:100    }
        # self.translation = {'quarter':.25,
        #  'nickel':.05,
        #  'dime':.10,
        #  'dollar':1,
        #  .25:'quarter',
        #  .05:'nickel',
        #  .10:'dime',
        #  1:'dollar'                  
        # }
        # # self.password = "Admin"
        # # self.data = {'moneyInMachine':self.moneyInMachine,
        # #              'translation':self.translation,
        # #              'password':self.password}
    
    def storeInDatabase(self):
        
        filename = 'database.json'
        with open(filename, "w") as f:
            f.write(json.dumps(self.data))
        
    
    def insertMoney (self,amount):
        
        
        self.curTotalInMachine += Decimal(self.data['translation'][amount])
        #self.curTotalInMachine =round(self.curTotalInMachine, 2)
        self.data['moneyInMachine'][self.data['translation'][amount]]+=1
        print('After Inserting {} your total is {:.2f}'.format(amount,self.curTotalInMachine))
    
    
    def coinReturn(self):
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
                #print(x)
                x-=1
        self.storeInDatabase()    
        return coinReturn    
    def getItem(self,item):
        
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
    def service(self,password):
        #1- Ability to change amount 
        #2- ability to add and remove items 
        #3- 
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
                pass
            
        self.storeInDatabase()    
        
        

VM = vendingMachine()
#print(VM.data)
VM.service("Admin")
# VM.insertMoney('dollar')
# VM.insertMoney('dollar')
# VM.insertMoney('dime')
# VM.insertMoney('nickel')
# VM.insertMoney('quarter')
# print(VM.curTotalInMachine)
# VM.getItem('itemA')
# VM.getItem('itemA')
# print(VM.curTotalInMachine)
# print(VM.data)
# print(VM.coinReturn())
# print(VM.data)
# VM.insertMoney('dollar')
# VM.insertMoney('dollar')

# VM.insertMoney('quarter')
# VM.insertMoney('quarter')
# VM.insertMoney('quarter')
# VM.insertMoney('quarter')
# VM.insertMoney('dollar')
# VM.insertMoney('dime')
# VM.insertMoney('nickel')

# print(VM.coinReturn())
#VM.moneyInMachine[.25]=101
#print(VM.moneyInMachine[.25])
#print(VM.service('Admin'))