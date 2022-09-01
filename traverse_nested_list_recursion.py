#Recursive algo to traverse a nested list 
# i.e. get the leaf items
#solution steps
#1.move through the list items
#if a leave is found, add it to a container
#if a sublist is found:
#   jump into the sublist, and similarly move thru the items
#   do this until 
#          
from operator import le
from typing import Any, List


names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

def retrieve_leafs(passed_list:Any) -> List:
    length: int = len(passed_list)
    final_leafs = []
    
    for i in range(0, length):
        present_item = passed_list[i]
        
        #breaking condition
        if isinstance(present_item, str):
            final_leafs.append(present_item)
        else:
            x = retrieve_leafs(present_item)
            final_leafs.extend(x)
           
    
    return final_leafs
            
x = retrieve_leafs(names)       
     
print("finalee", x)
                
                
                
        



# def retrieve_leafs(passed_list: List)->List:
#     list_leng: int =  (len(passed_list))
#     #handle edge case
    
#     leaf_elements = []
#     if list_leng == 0:
#         return []
    
#     def get_leafs():
        
#         pass
    
#     for i in range(0, list_leng):
#         item = passed_list[i]
#         if isinstance(item, str):
#             leaf_elements.append(item)
#         else:
#             leafs = get_leafs()
#             leaf_elements.extend(leafs)
    
#     print("leaf", leaf_elements)
        
# retrieve_leafs(names)