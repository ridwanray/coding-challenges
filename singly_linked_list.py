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
        count = 0
        while current_node:
            # print(current_node.data)
            list_data.append(current_node.data)
            current_node = current_node.next 
            count +=1
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

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def count(self, head):
        lenght = 1
        if head.next == None:
            return lenght
        else:
            head= head.next
            # value = self.count(head)
            lenght = lenght + self.count(head)
                

            
        return lenght
    def node_swap(self,first=None, second= None):
        # [1] [2 [3] [4] [5] [6]
        #solution steps
        #Accept two nodes data as parameters
        #Identify the head of the LinkedList
        #Move thru the list to find the nodes
        #swap their pointers(previous node and next node) 
        
        #validate input
        if not first or not second:
            raise ValueError("Put two data to swap")
        
        #initialize two nodes
        first_node = None
        second_node = None
        
        first_node_prev = None
        second_node_prev = None
        
        previous_node = None
         
        current_node = self.head
        
        while current_node:
            if current_node.data == first:
                first_node = current_node
                first_node_next = current_node.next
                first_node_prev = previous_node
                previous_node = current_node
                current_node = current_node.next
                
            elif current_node.data == second:
                second_node = current_node
                second_node_next = current_node.next
                second_node_prev = previous_node
                previous_node = current_node
                current_node = current_node.next
                           
            else:
                previous_node = current_node
                current_node = current_node.next
                
        if not first_node or not second_node: raise ValueError(f"Some nodes where not found in List")
        
        #swap Node prev and next pointer
        ## [1] [2] [3] [4] [5] [6]
        #      [5]         [2] 

        #handle consecutive nodes

        if first_node_next == second_node:
            if first_node_prev is None:
                self.head = second_node
                second_node.next = first_node
                first_node.next = second_node_next
            else:
                
                first_node_prev.next = second_node
                second_node.next = first_node
                first_node.next = second_node_next
            
        
        else:
            second_node_prev.next =  first_node
            first_node.next = second_node_next
            if first_node_prev is None:
                self.head = second_node
                second_node.next = first_node_next
               
            else: 
                first_node_prev.next = second_node
                second_node.next = first_node_next
        
        return  
    
    def edu_swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return 

        prev_1 = None 
        curr_1 = self.head 
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1 
            curr_1 = curr_1.next

        prev_2 = None 
        curr_2 = self.head 
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2 
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return 

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next
        
    def reverse_linked_list(self):
        #solution steps
        #[1] [2] [3] [4] [5] [6] => [6] [5] [4] [3] [2] [1]
        #identify the head
        #move through the list
        #for every node, set the its previous node as the next
        #move through the list
        #set the its previous node as the next until th
        current_node:Node  = self.head
        if not current_node: raise ValueError("List is empty. head is None!")
        
        prev_node = None
        while current_node:
                nxt = current_node.next
                current_node.next = prev_node
                
                
                prev_node = current_node
                current_node = nxt
              
        self.head = prev_node
    
    def reverse_recursive(self):
        #solution steps
        #[1] [2] [3] [4] [5] [6] => [6] [5] [4] [3] [2] [1]
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)
        
    
    def merge_two_linkedlist(self, l2:'LinkedList'):
        #solution steps 
        #1. Accept 2 lists as parameter
        #identify 1st list head
        #2. move till the end of first list
        #3  set the next node of l1 end to head to second list
        # [1] [2] [3] [4]    [5] [6] [7] [8]
        current_node = self.head
        prev_node = None
        while current_node:
            prev_node = current_node
            current_node =  current_node.next
            
        prev_node.next = l2.head  
        
    def merge_two_sorted_lists(self, l2:'LinkedList')->Any:
        #solution steps
        #1. get the head of both LinkedList, i.e. p and q
        #2. compare their respective data and make s point to smaller
        #3. if the lower is in p, new p points to next node in p
        #4. otherwise new q points to next node in q
        #5. repeat step 2 to 4 until either p or q is null, then s points to the one
        #that is not null
                

        merged = LinkedList() #initialize Linkedlist to hold final merge list
        
        p = self.head
        q = l2.head
        
        p_data = p.data
        q_data = q.data
        
        smaller_value = p_data if p_data < q_data else q_data #get the smaller value
        
        head = p if smaller_value == p.data else q   #get the node of the smaller value
 
        merged.head = head       #set the head of the final LinkedList
       
        if smaller_value == p.data:
            p = p.next
        else:
            q = q.next
        prev_node = head
        while p or q:
            
            if not q or not p: #handle case when a list has reach end, just copy remain list content accordingly
                if p:
                    prev_node.next = p
                    break
                   
                if q:
                    prev_node.next = q
                    break
            
            p_data = p.data
            q_data = q.data

            smaller_value = p_data if p_data < q_data else q_data
            smaller_node = p if smaller_value == p.data else q
            prev_node.next = smaller_node
            
            
            if smaller_value == p.data:
                prev_node = p
                p = p.next
            else:
                prev_node = q
                q = q.next
        
    
        merged.print_list()


    
    def edu_merge_sorted(self, llist):

        p = self.head 
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.data <= q.data:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p

        self.head = new_head     
        return self.head
      
    def edu_remove_duplicate(self):
        #solution step
        cur = self.head 
        prev_node = None
        
        dup = dict()
        
        while cur:
            
            if cur.data in dup:
                # Remove node:
                prev_node.next = cur.next
                cur = None
                
            else:
                # Have not encountered element before.
                dup[cur.data] = 1
                prev_node = cur
            
            cur = prev_node.next
                
    def nth_to_last_node(self, n : int):
        #[1] [2] [3] [4] [5] [6] [7]
        #solution steps
        #accept postion as parameter
        #identify node head
        #go through the list untill the postion is reach
        #set it as the head

        
        if n <= 0:raise ValueError("Position starts from 1")
        cur = self.head
        init_position = 0
        while cur :
            init_position += 1
            if init_position == n:
                self.head = cur
                break
            else:
                cur = cur.next
                
    def print_nth_from_last(self, n):
        total_len = self.count()
  
        cur = self.head 
        while cur:
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
            return         
    def count_number_of_occurence_iterative (self, data):
        #interative method 
        #solution steps
        #accepts data to search as parameter
        #identify the head of the node
        #move thru the list, for every occurence, increment count
        cur = self.head
        count = 0
        
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        
        return count
    
    def recursive_count_occurence(self, data, cur):    
        count = 0
        
        if cur is None:
            return 0
        
        if cur.data == data:
            count += 1
        cur = cur.next
        count = count + self.recursive_count_occurence(data, cur)     
        return count
    
    def count_occurences_recursive(self, node, data):
        if not node:
            return 0 
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)
                
        
#Test occurence iterative
l1 = LinkedList() 
l1.append(30)
l1.append(35)
l1.append(50)
l1.append(70)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(30)
l1.append(75)
l1.append(75232)
l1.append(75232)
x = l1.recursive_count_occurence(30, l1.head)
y = l1.count_number_of_occurence_iterative(30)
print("recursive value", x)
print("iterative value", y)


