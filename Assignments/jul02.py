class Bank:
    def __init__(self, AccountNo, Amount, Address):
        self.AccountNo = AccountNo
        self.Amount = Amount
        self.Address = Address

    def display_account_info(self):
        print(f'Account holder number: {self.AccountNo}')

    def display_account_holder_address(self):
        print(f'Account holder address: {self.Address}')

acholder = Bank(AccountNo=int(9226483), Amount=1000, Address='At Pune Kharadi')

acholder.display_account_info()
acholder.display_account_holder_address()
