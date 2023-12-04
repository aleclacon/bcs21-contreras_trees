'''
stack using Linked list
Class Node:
 def __init__(self, data):
 self.data = x
 self.next = None
Class Stack:
 def __init___(self):
 self.top = None
Top
Operations
 push - insertion at the beginning
 pop - deletion from the beginning
Insertion
 - Case 1
 - stack is Empty (Top is None)
 - new = Node(10)
 - self.Top = new
   Top.next = None
 - Case 2
 - stack is not Empty
 - new = Node(20)
  new.next = top
  top = new
  new = Node(30)
  top = top.data
Deletion
 - Case 1
 - stack is empty
 if top is None:
 print("Stack is empty")
 - Case 2
 - stack with single element
 if top.next is None:
 top = None
 - Case 3
 - stack with more than one element
 temp = top
 top = temp.next
 temp = None
Display
 - Case 1
 - stack is empty
 if top is None"
 print("Empty Stack")
 - Case 2
 temp = top
 while temp
 print(temp.data)
 temp = temp.next
------------------------------------------------------------------
Title: Palindra-palooza
Objectives:
- Implement modifications to the existing palindrome checker to handle palindromes in sentences, considering spaces, punctuation, and capitalization.
The challenge of extending the palindrome checker to handle sentences involves addressing additional complexities introduced by spaces, punctuation, and capitalization within the input text. Unlike single-word palindromes, sentences may contain various characters that need special consideration.
Palindrome is a sequence of charaters that read the same forward as backward.
 ex: radar, level, deed, noon
 "Able was I ere I saw Elba"
 "Madam, in Eden, I'm Adam"
 "Was it a car or a cat I saw"
Let's break down the key challenges:
Spaces: Sentences may contain spaces between words. In a sentence palindrome, spaces should be ignored when determining whether the sentence reads the same forward and backward.
Punctuation: Sentences often include punctuation marks (e.g., commas, periods, exclamation points). For a sentence to be recognized as a palindrome, these punctuation marks need to be treated appropriately. In the example "A man, a plan, a canal, Panama!", the commas are part of the palindrome and should not be ignored.
Capitalization: The palindrome checker should be case-insensitive. Uppercase and lowercase letters should be considered equivalent. In the example "A man, a plan, a canal, Panama!", the capitalization is mixed, and the palindrome checker should correctly handle this variation.
Example: "A man, a plan, a canal, Panama!"
Original Sentence: "A man, a plan, a canal, Panama!"
Cleaned Sentence (for comparison): "amanaplanacanalpanama"
Expected Result: The sentence is a palindrome because it reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
Rubrics for Evaluation:
- Correctness (60 points): 
 - Assess the correctness of the implementation, considering all aspects of the specified challenges and on time.
- Efficiency (15 points): 
 - Evaluate the efficiency of the solutions, especially in the case of the efficiency improvement challenge.
- Creativity and Innovation (15 points): 
 - Assess the creativity and innovation demonstrated in addressing the challenges.
- Documentation and Comments (5 points):  
 - Evaluate the clarity and completeness of comments and documentation in the code.
- Discussion and Reflection (5 points): 
 - Evaluate the depth and quality of the discussions and reflections provided by the student.
-- Note for each day of late submission, there is a deduction of 10 points
'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        x = int(input("\nEnter element to be inserted into Stack: "))
        new_node = Node(x)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is EMPTY")
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
                temp = temp.next
            print("\nTop if the stack is ", self.top.data)
            print("--------------------")


def isPalindrome(data):
    ibabalik = ''.join(char.lower() for char in str(data) if char.isalnum())
    return ibabalik == ibabalik[::-1]


s = Stack()
print("ACTIVITY NAME: palindra-palooza.py")
print("\nWelcome to our modified Palindrome Checker"
        "\n\nMade by Contreras, Aleianna Clarisse C.")
while True:
    choice = input("\n[1] - Input to Palindrome Checker\n[2] - Exit\n\nChoice: ")
    if choice == "1":
        
            inputs = input("\nInput Sentence: ")
            inputr = isPalindrome(inputs)

            if inputr is isPalindrome:
                print(f"\nRESULT: The user input '{inputs}' is a Palindrome")
                
            else:
                print(f"\nRESULT: The user input '{inputs}' is NOT a Palindrome")
                

    elif choice == "2":
        print("Thank you for using our Palindroma Checker")
        print("\nMade by CONTRERAS, Aleianna Clarisse C. from BCS21"
            "\nThank you so much and God bless")
        break
    else: 
        print("\nThat is an invalid input. Please try again.")
        
            
 # print("Thank you for using our Palindroma Checker")
    # print("\nMade by CONTRERAS, Aleianna Clarisse C. from BCS21"
    #             "\nThank you so much and God bless")

    # print("Welcome to our modified Palindrome Checker"
#       "\nMade by Contreras, Aleianna Clarisse C.")