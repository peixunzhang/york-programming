#Activity 5: Functions
#Exercise 1
from turtle import backward
def sentenceCount():
    sentence = str(input("Write a sentence: "))
    splited = list(sentence)
    a = []
    e = []
    i = []
    o = []
    u = []
    other = 0
    for char in splited:
        if char == 'a':
            a.append("*")
        elif char == 'e':
            e.append("*")
        elif char == 'i':
            i.append("*")
        elif char == 'o':
            o.append("*")
        elif char == 'u':
            u.append("*")
        elif char != " ":
            other = other + 1

    return (f"A: {a}\nE: {e}\nI: {i}\nO: {o}\nU: {u}\nOther (non-space) Characters: {other}")
print(sentenceCount())
# exercise 2
def isAnagram():
    originWord = str(input("Enter word: "))
    reversed = originWord[::-1]
    if originWord == reversed:
        print("These are anagrams")
    else: print("These are not anagrams")

if __name__ == "__main__":
    isAnagram()
#exercie 3
def sORq():
    # stack
    myList = []
    while(True):
        structure = int(input("Enter 1 for stack 2 for queue: "))
        if structure == 1:
            action = int(input("Pick an action for stack, 1 for push, 2 for pop, 3 for view: "))
            if action == 1:
                myItem = input("Push an item to the list: ")
                myList.append(myItem)
            elif action == 2:
                last = len(myList)
                myList.pop(last-1)
            elif action == 3:
                print(myList)
            else: print("wrong input")
        elif structure == 2:
            # queue
            myListq = []
            while(True):
                action = int(input("Pick an action for queue, 1 for push, 2 for pop, 3 for view: "))
                if action == 1:
                    myItem = input("Push an item to the list: ")
                    myListq.append(myItem)
                elif action == 2:
                    myListq.pop(0)
                elif action == 3:
                    print(myListq)
                else: print(myListq)
sORq()
