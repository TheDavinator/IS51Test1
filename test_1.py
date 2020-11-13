
def Hundred_A_Day(Days) :
    Pay = 100
    Bank_Account = 0
    while Days > 0:
        Pay += Bank_Account
        Days -= 1
        if Days == 0 :
            return Bank_Account

def Compound_A_Day(Days) :
    Pay = 1
    Bank_Account = 0
    
    while Days > 0 :
        Pay += Bank_Account
        Pay = Pay * 2
        if Days == 0:
            return Bank_Account



Days = 10
Salary1 = Compound_A_Day(Days) 
Salary2 = Hundred_A_Day(Days)

if Salary1 > Salary2 :
    print("Option 1 is better")
if Salary2 > Salary1 :
    print("Option 2 is better")
if Salary1 == Salary2 :
    print("Option 1 and Option 2 pays the same")

#lol

