class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for i in nums: 
            try:
                hash_table[i]
            except KeyError:
                hash_table[i] = 1 
            else:
                return True
        return False