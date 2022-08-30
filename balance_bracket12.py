#implement stack
from balance_brackets import is_match


class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def match(p1,p2):
    if p1=="(" and p2==")":
        return True
    elif p1=="{" and p2=="}":
        return True 
    elif p1=="[" and p2=="]":
        return True
    else:
        return False

def check_balance(passed_string):
    s =  Stack()
    balanced =True
    index = 0
    opening_brackets = "({["
    while index < len(passed_string) and balanced:
        #moving thru all strings
        current_string = passed_string[index]
        if current_string in opening_brackets:
            s.push(current_string)
        else:
            if s.is_empty():
                balanced = False
                break
            else:
                #compare
                top = s.pop()
                if not is_match(top, current_string):
                    balanced =  False
                    break
        index += 1

                    
    if s.is_empty() and balanced:
        return True
    else:
        return False
            
        