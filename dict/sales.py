file = open("dict/text.txt")
lines = file.readlines()

file.close()

database = {}
for line in lines:
    customer, product, number = line.split()
    if customer not in database.keys():
        database[customer] = {product: int(number)}
    else:
        database[customer][product] = database[customer].get(product, 0) + int(number)
for customer, product_number in sorted(database.items()):
    print(customer, ':')
    for product, number in sorted(database[customer].items()):
        print(product, number)
