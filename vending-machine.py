from decimal import Decimal
from unicodedata import decimal

class vendingMachine ():
    def __init__(self) -> None:
        self.totalInMachine = Decimal("{:.2f}".format(float(0.00)))
        self.moneyInMachine = {.25:100,
         .05:100,
         .10:100,
         1:100    }
        self.translation = {'quarter':.25,
         'nickel':.05,
         'dime':.10,
         'dollar':1,
         .25:'quarter',
         .05:'nickel',
         .10:'dime',
         1:'dollar'                  
        }
    
    def insertMoney (self,amount):
        
        
        self.totalInMachine += Decimal("{:.2f}".format(float(self.translation[amount])))
        #self.totalInMachine =round(self.totalInMachine, 2)
        print('After Inserting {} your total is {}'.format(amount,self.totalInMachine))
    def coinReturn(self):
        coinReturn = {}
        translation = {              
        }
        sorted_amount = [x for x in self.moneyInMachine]
        sorted_amount.sort()
        x = -1
        print(sorted_amount)
        #print(sorted_amount[-1])
        self.totalInMachine=Decimal('{:.2f}'.format(self.totalInMachine))
        while self.totalInMachine> 0.01:
            
            self.totalInMachine=Decimal('{:.2f}'.format(self.totalInMachine))
            cur_ammount=Decimal('{:.2f}'.format(float(sorted_amount[x])))
            print(self.totalInMachine,x, sorted_amount[x],self.totalInMachine >= sorted_amount[x])
            if self.totalInMachine >= cur_ammount:
                
                self.totalInMachine -= cur_ammount
                
                coinReturn[self.translation[sorted_amount[x]]]=coinReturn.get(self.translation[sorted_amount[x]],0)+1
            else: 
                #print(x)
                x-=1
            
        return coinReturn    
    def getItem(self,item):
        pass
    def service(self):
        pass

VM = vendingMachine()

VM.insertMoney('dollar')
VM.insertMoney('dollar')
VM.insertMoney('dime')
VM.insertMoney('nickel')
VM.insertMoney('quarter')
VM.insertMoney('quarter')
VM.insertMoney('quarter')
VM.insertMoney('quarter')
VM.insertMoney('quarter')
VM.insertMoney('dollar')
VM.insertMoney('dime')
VM.insertMoney('nickel')

print(VM.coinReturn())