# stack
myList = []
while(True):
    action = int(input("Pick an action, 1 for push, 2 for pop, 3 for view: "))
    if action == 1:
        myItem = input("Push an item to the list: ")
        myList.append(myItem)
    elif action == 2:
        last = len(myList)
        myList.pop(last-1)
    elif action == 3:
        print(myList)
    else: print("wrong input")

# queue
myListq = []
while(True):
    action = int(input("Pick an action, 1 for push, 2 for pop, 3 for view: "))
    if action == 1:
        myItem = input("Push an item to the list: ")
        myListq.append(myItem)
    elif action == 2:
        myListq.pop(0)
    elif action == 3:
        print(myListq)
    else: print(myListq)

# excerise 2
stores = {'L3': 'London', 'P2': 'Paris', 'N6': 'New York', 'B8': 'Beijing'}
April18 = {'L3': 390, 'P2': 250, 'N6': 460, 'B8': 470}
May18 = {'L3': 345, 'P2': 270, 'N6': 480, 'B8': 510}
Jun18 = {'L3': 379, 'P2': 300, 'N6': 450, 'B8': 360}
months = {'April18': April18, 'May18': May18, 'Jun18': Jun18}

print("Quarterly sales report\n")
for k, v in stores.items():
    total =  April18[k] + May18[k] + Jun18[k]
    average = total // len(months)
    maxLength = max([len(v) for v in stores.values()])
    print(f"{v.ljust(maxLength)}\t{k}:\t${average}\t${total}")
for mk, mv in months.items():
    sum = 0
    gTotal = 0
    for k, v in mv.items():
        sum = sum + v
        avg = sum//len(stores)
        gTotal = gTotal + sum
        maxLengthm = max([len(v) for v in months.values()])
    print(f"{mk.ljust(maxLengthm)}\t:\t\t${avg}\t${sum}")
print(f"GrandTotal: ${gTotal}")
