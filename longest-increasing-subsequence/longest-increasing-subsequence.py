class Solution:
    def lengthOfLIS(self, lst: List[int]) -> int:

        # Initialize memo 
        memo = [1 for _ in range(len(lst))]
        memo_index = [0 for _ in range(len(lst))]

        for i in range(1,len(memo)):
            for k in range(0,i):
                if lst[i] > lst[k] and memo[i] < memo[k]+1: 
                    memo[i] = memo[k] + 1
                    memo_index[i] = k

        return max(memo)