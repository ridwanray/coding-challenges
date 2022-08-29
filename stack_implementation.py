#Stack Implementation
# LIFO (LastIn FirstOut)

class Stack():
    
    def __init__(self):
        self.items = []
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            pass     
    def is_empthy(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empthy():
            return self.items[-1]
    def display(self):
        """Display stack content"""
        print("Stack Items=>", self.items)
    

#initiate a stack
book_stack = Stack()
#add items to stack
book_stack.push("Book 1")
book_stack.push("Book 2")
book_stack.push("Book 3")
print("Empty",book_stack.is_empthy())
print("Peek Value",book_stack.peek())
book_stack.display()

#pop intems from stack top
book_stack.pop()
book_stack.display()
book_stack.pop()
book_stack.pop()
book_stack.pop()
book_stack.display()

print(book_stack.is_empthy())