#implement a stack
#balance brackets
#Steps to determine if string is balance
#1. go thru the strings to look for opening bracket

class Stack():
    def __init__(self):
        self.items = []
    
    def push(self,value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:

            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

import unittest
class CountLowHighTests(unittest.TestCase):

    def test_1(self):
        returned = is_paren_balanced("]{")
        self.assertEqual(returned,False)
    
    def test_2(self):
        returned = is_paren_balanced("{{")
        self.assertEqual(returned,False)
    
    def test_3(self):
        returned = is_paren_balanced("(((({}))))")
        self.assertEqual(returned,True)
        
        
        
if __name__ == '__main__':
    unittest.main()