#Test nth to last node
# l1 = LinkedList() 
# l1.append(30)
# l1.append(35)
# l1.append(50)
# l1.append(70)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(75)
# l1.append(75232)
# l1.append(75232)
# l1.nth_to_last_node(13)
# l1.print_list() 


#Test remove duplicates in List

# l1 = LinkedList() 
# l1.append(30)
# l1.append(35)
# l1.append(50)
# l1.append(70)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(30)
# l1.append(75)
# l1.append(75232)
# l1.append(75232)
# l1.edu_remove_duplicate()
# l1.print_list() 



#Test merge sorted list

# l1 = LinkedList() 
# l1.append(30)
# l1.append(35)
# l1.append(50)
# l1.append(70)
# l1.append(75)

# l2 = LinkedList()
# l2.append(20)
# l2.append(48)
# l2.append(80)
# l2.append(90)
# l2.append(100)
# l2.append(200)
# l2.append(300)
# l2.append(400)

# l1.merge_two_sorted_lists(l2)
# l1.print_list()    
    
#p [1] [5] [7] [9] [10]
#q  [2] [3] [4] [6] [8]








   
# #Merge two sorted list test  
# l1 = LinkedList() 
# l1.append(1)
# l1.append(2)
# l1.append(3)
# l1.append(4)
# l1.append(4)

# l2 = LinkedList()
# l2.append(5)
# l2.append(6)
# l2.append(7)
# l2.append(8)
# l2.append(9)

# l1.merge_two_sorted_linkedlist(l2)
# l1.print_list()    

# #Recursively reverse linked list          
# l = LinkedList() 
# l.append(1)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# l.append(6)
# l.append(7)
# l.append(8)
# l.append(9)
# l.append(10)
# l.append(11)
# l.append(12)
# # l.append(13)
# l.reverse_recursive()
# l.print_list()    
    
        
        
#Test reverse linked list:iteration method    
# l = LinkedList() 
# l.append(1)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# l.append(6)
# l.append(7)
# l.append(8)
# l.append(9)
# l.append(10)
# l.append(11)
# l.append(12)
# l.append(13)
# l.reverse_linked_list()
# l.print_list()    
    
    
        
# # Test rswap
# l = LinkedList() 
# l.append(1)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# l.append(6)
# l.append(7)
# l.append(8)
# l.append(9)
# l.append(10)
# l.append(11)
# l.append(12)
# l.append(13)
# l.node_swap(1,2)
# l.print_list()
    
# # Test recursive  LinkedList count 
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
# value = l.count(l.head)
# print("my lenght", value)
                            
 
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