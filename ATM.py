print("="*53)
print("="*15, "WELCOME TO FIRST BANK", "="*15)
print("="*53)
print("Enter your card")
print('')
print("Please wait....")
Am = ['a','b','c','d','e','f','g','h','i','j']
By = ['1234','1111',"2222","3333","4444"]
while True:
    pin = str(input("Enter your pin: "))
    if pin in By:
        Transaction = input("Select transaction\na.Withdrawal\nb.Transfer\nc.Balance:\n")
        if Transaction == "a":    
            Amount = input("Select Amount\na.1000   b.2000\nc.3000   d.4000\ne.5000   f.6000\ng.7000   h.8000\ni.9000   j.10000\nk.OTHER:\n ")
    
            if Amount in Am:
                print("Take your cash 💴💴")
                print("THANK YOU FOR USING OUR BANK")
                #break    
            elif Amount == "k":
                am = int(input("Enter the Amount: "))
                print("Take your cash 💴💴💴💴💴")
                print("THANK YOU FOR USING OUR BANK")
                #break
        elif Transaction == "b":
            bank = input("which bank:\na.Between my first bank\nb.Other:\n")
            if bank == "a":
                Acc_no = str(input("Enter destination account: "))
                if len(Acc_no) < 10 or len(Acc_no) > 10:
                    print("Invalid Acc no")
                    break
                amount = int(input("Enter Amount: "))
                print("Transfer of the sum of ",amount,"to",Acc_no,"of first bank was succesfully") 
            elif bank == "b":
                Bank = input("Select bank\na.Acess     b.UBA\nc.Polaris   d.Union\ne.Opay      f.PalmPay\ng.GTB       h.FCMB\ni.Sky       j.MoniPoint\nk.OTHER: ")
                if Bank in Am:
                    Acc_no = str(input("Enter destination account: "))
                    if len(Acc_no) < 10 or len(Acc_no) > 10:
                        print("Invalid Acc no")
                        break
                    amount = int(input("Enter Amount: "))
                    print("Transaction succesfull")
                elif Bank == "k":
                    AM = input("Enter the name of the bank: ") 
                    Acc_no = str(input("Enter destination account: "))
                    if len(Acc_no) < 10 or len(Acc_no) > 10:
                        print("Invalid Acc no")
                        break
                    amount = int(input("Enter Amount: "))
                    print("Transfer of the sum of ",amount,"to",Acc_no,"of",AM,"was succesfully")
        elif Transaction == "c":
            print("Please wait....." )
            print("")
            print("Your balance is 7952895542.20")
                         
    else:
        print("Incorect pin ")
        quit()          
