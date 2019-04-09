'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution(A):
    positive_A = []
    for i in A:
        if i > 0:
            positive_A.append(i)
            
    n = len(positive_A)
            
    for idx, val in enumerate(positive_A):
        val = abs(val)
        if val - 1 < n and positive_A[val - 1] > 0:
            positive_A[val - 1] = - positive_A[val - 1]
    
    for idx, val in enumerate(positive_A):
        if val > 0:
            return idx + 1
            
    return n + 1

if __name__ == '__main__':
    A = [1, 3, 6, 4, 1, 2]
    ans = solution(A)
    print(ans)