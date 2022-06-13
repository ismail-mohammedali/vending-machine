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
        if self.password == password:
            "Print"
        else:
            return "The Password is incorrect"
        

VM = vendingMachine()
#print(VM.data)

VM.insertMoney('dollar')
VM.insertMoney('dollar')
VM.insertMoney('dime')
VM.insertMoney('nickel')
VM.insertMoney('quarter')
print(VM.curTotalInMachine)
VM.getItem('itemA')
VM.getItem('itemA')
print(VM.curTotalInMachine)
print(VM.data)
print(VM.coinReturn())
print(VM.data)
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