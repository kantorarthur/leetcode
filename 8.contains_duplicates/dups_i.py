class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicates = {}

        for num in nums:
            if duplicates.get(num, 0) != 0:
                return True
            duplicates[num] = duplicates.get(num, 0) + 1
        
        return False