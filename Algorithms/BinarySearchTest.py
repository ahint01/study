import unittest

from BinarySearch import locate_val

class TestBSA(unittest.TestCase):
    def test_left_side(self):
        arr = [13,11,10,7,4,3,0]
        val = 11
        result = locate_val(arr,val)
        self.assertEqual(result, 1)
    
    def test_right_side(self):
        arr = [13,11,10,7,4,3,0]
        val = 4
        result = locate_val(arr,val)
        self.assertEqual(result, 4)

    def test_empty_arr(self):
        arr = []
        val = 1
        result = locate_val(arr,val)
        self.assertEqual(result, -1)

    def test_val_not_in_arr(self):
        arr = [13,11,10,7,4,3,0]
        val = 21
        result = locate_val(arr,val)
        self.assertEqual(result, -1)

    def test_first_val(self):
        arr = [13,11,10,7,4,3,0]
        val = 13
        result = locate_val(arr,val)
        self.assertEqual(result, 0)

    def test_last_val(self):
        arr = [13,11,10,7,4,3,0]
        val = 0
        result = locate_val(arr,val)
        self.assertEqual(result, 6)

    def test_repeated_val(self): #we want the index of the first instance of the repeated val
        arr = [13,11,11,7,4,3,0]
        val = 11
        result = locate_val(arr,val)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

