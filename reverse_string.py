#Reverse a string using stack
#Solution Step
#implement a Stack
#get last item from items list i.e.
#push the item as first into stack

class Stack():
    def __init__(self):
        self.items = ""
        
    def push(self,value):
        self.items += value
        
    def pop(self):
        return self.items.pop()
    
    def display_stack(self):
        print("Stack content", self.items)
    
def reverse_string(strings):
    s = Stack()
    #convert string to list
    converted= list(strings)

    for i in range(0, len(strings)):
        item = converted.pop()
        s.push(item)
    return s.items

import unittest
class ReverseStringsTests(unittest.TestCase):

    def test_1(self):
        returned = reverse_string("abcd")
        self.assertEqual(returned,"dcba")
    
    def test_2(self):
        returned = reverse_string("123456")
        self.assertEqual(returned,'654321')
    
    def test_3(self):
        returned = reverse_string("ade")
        self.assertEqual(returned,"eda")
    
    def test_4(self):
        returned = reverse_string("!evitacudE ot emocleW")
        self.assertEqual(returned,"Welcome to Educative!")
        
        
        
if __name__ == '__main__':
    unittest.main()
    