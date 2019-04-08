from typing import List

'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carries = [0] * (n + 1)
        carries[-1] = 1
        res = []
        
        for i in range(n):
            idx = - (i + 1)
            tmp = digits[idx] + carries[idx]
            if tmp >= 10:
                carries[idx - 1] = 1
            res = [tmp % 10] + res
        if carries[0] == 1:
            res = [1] + res
        return res

class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        add = 1
        
        for i in range(n):
            idx = - (i + 1)
            tmp = digits[idx] + add
            add = tmp // 10
            digits[idx] = tmp % 10
        if add == 1:
            digits = [1] + digits
        return digits

if __name__ == '__main__':
    s1 = Solution1()
    digits = [4,3,2,1]
    ans1 = s1.plusOne(digits)
    print(ans1)

    s2 = Solution2()
    digits = [4,3,2,1]
    ans2 = s2.plusOne(digits)
    print(ans2)