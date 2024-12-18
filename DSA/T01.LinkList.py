from typing import Optional
class Node:
    def __init__(self, data:int, next:Optional['Node']=None):
        self.data:int = data
        self.next:Optional['Node'] = next
class LinkedList:
    def __init__(self):
        self.head:Optional['Node'] = None
        self.size:int = 0
        
    def insertion(self, data:int):
        if not self.head:
            self.head =  Node(data, self.head)
        else:
            node = Node(data)
            current = self.head
            while(current.next):
                current = current.next
            current.next = node
            self.size+=1

    def create_cycle(self, position:int):
        current = tail = self.head
        index = 0
        while tail.next:
            tail = tail.next # tail is last
        while index < position:
            index+=1
            current = current.next
        tail.next = current    

    def display_cycle(self, limit:int):
        print("---display_cycle---")
        # limit = limit if limit is not None else self.size
        current = self.head
        index = 0
        while index <= limit:
            index+=1
            print(current.data)
            current = current.next

    # Floyd's Cycle Detection Algorithm
    # Also known as Tortoise and Hare Algorithm
        # is an efficient approach to detect a cycle in a linked list
    def detect_cycle_link_list(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                print("list is a cyclic")
                return True
        print("No Cycle")
        return False
    
    def create_circular_link_list(self):
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = self.head
    def display_circular_link_list(self, limit:int):
        index = 0
        current = self.head
        while index < limit:
            index+=1
            print(current.data)
            current = current.next



    def delete(self, index):
        if index < 0 or index >= self.size or not self.head:
            print("Error: index is not correct")
            return False
        if index == 0:
            print(self.head.data)
            return True
        count = 0
        prev = None
        current = self.head
        while(count < index):
            count+=1
            prev = current
            current = current.next
        prev.next = current.next
        
    def display(self):
        print("---Data---")
        current = self.head
        while(current):
            print(current.data)
            current = current.next
            
list = LinkedList()
list.insertion(15)
list.insertion(25)
list.insertion(26)
list.insertion(31)
list.insertion(32)
list.insertion(35)

list.display()

# list.create_cycle(2)
# list.display_cycle(20)
list.detect_cycle_link_list();

# list.create_circular_link_list()
# list.display_circular_link_list(20)

# list.delete(4)
# list.display()

# Types of Linked Lists
# Singly Linked List: Each node points to the next node; ends with None (no cycle).
# Cyclic Linked List: A general term for any linked list with a loop where a next pointer references an earlier node.
# Circular Linked List: A type of cyclic linked list where the tail node points directly back to the head node.


# Problems Related to Singly Linked List
# Reverse a Singly Linked List