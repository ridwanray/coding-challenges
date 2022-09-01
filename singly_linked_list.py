from operator import le
from typing import Any


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, data):
        #time complexity:O(n)
        #since we need to go thru
        new_node = Node(data)
        #if head is empty, use this node as the head
        if self.head is None:
            self.head = new_node
            return
        #find last_node and set new node as next
        #solution steps
        #go thru nodes untill where next is none
        ##reference that node as the next of this node 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node
        
        return new_node
        
    def print_list(self):
        current_node = self.head
        list_data =[]
        while current_node:
            # print(current_node.data)
            list_data.append(current_node.data)
            current_node = current_node.next
            
        print(list_data)
    def prepend(self,data):
        #time complexity:O(1), constant time
        #solution steps
        #create a new node
        #set new node as head if head is None
        #find the linkedlist head
        #set the current node as head
        #set next of the current node as the initial node
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        initial_head = self.head
        self.head = new_node
        new_node.next = initial_head
        
        return 
        
    def insert_after_node(self,existing_node:Node, data:Any):
        #time complexity:constant time->O(1)
        #solution steps[1] [2] [3] [4]
        #create a new node with data given
        #set new node as next of existing node
        #set the initial next of the existing as the next of the newly created node
        if type(existing_node) != Node:
            raise ValueError("Previous node must be a node instance!")
        new_node : Node = Node(data)
        existing_node_next = existing_node.next
       
        existing_node.next = new_node
        new_node.next = existing_node_next
    def delete_by_value(self, value):
        #[1] [2]  [3] [4] [5] 
        #solution steps
        #idenfity the head of the LinkedList
        #move through the List and check for data match
        #If match occurs:
        #       when match occurs at a node...
        #       pick the previous node 
        #       set the previous node next to be the next of the match
        
        prev_node = None
        head = self.head
        if head and head.data == value:
            self.head =  None
            return
        
        while head:
            if head.data == value :
                prev_node.next = head.next
                head = prev_node.next
            else:
                prev_node = head
                head = head.next
                
        return
    def delete_by_position(self, position):
        #solution steps [1] [2] [3] [4]
        #handle edge case of position being 0
        #1. validate input: Expect only +ve interger
        #2 initialize count to be -1
        #3.on getting to a match
        #4.     set prev_node next to be d current/match node next 
        #5. if position is passed as zero, set the next node as 
        
        #validate position
        if position < 0: raise ("Postion cannot be less thank 0")
        

        
        prev_node = None
        index = -1
        head = self.head
        
        #handle edge case of position Zero
        if head and position == 0:
            self.head = head.next
            return
        
        while head:
            index += 1
            if index == position:
                prev_node.next = head.next
                head = prev_node.next
            else:
                prev_node = head
                head = head.next
                
    def leng(self) -> int:
    
        #solution steps
        #identify the head of the LinkedLIst
        #move through the list and count till where Node next is empty i.e. end
        
        head = self.head
        if not head:
            return 0
        
        count = 0
        while head:
            count += 1
            head = head.next
        return count

        
    def count(self, head):
        lenght = 1
        head = head
        if head.next == None:
            return lenght
        else:
            head= head.next
            value = self.count(head)
            lenght += value
                

            
        return lenght
        
        
# Test recursive  LinkedList count
l = LinkedList() 
l.append(99)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.append(100)
l.append(2)
l.append(8)
l.append(5)
l.append(2)
l.append(10)
l.append(2)
l.append(99)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.append(100)
l.append(2)
l.append(8)
l.append(5)
l.append(2)
l.append(10)
l.append(2)
value = l.count(l.head)
print("my lenght", value)
                            




                
# #Test count LinkedList
# l = LinkedList() 
# l.append(99)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# l.append(6)
# l.append(100)
# l.append(2)
# l.append(8)
# l.append(5)
# l.append(2)
# l.append(10)
# l.append(2)
# l.append(99)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# l.append(6)
# l.append(100)
# l.append(2)
# l.append(8)
# l.append(5)
# l.append(2)
# l.append(10)
# l.append(2)
# value = l.leng()
# print("my lenght", value)
                







            
# #Test delete by position
# l = LinkedList() 
# l.append(99)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# l.append(6)
# l.append(100)
# l.append(2)
# l.append(8)
# l.append(5)
# l.append(2)
# l.append(10)
# l.append(2)
# l.delete_by_position(0)
# # print("is deleted", is_deleted)
# l.print_list()
                
                
# #Test delete by value
# l = LinkedList() 
# l.append(100)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# l.append(6)
# l.append(100)
# l.append(2)
# l.append(8)
# l.append(5)
# l.append(2)
# l.append(10)
# l.append(2)
# l.delete_by_value(100)
# # print("is deleted", is_deleted)
# l.print_list()



#initialise a Linked List
#Test append and insert
# l = LinkedList() 
# l.append(1)
# l.append(2)
# l.append(3)
# node = l.append(4)
# l.append(5)


# l.insert_after_node(node, 99)
# l.insert_after_node(l.head.next, 900)
# l.print_list()