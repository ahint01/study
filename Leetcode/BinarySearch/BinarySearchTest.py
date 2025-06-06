import unittest

from BinarySearch import Solution

my_instance = Solution

class TestBSA(unittest.TestCase):
    def test_left_side(self):
        nums = [0,3,4,7,10,11,13]
        target = 4
        result = my_instance.search(self,nums,target)
        self.assertEqual(result, 2)
    
    def test_right_side(self):
        nums = [0,3,4,7,10,11,13]
        target = 11
        result = my_instance.search(self,nums,target)
        self.assertEqual(result, 5)

    def test_empty_arr(self):
        nums = []
        target = 1
        result = my_instance.search(self,nums,target)
        self.assertEqual(result, -1)

    def test_val_not_in_arr(self):
        nums = [0,3,4,7,10,11,13]
        target = 21
        result = my_instance.search(self,nums,target)
        self.assertEqual(result, -1)

    def test_first_val(self):
        nums = [0,3,4,7,10,11,13]
        target = 0
        result = my_instance.search(self,nums,target)
        self.assertEqual(result, 0)

    def test_last_val(self):
        nums = [0,3,4,7,10,11,13]
        target = 13
        result = my_instance.search(self,nums,target)
        self.assertEqual(result, 6)

    def test_repeated_val(self): #we want the index of the first instance of the repeated val
        nums = [0,3,4,7,11,11,13]
        target = 11
        result = my_instance.search(self,nums,target)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

