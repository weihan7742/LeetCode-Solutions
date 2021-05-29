class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n == 0:
            return [0]
        
        memo = [0 for _ in range(n+1)]
        memo[0] = 0
        memo[1] = 1
        for i in range(2,n+1):

            if i%2 == 0:
                memo[i] = memo[i//2]
            else:
                memo[i] = memo[i//2] + 1

        return memo