# You can remove 'pass' if you written code in the function
# Each node is a list: [Data, Pointer]. A pointer of -1 means "points to nothing".
from tkinter.constants import CURRENT

# Exercise 1



def IsEmpty():
    if FirstNode==-1:
        return False
    else:
        return True
def IsFull():
    if FirstEmpty==-1:
        return True
    else:
        return False

# Exercise 2
def Traverse():
    Output=[]
    CurrentPionter = FirstNode
    for i in range (8):
        if CurrentPionter!=-1:
            Output.append(LinkedList[CurrentPionter][0])
            CurrentPionter = LinkedList[CurrentPionter][1]
        else:
            break
    return Output





# Exercise 3
def Search(Item):
    CurrentPionter = FirstNode
    while CurrentPionter != -1:
        if LinkedList[CurrentPionter][0]==Item:
            return CurrentPionter
        else:
            CurrentPionter = LinkedList[CurrentPionter][1]
    return -1




def CountNodes():
    count=0
    CurrentPionter = FirstNode
    for i in range (8):
        if CurrentPionter!=-1:
            count+=1
            CurrentPionter = LinkedList[CurrentPionter][1]
        else:
           break
    return count

# Exercise 4
def InsertFront(Item):
    global LinkedList, FirstNode, FirstEmpty
    if FirstEmpty == -1:
        return False
    else:
        NewNode = FirstEmpty
        FirstEmpty = LinkedList[NewNode][1]
        LinkedList[NewNode][0] = Item
        LinkedList[NewNode][1] = FirstNode
        FirstNode = NewNode
        return True

# Exercise 5
def InsertEnd(Item):
global LinkedList, FirstNode, FirstEmpty
    if FirstEmpty == -1:
        return False
    NewNode = FirstEmpty
    FirstEmpty = LinkedList[NewNode][1]
    LinkedList[NewNode][0] = Item
    LinkedList[NewNode][1] = -1
    if FirstNode == -1:
        FirstNode = NewNode
    else:
        CurrentPointer = FirstNode
        while LinkedList[CurrentPointer][1] != -1:
            CurrentPointer = LinkedList[CurrentPointer][1]
        LinkedList[CurrentPointer][1] = NewNode
    return True


# Exercise 6
def Delete(Item):
    global LinkedList, FirstNode, FirstEmpty
    PreviousPointer = -1
    CurrentPointer = FirstNode
    while CurrentPointer != -1 and LinkedList[CurrentPointer][0] != Item:
        PreviousPointer = CurrentPointer
        CurrentPointer = LinkedList[CurrentPointer][1]
    if CurrentPointer == -1:
        return False
    if PreviousPointer == -1:
        FirstNode = LinkedList[CurrentPointer][1]
    else:
        LinkedList[PreviousPointer][1] = LinkedList[CurrentPointer][1]
    LinkedList[CurrentPointer][0] = -1
    LinkedList[CurrentPointer][1] = FirstEmpty
    FirstEmpty = CurrentPointer
    return True
