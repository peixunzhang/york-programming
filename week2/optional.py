
fileName = "abc.txt"
try:
    file = open(fileName)
except FileNotFoundError:
    print("The file does not exist")
else:
    for line in file:
        print(line, end="")
finally:
    print("\nClosing file")
    file.close()
