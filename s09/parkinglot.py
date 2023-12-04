'''
Main Activity
 Create a parking lot simulation using Queue in python avoid using libraries and methods but instead create your own methods/functions
 Submission: GitHub link  and screenshot ng result
 
 Deadline On or before Thursday Nov 30 at 11:00 am
'''
class Node:
    def __init__(self,data= None):
        self.data = data 
        self.next = None
class Queue:
    def __init__(self,capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        
    def enqueue(self,value):
        if self.slot() < self.capacity:
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
                print(f"Vehicle '{value}' has been parked.")
            else:
                self.tail.next = new_node
                self.tail = new_node
                print(f"Vehicle '{value}' has been parked.")
        else:
            print("The parking lot is full. No more slots available.")
    def dequeue(self):
        if self.head is None:
            print("No vehicles in the parking lot.")
            return None
        else:
            removed_node = self.head
            self.head = self.head.next
            return removed_node.data
        

    def flow(self):
        if self.slot() < self.capacity:
            x = self.capacity - self.slot()
            print(f"! ATTENTION : THERE ARE {x} SLOTS LEFT !")
        elif self.slot() == self.capacity:
            print("! ATTENTION : THE PARKING LOT IS FULL !")
        else:
            print("! ATTENTION : ALL SLOTS IN THIS PARKING LOT ARE AVAILABLE !")


	 
    def status(self):
        print(f"Number of occupied slots: {self.slot()} / {self.capacity} \n", end="")
        for _ in range(self.slot(), self.capacity):
            print("| | ", end=" ")
        print()
         #print(f"Number of occupied slots: {self.slot} {self.slot} {self.slot} {self.slot} {self.slot} {self.slot} {self.slot} {self.slot}")
         #(self.slot(), self.capacity))
    def slot(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count 
    

    def print_queue(self):
        if self.head is None:
            print("! ATTENTION : ALL SLOTS IN THIS PARKING LOT ARE AVAILABLE !")
        else:
            print("\n >>> NOW PARKING <<<")
            current_node = self.head
            while current_node:
                print(f"Parking Slot: {hex(id(current_node.next))}", current_node.data)
                #print(f"current_node.data, next: {hex(id(current_node.next))}")
                current_node = current_node.next
        print()














queue = Queue(8)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>START<<<<<<<<<<<<<<<<<<<<<<\n\n\n")
print("MESSAGE: Good Morning, De La Salle University-Dasmarinas!")

queue.flow()
queue.status()

print("_____________________________________________\n")
print("\nTIME AND DATE: 7:00 AM - Monday, 20 November 2023")
queue.enqueue("MKL - Red")
queue.print_queue()
queue.status()
queue.flow()
print("_____________________________________________")


print("\n\nTIME AND DATE: 7:45 AM - Monday, 20 November 2023")
queue.enqueue("NJM - Pink")
queue.enqueue("LJN - Blue")
queue.enqueue("LHC - Yellow")
queue.print_queue()
queue.status()
queue.flow()

print("_____________________________________________")



print("\n\nTIME AND DATE: 8:05 AM - Monday, 20 November 2023")
print(f"PARKING STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}\n")
#queue.print_queue()


queue.status()
queue.flow()
print("_____________________________________________")


print("\n\nSTATUS: 9:05 AM - Monday, 20 November 2023")
print(f"PARKING STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}")
print(f"PARKING STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}")
print(f"PARKING STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}\n")
queue.print_queue()
queue.status()
queue.flow()

print("_____________________________________________")


print("\n\nSTATUS: 9:59 AM - Monday, 20 November 2023")
queue.enqueue("MKL - Red")
queue.enqueue("NJM - Pink")
queue.enqueue("LJN - Blue")
queue.enqueue("LHC - Yellow")
queue.enqueue("ZCL - Purple")
queue.enqueue("HRJ - Orange")
queue.enqueue("PJS - Black")
#queue.enqueue("JJH - Pink")
queue.enqueue("ACC - Magenta Pink")
queue.print_queue()

queue.status()
queue.flow()

print("_____________________________________________")


print("\n\nSTATUS: 9:59 AM - Monday, 20 November 2023")
print("ENTERING: {x}")
x="KMG - White"
queue.enqueue("KMG - White")
queue.flow()
queue.status()
#queue.print_queue()
print("_____________________________________________")


print("\n\nSTATUS: 8:30 PM - Monday, 20 November 2023")
print(f"STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}")
print(f"STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}")
print(f"STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}")
print(f"STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}")
print(f"STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}")
print(f"STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}")
print(f"STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}")
print(f"STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}\n")
#print(f"STATUS:( {queue.dequeue()} ) LEFT SLOT {queue.slot()}")
queue.flow()
queue.status()
print("_____________________________________________")

print("\n\n>>>>>>>>>>>>>>>>>>>>>>>END<<<<<<<<<<<<<<<<<<<<<<\n")
print("MESSAGE: Good Night, De La Salle University-Dasmarinas!")

'''
kalat dump
queue = Queue(8)
print("MESSAGE: Good Morning, De La Salle University-Dasmarinas!")
queue.flow()
queue.status()

#pasok muna mk then pasok tatlo, labas isa, tas pasok 4
print("\nSTATUS: 7:00 AM - Monday, 20 November 2023")
queue.enqueue("MKL - Red")
queue.print_queue()
#queue.status()
#queue.print_queue()
#queue.slot()
#queue.status()

queue.flow()
queue.status()
print("\nSTATUS: 7:45 AM - Monday, 20 November 2023")
# queue.flow()
# queue.status()
queue.enqueue("NJM - Pink")
queue.enqueue("LJN - Blue")
queue.enqueue("LHC - Yellow")
queue.print_queue()


queue.enqueue("LJN - Blue")
queue.enqueue("LHC - Yellow")
queue.enqueue("ZCL - Purple")
queue.enqueue("HRJ - Orange")
queue.enqueue("PJS - Black")
queue.enqueue("ACC - Magenta Pink")
queue.print_queue()
queue.flow()

print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
queue.flow()
queue.print_queue()



   def print_queue(self):
        if self.head is None:
            print("! ATTENTION : ALL SLOTS IN THIS PARKING LOT ARE AVAILABLE !")
        else:
            
            print("\n >>> NOW PARKING <<<")
            current_node = self.head
            while current_node:
                print(f"Parking Slot: {hex(id(current_node.next))}", current_node.data)
                #print(f"current_node.data, next: {hex(id(current_node.next))}")
                current_node = current_node.next
        print()




    def enqueue(self,value):
        if self.slot() < self.capacity:
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
                print(f"Vehicle '{value}' has been parked.")
            else:
                self.tail.next = new_node
                self.tail = new_node
                print(f"Vehicle '{value}' has been parked.")
        else:
            print("The parking lot is full. No more slots available.")
'''






