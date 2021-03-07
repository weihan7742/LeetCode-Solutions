class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        table = {}
        for i in range(len(nums)): 
            if nums[i] in table:
                j = 1 
                while j <= k: 
                    if nums[i] == nums[i-j]: 
                        return True
                    j += 1
            else:
                table[nums[i]] = 1
        return False
