from typing import List

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