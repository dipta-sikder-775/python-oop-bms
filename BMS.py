class BankingManagementSystem:
    def __init__(self):
        self.clients = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_on = False

    def create_account(self, account_id):
        if account_id in self.clients:
            raise ValueError("Account already exists.")
        else:
            self.clients[account_id] = {
                'balance': 0, 'transaction_history': []}
            print("Account created successfully.")

    def check_balance(self, account_id):
        if account_id in self.clients:
            balance = self.clients[account_id]['balance']
            print(f"Available balance: {balance}")
        else:
            raise ValueError("Account does not exist.")

    def deposit(self, account_id, amount):
        if account_id in self.clients:
            if amount > 0:
                self.clients[account_id]['balance'] += amount
                self.total_balance += amount
                self.clients[account_id]['transaction_history'].append(
                    f"Deposited: {amount}")
                print("Money deposited successfully.")
            else:
                raise ValueError("Amount should be a positive number.")
        else:
            raise ValueError("This account does not exist.")

    def withdraw(self, account_id, amount):
        if account_id in self.clients:
            if amount > 0:
                if self.clients[account_id]['balance'] >= amount:
                    self.clients[account_id]['balance'] -= amount
                    self.total_balance -= amount
                    self.clients[account_id]['transaction_history'].append(
                        f"Withdrawn: {amount}")
                    print("Money Withdrawal successfully.")
                else:
                    raise ValueError("Insufficient balance!")
            else:
                raise ValueError("Amount should be a positive number")
        else:
            raise ValueError("Account does not exist")

    def transfer_amount(self, sender_id, receiver_id, amount):
        if sender_id in self.clients and receiver_id in self.clients:
            if amount > 0:
                sender_balance = self.clients[sender_id]['balance']
                if sender_balance >= amount:
                    self.clients[sender_id]['balance'] -= amount
                    self.clients[receiver_id]['balance'] += amount
                    self.clients[sender_id]['transaction_history'].append(
                        f"Transferred: {amount} to {receiver_id}")
                    self.clients[receiver_id]['transaction_history'].append(
                        f"Received: {amount} from {sender_id}")
                    print("Transfer successfully.")
                else:
                    raise ValueError("Insufficient balance.")
            else:
                raise ValueError("Amount should be a positive number.")
        else:
            raise ValueError("Receiver accounts do not exist.")

    def check_transaction_history(self, account_id):
        if account_id in self.clients:
            print('\nTransaction history:\n')
            history = self.clients[account_id]['transaction_history']
            for transaction in history:
                print(transaction)
        else:
            raise ValueError("This account does not exist.")

    def take_loan(self, account_id):
        if account_id in self.clients:
            if self.loan_feature_on:
                balance = self.clients[account_id]['balance']
                loan_amount = 2 * balance
                self.clients[account_id]['balance'] += loan_amount
                self.total_loan_amount += loan_amount
                self.clients[account_id]['transaction_history'].append(
                    f"Loan taken: {loan_amount}")
                print("Loan permitted.")
            else:
                print("Loan permission is currently off.")
        else:
            raise ValueError("This account does not exist.")

    def check_total_balance_of_bank(self):
        print(f"Total available balance in the bank is: {self.total_balance}")

    def total_loan_amount_of_clients(self):
        print(f"Total loan amount in the bank is: {self.total_loan_amount}")

    def turn_on_loan_feature(self):
        self.loan_feature_on = True
        print("Loan is on.")

    def turn_off_loan_feature(self):
        self.loan_feature_on = False
        print("Loan is off.")


banking_system = BankingManagementSystem()

""" Create accounts for users """
banking_system.create_account("client1")
banking_system.create_account("client2")
banking_system.create_account("client3")

""" Deposit money into client1's account """
banking_system.deposit("client1", 500000)

""" Withdraw an amount from client1's account """
banking_system.withdraw("client1", 20000)

""" Check client1's transaction history """
banking_system.check_transaction_history("client1")

""" Check client1's available balance """
banking_system.check_balance("client1")

""" Transfer an amount from client1's account to client2's account """
banking_system.transfer_amount("client1", "client2", 3000)

""" Take a loan from the bank for client1 """
banking_system.take_loan("client1")

""" Admin operations """
""" Check the total available balance of the bank """
banking_system.check_total_balance_of_bank()

""" Check the total loan amount of all clients """
banking_system.total_loan_amount_of_clients()

""" Turn on the loan feature for the bank """
banking_system.turn_on_loan_feature()

""" Turn off the loan feature for the bank """
banking_system.turn_off_loan_feature()

""" Perform some additional operations for testing edge cases """
try:
    """ Try to create an account with an existing account ID """
    banking_system.create_account("client1")
except ValueError as e:
    print(str(e))

try:
    """ Try to withdraw an amount larger than the available balance """
    banking_system.withdraw("client1", 1000000)
except ValueError as e:
    print(str(e))

try:
    """ Try to transfer an amount from a non-existing sender account """
    banking_system.transfer_amount("client4", "client2", 500)
except ValueError as e:
    print(str(e))

try:
    """ Try to transfer an amount to a non-existing receiver account """
    banking_system.transfer_amount("client1", "client5", 500)
except ValueError as e:
    print(str(e))

""" Check the transaction history of a non-existing account """
try:
    banking_system.check_transaction_history("client4")
except ValueError as e:
    print(str(e))
