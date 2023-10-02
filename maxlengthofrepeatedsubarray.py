'''
Problem: Maximum Length of Repeated Subarray

Description:

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Input: A: [1,2,3,2,1], B: [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3, 2, 1].
'''

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        max_length = 0
        
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    max_length = max(max_length, dp[i][j])
        
        return max_length
