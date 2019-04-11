'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.
'''
from typing import List
from collections import defaultdict

class Solution1:
    '''
    Solution 1 is stupid, please skip to other solutions. (Oh yeah this is my original solution.)
    '''
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        M = len(matrix) # Number of rows
        if M == 0:
            return res
        N = len(matrix[0]) # Number of cols
        if N == 0:
            return res
        is_up = True # Initial direction is UP
        i = 0 # Starting row index is 0
        j = 0 # Starting col index is 0
        
        while i < M and j < N:
            res.append(matrix[i][j])
            if is_up:
                # When going up, current element is on the right most col. Keep col idx, move row idx to the next one and change direction.
                if j + 1 == N:
                    i += 1
                    is_up = False
                    continue
                # When going up, current element is on the first row. Keep row idx, move col idx to the next one and change direction.
                if i - 1 == -1:
                    j += 1
                    is_up = False
                    continue
                i -= 1
                j += 1
            else:
                # When going down, current element is on the last row. Keep row idx, move col idx to the next one and change direction.
                if i + 1 == M:
                    j += 1
                    is_up = True
                    continue
                # When going down, current element is on the first col. Keep col idx, move row idx to the next one and change direction.
                if j - 1 == -1:
                    i += 1
                    is_up = True
                    continue
                i += 1
                j -= 1
                
        return res

class Solution2:
    '''
    reference: https://leetcode.com/problems/diagonal-traverse/discuss/97767/Simply-Python-Solution
    Simple two step approach:
    1- Group numbers according to diagonals. Sum of row+col in same diagonal is same.
    2- Reverse numbers in even diagonals before adding numbers to result list.
    '''
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return res
        
        dd = defaultdict(list)
        
        for i in range(len(matrix)): # Row idx
            for j in range(len(matrix[0])): # Col idx
                dd[i + j].append(matrix[i][j])
        
        for key in sorted(dd.keys()):
            if key % 2 == 0:
                dd[key].reverse()
                
            res += dd[key]
                
        return res

if __name__ == '__main__':
    s = Solution2()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    ans = s.findDiagonalOrder(matrix)
    print(ans)
