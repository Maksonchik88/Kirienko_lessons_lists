file = open("dict/text.txt")
lines = file.readlines()
file.close()
bank_accounts = {}

for line in lines:
    if line.startswith('DEPOSIT'):
        _, name, amount = line.split()
        amount = int(amount)
        if name not in bank_accounts:
            bank_accounts[name] = amount
        else:
            bank_accounts[name] += amount
    elif line.startswith('WITHDRAW'):
        _, name, amount = line.split()
        amount = int(amount)
        if name not in bank_accounts:
            bank_accounts[name] = 0
        bank_accounts[name] -= amount
    elif line.startswith('BALANCE'):
        _, name = line.split()
        if name not in bank_accounts:
            print('ERROR')
        else:
            print(bank_accounts[name])
    elif line.startswith('TRANSFER'):
        _, name_from, name_to, amount = line.split()
        amount = int(amount)
        if name_from not in bank_accounts:
            bank_accounts[name_from] = 0
        bank_accounts[name_from] -= amount
        if name_to not in bank_accounts:
            bank_accounts[name_to] = 0
        bank_accounts[name_to] += amount
    elif line.startswith('INCOME'):
        _, balance = line.split()
        balance = int(balance)
        for name, amount in bank_accounts.items():
            if amount > 0:
                bank_accounts[name] += int(amount * balance / 100)
