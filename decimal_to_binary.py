#Decimal to binary using Stack
#solution steps
#implement Stack
#1. Function Receives an interger as argument
#2. divide the whole number by 2
#3. store the modulus remainder in a container
#4. repeat step 2 untill the remainder is zero
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



def convert_dec_to_bin(stack:Stack, number:int):
    #check type of passed value/number
    if type(number) != int:
        raise ValueError("Integer expected as argument")
    
    s = stack() #initialize stack

    while  number != 0 :
        #we need dividend and remainder
        dividend, remainder =  number // 2, number % 2
        s.push(str(remainder))
        number = dividend
    
    #reverse
    binary_value = ""
    while not s.is_empty():
        binary_value += s.pop()

    
    return int(binary_value)
     


import unittest
class DecToBinTests(unittest.TestCase):

    def test_1(self):
        returned = convert_dec_to_bin(Stack, 788)
        print("returned", returned)
        # self.assertEqual(returned,"dc,ba")
    
    # def test_2(self):
    #     returned = reverse_string("123456")
    #     self.assertEqual(returned,'654321')
    
    # def test_3(self):
    #     returned = reverse_string("ade")
    #     self.assertEqual(returned,"eda")
    
    # def test_4(self):
    #     returned = reverse_string("!evitacudE ot emocleW")
    #     self.assertEqual(returned,"Welcome to Educative!")
        
        
        
if __name__ == '__main__':
    unittest.main()
    