from typing import Any


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
        
    def append(self, data):
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
        #solution steps[1] [2] [3] [4]
        
        new_node : Node = Node(data)
        existing_node_next = existing_node.next
       
        existing_node.next = new_node
        new_node.next = existing_node_next
            
            
        #create a new node with data given
        #set new node as next of existing node
        #set the initial next of the existing as the next of the newly created node


    


#initialise a Linked List
l = LinkedList() 
l.append(1)
l.append(2)
l.append(3)
node = l.append(4)
l.append(5)


l.insert_after_node(node, 99)
l.insert_after_node(l.head.next, 900)
# l.prepend(4)
#create a node
# node = Node(99)

l.print_list()