def Hundred_A_Day(Days) :
    Pay = 100
    Bank_Account1 = 0
    while Days > 0:
        Bank_Account1 += Pay
        Days -= 1
        if Days == 0 :
            return Bank_Account1

def Compound_A_Day(Days) :
    Pay = 1
    Bank_Account2 = 0
    while Days > 0 :
        Bank_Account2 += Pay
        Pay += Pay * 2
        Days -= 1
        if Days == 0:
            return Bank_Account2


Days = 10
Salary1 = Hundred_A_Day(Days) 
Salary2 = Compound_A_Day(Days)
if Salary2 < Salary1 :
    print ("Option 1 is Better")
    if Salary1 < Salary2 :
        print("Option2 is better")
        if (Salary1 == Salary2) :
            print("They are the same!")

