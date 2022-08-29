# Problem Statement#
# You must implement the count_low_high() function. Its parameter is a list of numbers.
# If a number is greater than 50 or divisible by 3, it will count as a high. If these conditions are not met, the number is considered a low.
# At the end of the function, you must return a list that contains the number of lows and highs, in that order.

# In case the list is empty, you may return None.
# Sample Input#
# num_list = [20, 9, 51, 81, 50, 42, 77]
# Sample Output#
# [2, 5] # 2 lows and 5 highs

#Step to solution
#initialise stores [] for output
#range thru d list items
#perform conditional check and update stores accordingly
import unittest

def count_low_high(num_list):
    low_count = 0
    high_count = 0
    for item in range(0, len(num_list)):
        if num_list[item] > 50 or num_list[item]% 3 == 0:
            high_count += 1
        else:
            low_count += 1
            
    return[low_count, high_count]

def count_low_high(num_list):
    #using lambda and filter
    high_list = list(filter(lambda n: n > 50 or n % 3 == 0, num_list))
    low_list = list(filter(lambda n: n <= 50 and not n % 3 == 0, num_list))
    return [len(low_list), len(high_list)]


def count_low_high(num_list):
    #using list comprehension
    if (len(num_list)==0):
        return None
    high_list = len([n for n in num_list if n > 50 or n % 3 == 0])
    low_list = len([n for n in num_list if n <= 50 and not n % 3 == 0])
    return [low_list, high_list]




class CountLowHighTests(unittest.TestCase):

    def test_1(self):
        returned = count_low_high([20, 9, 51, 81, 50, 42, 77])
        self.assertEqual(returned, [2, 5])
        
        
if __name__ == '__main__':
    unittest.main()