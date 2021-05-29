class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [float('-inf') for _ in range(len(nums)+1)]
        memo[0] = 0
        
        max_item = nums[0]
        
        for i in range(1,len(memo)):
            index = i-1
            memo[i] = max(nums[index],nums[index]+memo[i-1])

            if memo[i] > max_item: 
                max_item = memo[i]
        
        return max_item