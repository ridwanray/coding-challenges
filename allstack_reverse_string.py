#reverser st ring 2 using Stack through out
#step to solution
#implement stack
#for item in string, push to a stack
# for the new stack pop and push to a stack 
class Stack():
    def __init__(self):
        self.items = []
        
    def push(self,value):
        self.items.append(value)
        
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
        
    def display_stack(self):
        print("Stack content", self.items)

def reverse_string(stack: Stack, strings: str):
    s = Stack()
    for i in strings:
        s.push(i)
    
    reversed_str =""
    while not s.is_empty():
        reversed_str += s.pop()
    return reversed_str

import unittest
class ReverseStringsTests(unittest.TestCase):

    def test_1(self):
        returned = reverse_string(Stack,"abcd")
        self.assertEqual(returned,"dcba")
    
    def test_2(self):
        returned = reverse_string(Stack,"123456")
        self.assertEqual(returned,'654321')
    
    def test_3(self):
        returned = reverse_string(Stack,"ade")
        self.assertEqual(returned,"eda")
    
    def test_4(self):
        returned = reverse_string(Stack,"!evitacudE ot emocleW")
        self.assertEqual(returned,"Welcome to Educative!")
        
        
        
if __name__ == '__main__':
    unittest.main()