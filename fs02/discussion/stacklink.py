class Node:
    def __init__(self,x):
        self.data= x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        x = int(input("\nEnter element to be inserted into Stack: "))
        new = Node(x)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next=self.top
            self.top = new

    def pop(self):
        if self.top is None:
            print("STack is EMPTY")
        elif self.top.next is None:
            print("\nDeleted element is: ", self.top.data)
            print("--------------------")
            self.top = None
        else:
            temp = self.top
            print("Deleted element is: ", self.top.data)
            print("--------------------")
            self.top = temp.next
            temp = None
    def display(self):
        if self.top is None:
            print("\nStack is empty")
            print("--------------")
        else:
            print("\nElement of the Stack: \n")
            temp = self.top
            while temp:
                print(temp.data)
                temp =temp.next
            print("\nTop if the stack is ", self.top.data)
            print("--------------------")
s = Stack()
while(1):
        print("Choose the operation you would like to do: ")
        print("\n1 - Insert (Push) \n 2 - Delete (Pop) \n 3 - Show \n 4 - Exit")

        
        option = int(input())
        if option == 1:
            print("\nInsert (Push) Operation")
            print("-----------------------")
            s.push()
        elif option == 2:
            print("\nDelete (Pop) Operation")
            print("-----------------------")
            s.pop()
        elif option == 3:
            print("\nShow the Stack")
            print("-----------------------")
            s.display()
        else:
            break




