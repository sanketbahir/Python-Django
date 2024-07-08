#class bank 
#instance variable : name ,ammount , address , accountno
#instance method : createAcccount(), DisplayAccount()
class Bank_Account:
    Bank_Name = 'HDFC'
    ROI_FD = 4.5 
    def __init__(self):
        self.Name = ''
        self.Amount = 0
        self.Address = ''
        self.accountno = 0

    def createAccount(self):
        self.Name = input('Enter your name: ')
        self.Amount = int(input('Enter your initial amount: '))
        self.Address = input('Enter your Address: ')
        self.accountno = int(input('Enter your account Number: '))
        
    def Display(self):
        print(f'Account name: {self.Name} \nAmount: {self.Amount} \nAddress: {self.Address} \nAccount no: {self.accountno}')
        
def main():
    print('Name of the bank:', Bank_Account.Bank_Name)
    user1 = Bank_Account()
    user2 = Bank_Account()
    print()
    print('Creating First Account: ')
    user1.createAccount()
    print('Creating Second Account: ')
    user2.createAccount()
    print('Displaying First Account: ')
    user1.Display()
    print('Displaying Second Account: ')
    user2.Display()

if __name__ == "__main__":
    main()
