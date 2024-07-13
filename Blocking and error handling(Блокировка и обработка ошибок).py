import threading

class BankAccount:
    def __init__(self):
        self.balance = 1000
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            new_balance = self.balance + amount
            self.balance = new_balance
            print(f"Вы внесли: {amount}, баланс: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                new_balance = self.balance - amount
                self.balance = new_balance
                print(f"Вы сняли: {amount}, баланс: {self.balance}")
            else:
                print("На Вашем счете недостаточно средств")

def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)

if __name__ == "__main__":
    account = BankAccount()

    deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
    withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

    deposit_thread.start()
    withdraw_thread.start()

    deposit_thread.join()
    withdraw_thread.join()

    print(f"Всего на счете: {account.balance}")

