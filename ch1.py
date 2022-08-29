#Kth Maximum Integer in a List
import unittest

def find_kth_largest(kth:str, items:list)-> int:
    if kth > len(items):
        return -1

    items.sort(reverse=True)
    value = items[kth-1]
    return value

class KthLargestTests(unittest.TestCase):

    def test_1(self):
        returned = find_kth_largest(3, [12,456,34,8,80,890],)
        self.assertEqual(returned, 80)
        
    
    def test_2(self):
        returned = find_kth_largest(5, [89,0,34,456,567,67,90],)
        self.assertEqual(returned, 67)
        
        
    def test_3(self):
        returned = find_kth_largest(3, [1,2,3],)
        self.assertEqual(returned, 1)
        
    def test_4(self):
        returned = find_kth_largest(3, [1,2,3],)
        self.assertEqual(returned, 1)
        
    def test_5(self):
        returned = find_kth_largest(4, [1,2,3],)
        self.assertEqual(returned, -1)
    
    def test_6(self):
        returned = find_kth_largest(2, [40,35,82,14,22,66,53])
        self.assertEqual(returned, 66)
        
        
    def test_7(self):
        returned = find_kth_largest(6,[40,35,82,14,22,66,53])
        self.assertEqual(returned, 22)
        
        
    


if __name__ == '__main__':
    unittest.main()








