#excerise A
myNumber = int(input("\tEnter your numbre: "))
print(f"\nThe even timetable for {myNumber} is: ")
for i in range(2,21, 2):
    print(i, "\ttimes", myNumber, "is", myNumber*i)

#excerise B
myNum = int(input("Pick your size: "))
spaces = myNum - 1
mySymbol = input("Pick your symbol: ")
myShape = input("Pick a symbol from L, R ot D: ")
if myShape == 'L':
    for i in range(1, myNum+1):  
      print(mySymbol * i, end="\n")
elif myShape == 'R':
    for i in range(1, myNum):  
      print((mySymbol * i).rjust(myNum), end="\n")
elif myShape == 'D':
    for i in range(1, myNum+1,2):
        print((mySymbol* i).center(myNum, " "), end="\n")
    for j in range(myNum-2, -1, -2):
        print((mySymbol* j).center(myNum, " "), end="\n")
else: print("Invalid input")

#excerise C
weekday = "M", "T", "W", "Th", "F", "S", "Su"
myDays = int(input("How many days in your month? "))
myStart = int(input("Which day of the week the cakendar starts on? "))
if myDays <= 31 and myDays>= 28:
    for d in weekday:
        print(d, end= "\t")
    if myStart <= 7 and myStart >= 1:
        print()
        print("\t" * (myStart-1), end="")
        for i in range(1, myDays+1, 1):
            print(i, end="\t")
            if (i + myStart - 1) % 7 == 0 : print();
        else: print("Invalid input")
else: print("Invalid input")
