# Problem:
# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

# Your solution must run in O(logn)O(logn) time.

# Constraints:
# 1 <= nums.length <= 10000
# -10000 < nums[i], target < 1000
from typing import List

def binary_search(lo, hi, condition):
            while lo <= hi:
                mid = (lo + hi) //2
                result = condition(mid)
                if result == 'found':
                    return mid
                elif result == 'left':
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

def locate_val(nums, target):
        def condition(mid):
            if nums[mid] == target:
            # We only want to move left if values are repeated
                if mid + 1 < len(nums) and nums[mid+1] == target:
                    return 'left'
                else:
                    return 'found'
            # This assumes the list is sorted from high to low 
            elif nums[mid] > target:
                return 'left'
            else:
                return 'right'
        return binary_search(0, len(nums) - 1, condition)
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
         return locate_val(nums,target)

        
            
        
        
        
    
    