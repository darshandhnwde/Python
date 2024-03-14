# Constructor :

class Bank:
    def __init__(self,Bank_name,Full_name,Own_by) -> None:
        self.Bank_name = Bank_name
        self.Full_name = Full_name
        self.Own_by = Own_by


    def bank_detail(self):
        print(f"Bank name :{self.Bank_name }")
        print(f"Full name :{self.Full_name}")
        print(f"Own by :{self.Own_by} sector")

   
bank1 = Bank("SBI","State Bank Of India","Government")
bank2 = Bank("PNB","Punjab national Bank","Government")
bank3 = Bank("HDFC","Housing Development Finance Corporation Bank","Private")
bank4 = Bank("Axis","Axis Bank","Private")
bank5 = Bank("BOI","Bank Of India","Government")

print(bank1.bank_detail())
print(bank2.bank_detail())
print(bank3.bank_detail())
print(bank4.bank_detail())
print(bank5.bank_detail())

