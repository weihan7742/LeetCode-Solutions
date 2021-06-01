class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == '':
            return True
        
        memo = [0 for _ in range(len(t)+1)]
        memo[0] = 0

        for i in range(1,len(memo)):
            index = i-1
            prev_memo = memo[index]
            if s[prev_memo] == t[index]:
                memo[i] = prev_memo + 1
            else:
                memo[i] = prev_memo

            if memo[i] == len(s):
                return True

        return False