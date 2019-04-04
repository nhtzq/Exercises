from typing import List

'''
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

1. nums will have a length in the range [1, 50].
2. Every nums[i] will be an integer in the range [0, 99].
'''

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        res = -1
        max_val = nums[0]
        max_idx = 0
        second_max_val = None
        
        if len(nums) == 1:
            res = 0
        else:
            if nums[1] > nums[0]:
                max_val = nums[1]
                max_idx = 1
                second_max_val = nums[0]
            else:
                second_max_val = nums[1]
                
        
            for idx, val in enumerate(nums[2:]):
                idx += 2
                if val == max_val:
                    second_max_val = val
                elif val > max_val:
                    second_max_val = max_val
                    max_val = val
                    max_idx = idx
                elif val > second_max_val:
                    second_max_val = val

            if max_val >= second_max_val * 2:
                res = max_idx
            
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 0, 1]
    ans = s.dominantIndex(nums)
    print(ans)