from typing import List


def data(file_mane: str) -> List[str]:
    file = open(file_mane)
    lines = file.readlines()
    file.close()
    return lines


def get_deposit(name: str, amount: str) -> None:
    amount = int(amount)
    if name not in bank_accounts:
        bank_accounts[name] = amount
    else:
        bank_accounts[name] += amount


def get_withdraw(name: str, amount: str) -> None:
    amount = int(amount)
    if name not in bank_accounts:
        bank_accounts[name] = 0
    bank_accounts[name] -= amount


def get_balance(name: str) -> None:
    if name not in bank_accounts:
        print('ERROR')
    else:
        print(bank_accounts[name])


def get_transfer(name_from: str, name_to: str, amount: str) -> None:
    get_withdraw(name_from, amount)
    get_deposit(name_to, amount)


def get_income(percent: str) -> None:
    percent = int(percent)
    for name, amount in bank_accounts.items():
        if amount > 0:
            bank_accounts[name] += int(amount * percent / 100)


action_map = {'DEPOSIT': get_deposit, 'WITHDRAW': get_withdraw, 'BALANCE': get_balance, 'TRANSFER': get_transfer, 'INCOME': get_income}
def perform_operations(operations: List[str]) -> None:
    for line in operations:
        action, *args = line.split()
        action_map[action](*args)



operations = data("text.txt")
bank_accounts = {}
perform_operations(operations)
