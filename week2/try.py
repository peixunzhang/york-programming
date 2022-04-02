try:
    file = open("example.txt")
    line = file.read()
except FileNotFoundError:
    print("An I/O error has been generated.") 
except ValueError:
    print("That is not a number")
