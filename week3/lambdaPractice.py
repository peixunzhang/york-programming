def includeVAT(price):
    return lambda x: (price*1.2)*x
itemCost = []
for i in range(1, 9):
    itemCost.append(includeVAT(i))
print("5 items at $7", itemCost[6](5), "icluding VAT")
